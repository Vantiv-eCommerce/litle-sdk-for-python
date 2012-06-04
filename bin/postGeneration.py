#!/usr/bin/env python
import sys, os, re, string
lib_path = os.path.abspath('../lib/litleXmlFields.py')
sys.path.append(lib_path)


def replace_in_file(xfile, find, replace):
        found=re.compile(find)

        readlines=open(xfile,'r').readlines()
        
        listindex = -1
      
        for currentline in readlines:
            
            listindex = listindex + 1
            # if the regexp is found
            if found.search(currentline):
                cregex(find, replace, currentline, xfile, listindex, readlines)

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


def fixecheckSale(xfile):
    tx = "__litleTxnId.name\(\) : __litleTxnId,"
    am = "__amount.name\(\) : __amount,"
    ve = '__verify.name\(\) : __verify,'
    alr = '__litleTxnId.name\(\) : __litleTxnId, __amount.name\(\) : __amount, __verify.name\(\) : __verify,'
        
    tx2 = "__litleTxnId.name() : __litleTxnId,"
    am2 = "__amount.name() : __amount,"
    ve2 = '__verify.name() : __verify,'
    
    echeck=re.compile('class CTD_ANON_36 ')
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
                
fixecheckSale(lib_path)
replace_in_file(lib_path,"u'orderId'\)\), min_occurs=1","u'orderId')), min_occurs=0L")
replace_in_file(lib_path,"u'amount'\)\), min_occurs=1","u'amount')), min_occurs=0L")
replace_in_file(lib_path,"u'orderSource'\)\), min_occurs=1","u'orderSource')), min_occurs=0L")
replace_in_file(lib_path,"u'postDate'\)\), min_occurs=1","u'postDate')), min_occurs=0L")
replace_in_file(lib_path,"u'capability'\)\), min_occurs=1","u'capability')), min_occurs=0L")
replace_in_file(lib_path,"u'entryMode'\)\), min_occurs=1","u'entryMode')), min_occurs=0L")
replace_in_file(lib_path,"u'cardholderId'\)\), min_occurs=1","u'cardholderId')), min_occurs=0L")

replace_in_file(lib_path,"u'billToAddress'\)\), min_occurs=1L","u'billToAddress')), min_occurs=0L")
replace_in_file(lib_path,"u'echeckOrEcheckToken'\)\), min_occurs=1","u'echeckOrEcheckToken')), min_occurs=0L")
replace_in_file(lib_path,"u'litleToken'\)\), min_occurs=1","u'litleToken')), min_occurs=0L")
replace_in_file(lib_path,"u'routingNum'\)\), min_occurs=1","u'routingNum')), min_occurs=0L")
replace_in_file(lib_path,"u'accType'\)\), min_occurs=1","u'accType')), min_occurs=0L")
replace_in_file(lib_path,"u'accNum'\)\), min_occurs=1","u'accNum')), min_occurs=0L")
replace_in_file(lib_path,"u'authInformation'\)\), min_occurs=1","u'authInformation')), min_occurs=0L")
replace_in_file(lib_path,"u'authDate'\)\), min_occurs=1","u'authDate')), min_occurs=0L")
replace_in_file(lib_path,"u'authCode'\)\), min_occurs=1","u'authCode')), min_occurs=0L")
replace_in_file(lib_path,"u'litleTxnId'\)\), min_occurs=1L","u'litleTxnId')), min_occurs=0L")


replace_in_file(lib_path,"u'billToAddress'\)\), min_occurs=1","u'billToAddress')), min_occurs=0L")
replace_in_file(lib_path,"u'response'\)\), min_occurs=1","u'response')), min_occurs=0L")
replace_in_file(lib_path,"u'responseTime'\)\), min_occurs=1","u'responseTime')), min_occurs=0L")
replace_in_file(lib_path,"u'message'\)\), min_occurs=1","u'message')), min_occurs=0L")
replace_in_file(lib_path,"u'payerId'\)\), min_occurs=1","u'payerId')), min_occurs=0L")
replace_in_file(lib_path,"u'transactionId'\)\), min_occurs=1","u'transactionId')), min_occurs=0L")
replace_in_file(lib_path,"min_occurs=0LL","min_occurs=0L")