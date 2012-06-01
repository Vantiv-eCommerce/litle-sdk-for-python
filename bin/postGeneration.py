#!/usr/bin/env python
import sys, os, re, string
lib_path = os.path.abspath('../lib/litleXmlFields.py')
sys.path.append(lib_path)

#File = open('../lib/litleXmlFields',"W",0)

#def replace_in_files(xfile):
#    
#        cregex1=re.compile('GroupSequence')
#        cregex2=re.compile('min_occurs=1')
#        cregex3=re.compile('occurs')
#    
#        seqFlag=0
#        replaceflag=0
#        readlines=open(xfile,'r').readlines()
#         # intialize the list counter
#        listindex = -1
#        # search and replace in current file printing to the user changed lines
#        for currentline in readlines:
#             # increment the list counter
#            listindex = listindex + 1
#
#            # if the regexp is found
#            if cregex1.search(currentline):
#                seqFlag=1
#            elif (not cregex3.search(currentline)):
#                seqFlag=0
#            elif cregex2.search(currentline):
#                if(seqFlag):
#                    # make the substitution
#                    f=re.sub('min_occurs=1','min_occurs=0L',currentline)
#                    # print the current filename, the old string and the new string
#                    print '\n' + xfile
#                    print '- ' + currentline ,
#                    if currentline[-1:]!='\n': print '\n' ,
#                    print '+ ' + f ,
#                    if f[-1:]!='\n': print '\n' ,
#    
#                    readlines[listindex] = f
#                    replaceflag=1
#                            
#        # if some text was replaced
#        # overwrite the original file
#        if replaceflag==1:
#
#            # open the file for writting  
#            write_file=open(xfile,'w') 
#
#            # overwrite the file  
#            for line in readlines:
#                write_file.write(line)
#
#            # close the file
#            write_file.close()

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
    
    tx2 = "__litleTxnId.name() : __litleTxnId,"
    am2 = "__amount.name() : __amount,"
    ve2 = '__verify.name() : __verify,'
    
    echeck=re.compile('class CTD_ANON_36 ')
    txnid=re.compile(tx)
    amount=re.compile(am)
    verify=re.compile(ve)
    echeckFlag=0
    txnFlag = 0
    readlines=open(xfile,'r').readlines()
         # intialize the list counter
    listindex = -1
        # search and replace in current file printing to the user changed lines
    for currentline in readlines:
             # increment the list counter
            listindex = listindex + 1

            # if the regexp is found
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