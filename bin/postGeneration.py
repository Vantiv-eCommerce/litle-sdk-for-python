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
#def cregex(find, replace, currentline, xfile):
#    f = re.sub(tx, tx2 + ' ' + am2 + ' ' + ve2, currentline)
#    print '\n' + xfile
#    print '- ' + currentline ,
#    if currentline[-1:]!='\n': print '\n' ,
#    print '+ ' + f
#    if f[-1:]!='\n': print '\n' ,
#    print 'adding lines'
#    readlines[listindex] = f
#    write_file=open(xfile,'w') 
#    for line in readlines:
#        write_file.write(line)
#    write_file.close()


def fixecheckSale(xfile):
#    find class CTD_ANON_36 (transactionTypeWithReportGroup):
#
#    find __litleTxnId.name() : __litleTxnId,
#    add on next line    __amount.name() : __amount,
#    add on next line    __verify.name() : __verify,
#    delete next   __amount.name() : __amount,
#    delete next    __verify.name() : __verify,

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
                print 'got in echeck'
            elif (echeckFlag and (not txnFlag) and txnid.search(currentline)):
                txnFlag=1
                f = re.sub(tx, tx2 + ' ' + am2 + ' ' + ve2, currentline)
                print listindex
                print '\n' + xfile
                print '- ' + currentline ,
                if currentline[-1:]!='\n': print '\n' ,
                print '+ ' + f
                if f[-1:]!='\n': print '\n' ,
                print 'adding lines'
                readlines[listindex] = f
                write_file=open(xfile,'w') 
                for line in readlines:
                    write_file.write(line)
                write_file.close()
            elif (txnFlag and amount.search(currentline)):
                g = re.sub(am,'',currentline)
                print '\n' + xfile
                print '- ' + currentline ,
                if currentline[-1:]!='\n': print '\n' ,
                print '+ ' + g
                if  g[-1:]!='\n': print '\n' ,
                readlines[listindex] = g
                write_file=open(xfile,'w') 
                for line in readlines:
                    write_file.write(line)
                write_file.close()
                print 'removing am'
            elif (txnFlag and verify.search(currentline)):
                h = re.sub(ve,'',currentline)
                print '\n' + xfile
                print '- ' + currentline ,
                if currentline[-1:]!='\n': print '\n' ,
                print '+ ' + h
                if  h[-1:]!='\n': print '\n' ,
                readlines[listindex] = h
                write_file=open(xfile,'w') 
                for line in readlines:
                    write_file.write(line)
                write_file.close()
                print 'removing ve'
                echeckFlag = 0
                txnFlag = 0
                
fixecheckSale(lib_path)
print 'hello'