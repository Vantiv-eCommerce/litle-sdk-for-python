#!/usr/bin/env python
import sys, os, re, string
lib_path = os.path.abspath('../lib/litleXmlFields.py')
sys.path.append(lib_path)

#replaces all instances of find with replace
def replace_in_file(xfile, find, replace):
    found=re.compile(find)
    readlines=open(xfile,'r').readlines()   
    listindex = -1   
    for currentline in readlines:        
        listindex = listindex + 1
        # if the regexp is found
        if found.search(currentline):
            cregex(find, replace, currentline, xfile, listindex, readlines)
            
def isInFile(xfile, find):
    already=re.compile(find)
    doneFlag=0
    readlines=open(xfile,'r').readlines()
    for currentline in readlines:
        if(already.search(currentline)):
            doneFlag=1
            break
    return doneFlag
    
def makeNotRequired(xfile, field):
    replace_in_file(xfile,"u'"+field+"'\)\), min_occurs=1","u'"+field+"')), min_occurs=0L")

def cregex(find, replace, currentline, xfile, listindex, readlines):
    f = re.sub(find, replace, currentline)
    print '\n' + xfile
    print '- ' + currentline ,
    if currentline[-1:]!='\n': print '\n' ,
    print '+ ' + f
    if f[-1:]!='\n': print '\n' ,
    readlines[listindex] = f
    write_file=open(xfile,'w')
    for line in readlines:
        write_file.write(line)
    write_file.close()
    
def changeCreateFromDom(xfile):    
    replace_in_file(lib_path,"return pyxb.binding.basis.element.AnyCreateFromDOM\(node, _fallback_namespace=default_namespace\)","return LitleAnyCreateFromDOM(pyxb.binding.basis.element,node, _fallback_namespace=default_namespace)")
    replace_in_file(lib_path," saxer = pyxb.binding.saxer.make_parser\(fallback_namespace=Namespace.fallbackNamespace\(\), location_base=location_base\)","")
    replace_in_file(lib_path," handler = saxer.getContentHandler\(\)","")
    replace_in_file(lib_path," saxer.parse\(StringIO.StringIO\(xml_text\)\)","")
    replace_in_file(lib_path," instance = handler.rootObject\(\)","")
    replace_in_file(lib_path," return instance","")
    replace_in_file(lib_path," if pyxb.XMLStyle_saxer != pyxb._XMLStyle:"," if (True):")

def addLitleAnyCreateFromDOM(xfile):
    replace_in_file(lib_path," return LitleAnyCreateFromDOM\(pyxb.binding.basis.element,node, _fallback_namespace=default_namespace\)"," return LitleAnyCreateFromDOM(pyxb.binding.basis.element,node, _fallback_namespace=default_namespace)\n\n\
def LitleAnyCreateFromDOM (cls, node, _fallback_namespace):\n\
    if xml.dom.Node.DOCUMENT_NODE == node.nodeType:\n\
        node = node.documentElement\n\
    expanded_name = pyxb.namespace.ExpandedName(node, fallback_namespace=_fallback_namespace)\n\
    elt = expanded_name.elementBinding()\n\
    if elt is None:\n\
        return\n\
    assert isinstance(elt, pyxb.binding.basis.element)\n\
    return elt._createFromDOM(node, expanded_name, _fallback_namespace=_fallback_namespace)")

#finds the CTD_ANON number corresponding to the given field
def findAnon(xfile, field):
    line = field +" = pyxb.binding.basis.element\(pyxb.namespace.ExpandedName\(Namespace, u'"+field+"'\),"
    rightLine=re.compile(line)
    readlines=open(xfile,'r').readlines()
    for currentline in readlines:
        if(rightLine.search(currentline)):
            wholeLine = currentline
    i = wholeLine.find('CTD_ANON')
    temp =wholeLine[i:]
    i = temp.find('\)')
    return temp[:i-1]

# fix paypal as credit field
def fixPaypalinCredit(xfile):
    creditAnon = findAnon(xfile,"credit")
    line = creditAnon+"._AddElement\(pyxb.binding.basis.element\(pyxb.namespace.ExpandedName\(Namespace, u'paypal'\)"
    rightLine=re.compile(line)
    readlines=open(xfile,'r').readlines()
    for currentline in readlines:
        if(rightLine.search(currentline)):
            wholeLine = currentline
    i = wholeLine.find('\n')
    wholeLine = wholeLine[:i-1]
    wholeLine = wholeLine.replace(')','\)')
    wholeLine = wholeLine.replace('(','\(')
    replace_in_file(xfile,wholeLine,creditAnon+"._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal'), payPal, scope="+creditAnon+")")

#reorders the fields in echeckSale to be right
def fixecheckSale(xfile):
    tx = "__litleTxnId.name\(\) : __litleTxnId,"
    am = "__amount.name\(\) : __amount,"
    ve = '__verify.name\(\) : __verify,'
    alr = '__litleTxnId.name\(\) : __litleTxnId, __amount.name\(\) : __amount, __verify.name\(\) : __verify,'
    anon = 'class '+findAnon(lib_path, 'echeckSale')
        
    tx2 = "__litleTxnId.name() : __litleTxnId,"
    am2 = "__amount.name() : __amount,"
    ve2 = '__verify.name() : __verify,'
    
    echeck=re.compile(anon)
    txnid=re.compile(tx)
    amount=re.compile(am)
    verify=re.compile(ve)
    already=re.compile(alr)
    echeckFlag=0
    txnFlag = 0
    readlines=open(xfile,'r').readlines()

    listindex = -1

    for currentline in readlines:
             # increment the list counter
            listindex = listindex + 1

            # if the regexp is found
            if(already.search(currentline)):
                print 'the file has already been processed'
                break
            if ((not echeckFlag) and echeck.search(currentline)):
                echeckFlag=1
            elif (echeckFlag and (not txnFlag) and txnid.search(currentline)):
                txnFlag=1
                cregex(tx, tx2 + ' ' + am2 + ' ' + ve2, currentline, xfile, listindex, readlines)
            elif (txnFlag and amount.search(currentline)):
                cregex(am, '', currentline, xfile, listindex, readlines)
            elif (txnFlag and verify.search(currentline)):
                cregex(ve, '', currentline, xfile, listindex, readlines)
                echeckFlag = 0
                txnFlag = 0

# Run actual Changes
fixecheckSale(lib_path)
makeNotRequired(lib_path,'orderId')
makeNotRequired(lib_path,'amount')
makeNotRequired(lib_path,'orderSource')
makeNotRequired(lib_path,'postDate')
makeNotRequired(lib_path,'capability')
makeNotRequired(lib_path,'entryMode')
makeNotRequired(lib_path,'cardholderId')
makeNotRequired(lib_path,'billToAddress')
makeNotRequired(lib_path,'echeckOrEcheckToken')
makeNotRequired(lib_path,'litleToken')
makeNotRequired(lib_path,'routingNum')
makeNotRequired(lib_path,'accType')
makeNotRequired(lib_path,'accNum')
makeNotRequired(lib_path,'authInformation')
makeNotRequired(lib_path,'authCode')
makeNotRequired(lib_path,'authDate')
makeNotRequired(lib_path,'response')
makeNotRequired(lib_path,'responseTime')
makeNotRequired(lib_path,'message')
makeNotRequired(lib_path,'payerId')
makeNotRequired(lib_path,'transactionId')
makeNotRequired(lib_path,'tokenResponseCode')
makeNotRequired(lib_path,'tokenMessage')
makeNotRequired(lib_path,'accNum')
makeNotRequired(lib_path,'sellerId')
makeNotRequired(lib_path,'sellerMerchantCategoryCode')
makeNotRequired(lib_path,'originalAccountInfo')
makeNotRequired(lib_path,'newAccountInfo')
makeNotRequired(lib_path,'originalTokenInfo')
makeNotRequired(lib_path,'newTokenInfo')
makeNotRequired(lib_path,'originalCardInfo')
makeNotRequired(lib_path,'newCardInfo')
makeNotRequired(lib_path,'orignalCardTokenInfo')
makeNotRequired(lib_path,'newCardTokenInfo')
makeNotRequired(lib_path,'taxAmount')
makeNotRequired(lib_path,'totalHealthcareAmount')
makeNotRequired(lib_path,'healthcareAmounts')
makeNotRequired(lib_path,'IIASFlag')
makeNotRequired(lib_path,'expDate')
makeNotRequired(lib_path,'licenseNumber')
makeNotRequired(lib_path,'availableBalance')
makeNotRequired(lib_path,'code')
makeNotRequired(lib_path,'number')
makeNotRequired(lib_path,'paypageRegistrationId')
makeNotRequired(lib_path,'bmlMerchantId')
makeNotRequired(lib_path,'itemDescription')
if (not isInFile(lib_path, "import xml.dom")):
    replace_in_file(lib_path,"import sys","import sys\nimport xml.dom")
fixPaypalinCredit(lib_path)
#replace_in_file(lib_path,"CTD_ANON_18._AddElement\(pyxb.binding.basis.element\(pyxb.namespace.ExpandedName\(Namespace, u'paypal'\), CTD_ANON_44, scope=CTD_ANON_18\)\)","CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal'), payPal, scope=CTD_ANON_18))")
replace_in_file(lib_path,"min_occurs=0LL","min_occurs=0L")
changeCreateFromDom(lib_path)
if (not isInFile(lib_path, "def LitleAnyCreateFromDOM \(cls, node, _fallback_namespace\):")):
    addLitleAnyCreateFromDOM(lib_path)