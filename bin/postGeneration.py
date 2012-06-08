#!/usr/bin/env python
import sys
import os
import re
import string

lib_path = os.path.abspath('../litleSdkPython/litleXmlFields.py')
sys.path.append(lib_path)

#replaces all instances of find with replace
def replace_in_file(xfile, find, replace):
    found = re.compile(find)
    readlines = open(xfile, 'r').readlines()   
    listindex = -1   
    for currentline in readlines:        
        listindex = listindex + 1
        # if the regexp is found
        if found.search(currentline):
            cregex(find, replace, currentline, xfile, listindex, readlines)
            
def isInFile(xfile, find):
    already = re.compile(find)
    doneFlag = 0
    readlines = open(xfile, 'r').readlines()
    for currentline in readlines:
        if(already.search(currentline)):
            doneFlag = 1
            break
    return doneFlag
    
def makeNotRequired(xfile, field):
    replace_in_file(xfile, "u'" + field + "'\)\), min_occurs=1","u'" + field +
                    "')), min_occurs=0L")

def cregex(find, replace, currentline, xfile, listindex, readlines):
    f = re.sub(find, replace, currentline)
    print '\n' + xfile
    print '- ' + currentline ,
    if currentline[-1:] != '\n': print '\n' ,
    print '+ ' + f
    if f[-1:] != '\n': print '\n' ,
    readlines[listindex] = f
    write_file=open(xfile,'w')
    for line in readlines:
        write_file.write(line)
    write_file.close()
    
def changeCreateFromDom(xfile):    
    replace_in_file(lib_path, "return pyxb.binding.basis.element.AnyCreateFromDOM\(node, _fallback_namespace=default_namespace\)",
                    "return LitleAnyCreateFromDOM(pyxb.binding.basis.element,node, _fallback_namespace=default_namespace)")
    replace_in_file(lib_path, " saxer = pyxb.binding.saxer.make_parser\(fallback_namespace=Namespace.fallbackNamespace\(\), location_base=location_base\)",
                    "")
    replace_in_file(lib_path, " handler = saxer.getContentHandler\(\)", "")
    replace_in_file(lib_path, " saxer.parse\(StringIO.StringIO\(xml_text\)\)",
                    "")
    replace_in_file(lib_path, " instance = handler.rootObject\(\)", "")
    replace_in_file(lib_path, " return instance", "")
    replace_in_file(lib_path, " if pyxb.XMLStyle_saxer != pyxb._XMLStyle:",
                    " if (True):")

def addLitleAnyCreateFromDOM(xfile):
    replace_in_file(lib_path, " return LitleAnyCreateFromDOM\(pyxb.binding.basis.element,node, _fallback_namespace=default_namespace\)",
                    " return LitleAnyCreateFromDOM(pyxb.binding.basis.element,node, _fallback_namespace=default_namespace)\n\n\
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
    line = field + " = pyxb.binding.basis.element\(pyxb.namespace.ExpandedName\(Namespace, u'" + field + "'\),"
    rightLine = re.compile(line)
    readlines = open(xfile, 'r').readlines()
    for currentline in readlines:
        if(rightLine.search(currentline)):
            wholeLine = currentline
    i = wholeLine.find('CTD_ANON')
    temp = wholeLine[i:]
    i = temp.find('\)')
    return temp[:i-1]

def removeMinOccurs(xfile):
    txnIdStr = "litleTxnId"
    groupChoiceStr = " pyxb.binding.content.GroupChoice\("
    groupModelStr = "_GroupModel_" 
    minOccurs1Str = "min_occurs=1"
    minOccurs = "min_occurs=0L"
    closeParenStr = "    \)"
    
    txnId = re.compile(txnIdStr)
    groupChoice = re.compile(groupChoiceStr)
    groupModel = re.compile(groupModelStr)
    minOccurs1 = re.compile(minOccurs1Str)
    closeParen = re.compile(closeParenStr)
    
    readlines = open(xfile, 'r').readlines()

    listindex = -1
    choiceFlag = 0
    findTxnFlag = 0
    foundTxnFlag = 0
    groupModelNum = None
    for currentline in readlines:
         # increment the list counter
        listindex = listindex + 1

        # if the regexp is found
        if (groupModel.search(currentline)):
            findTxnFlag = 1
            i = currentline.find('.')
            temp = currentline[:i+1]
            i = temp.find(' ')
            groupModelNum = currentline[i-1:]
        elif (findTxnFlag and txnId.search(currentline)):
            foundTxnFlag = 1
            findTxnFlag = 0
            
        if (groupChoice.search(currentline)):
            choiceFlag = 1
        elif (closeParen.search(currentline)):
            choiceFlag = 0
        elif (minOccurs1.search(currentline) and not (txnId.search(currentline)) and not (choiceFlag)):
            if(groupModelNum != None):
                if(currentline.count(groupModelNum) == 0):
                    cregex(minOccurs1Str, minOccurs, currentline, xfile, listindex, readlines)
                else:
                    foundTxnFlag = 0
                    groupModelNum = None
            else:
                cregex(minOccurs1Str, minOccurs, currentline, xfile, listindex, readlines)
    replace_in_file(lib_path, "min_occurs=0LL", "min_occurs=0L")

# fix paypal as credit field
def fixPaypalinCredit(xfile):
    creditAnon = findAnon(xfile, "credit")
    line = creditAnon + "._AddElement\(pyxb.binding.basis.element\(pyxb.namespace.ExpandedName\(Namespace, u'paypal'\)"
    rightLine = re.compile(line)
    readlines = open(xfile, 'r').readlines()
    for currentline in readlines:
        if(rightLine.search(currentline)):
            wholeLine = currentline
    i = wholeLine.find('\n')
    wholeLine = wholeLine[:i-1]
    wholeLine = wholeLine.replace(')', '\)')
    wholeLine = wholeLine.replace('(', '\(')
    replace_in_file(xfile, wholeLine, creditAnon + "._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal'), payPal, scope=" + creditAnon + ")")
    

def fixChoices(xfile):
    line = "._GroupModel_.*?, min_occurs=1, max_occurs=1\)"
    lineToSkip = findAnon(xfile, "authorization") + "._GroupModel_,"
    lineToSkip2 = findAnon(xfile, "credit") + "._GroupModel_2"
    lineToSkip3 = findAnon(xfile, "echeckCredit") + "._GroupModel_,"
    lineToSkip4 = findAnon(xfile, "echeckSale") + "._GroupModel_,"
    rightLine = re.compile(line)
    readlines = open(xfile, 'r').readlines()
    count2 = 0;
    for currentline in readlines:
        if(rightLine.search(currentline)):
            if (currentline.count(lineToSkip2) == 0 and 
                currentline.count(lineToSkip) == 0 and 
                currentline.count(lineToSkip3) == 0 and 
                currentline.count(lineToSkip4) == 0):
                temp = currentline
                count2 = count2 + 1
                toReplace = temp.replace("min_occurs=1,", "min_occurs=0L,")
                currentline = currentline.replace(')', '\)')
                currentline = currentline.replace('(', '\(')
                replace_in_file(xfile, currentline, toReplace)
            
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
    
    echeck = re.compile(anon)
    txnid = re.compile(tx)
    amount = re.compile(am)
    verify = re.compile(ve)
    already = re.compile(alr)
    echeckFlag = 0
    txnFlag = 0
    readlines = open(xfile, 'r').readlines()

    listindex = -1

    for currentline in readlines:
             # increment the list counter
            listindex = listindex + 1

            # if the regexp is found
            if(already.search(currentline)):
                print 'the file has already been processed'
                break
            if ((not echeckFlag) and echeck.search(currentline)):
                echeckFlag = 1
            elif (echeckFlag and (not txnFlag) and txnid.search(currentline)):
                txnFlag = 1
                cregex(tx, tx2 + ' ' + am2 + ' ' + ve2, currentline, xfile, 
                       listindex, readlines)
            elif (txnFlag and amount.search(currentline)):
                cregex(am, '', currentline, xfile, listindex, readlines)
            elif (txnFlag and verify.search(currentline)):
                cregex(ve, '', currentline, xfile, listindex, readlines)
                echeckFlag = 0
                txnFlag = 0

# Run actual Changes
fixecheckSale(lib_path)
removeMinOccurs(lib_path)
if (not isInFile(lib_path, "import xml.dom")):
    replace_in_file(lib_path, "import sys", "import sys\nimport xml.dom")
fixPaypalinCredit(lib_path)
fixChoices(lib_path)

changeCreateFromDom(lib_path)
if (not isInFile(lib_path, "def LitleAnyCreateFromDOM \(cls, node, _fallback_namespace\):")):
    addLitleAnyCreateFromDOM(lib_path)