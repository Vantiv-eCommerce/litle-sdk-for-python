#!/usr/bin/env python
import sys, os, re, string
lib_path = os.path.abspath('../lib/litleXmlFields.py')
sys.path.append(lib_path)

#File = open('../lib/litleXmlFields',"W",0)

def replace_in_files(xfile):
    
        cregex1=re.compile('GroupSequence')
        cregex2=re.compile('min_occurs=1')
        cregex3=re.compile('occurs')
    
        seqFlag=0
        replaceflag=0
        readlines=open(xfile,'r').readlines()
         # intialize the list counter
        listindex = -1
        # search and replace in current file printing to the user changed lines
        for currentline in readlines:
             # increment the list counter
            listindex = listindex + 1

            # if the regexp is found
            if cregex1.search(currentline):
                seqFlag=1
            elif (not cregex3.search(currentline)):
                seqFlag=0
            elif cregex2.search(currentline):
                if(seqFlag):
                    # make the substitution
                    f=re.sub('min_occurs=1','min_occurs=0L',currentline)
                    # print the current filename, the old string and the new string
                    print '\n' + xfile
                    print '- ' + currentline ,
                    if currentline[-1:]!='\n': print '\n' ,
                    print '+ ' + f ,
                    if f[-1:]!='\n': print '\n' ,
    
                    readlines[listindex] = f
                    replaceflag=1
                            
        # if some text was replaced
        # overwrite the original file
        if replaceflag==1:

            # open the file for writting  
            write_file=open(xfile,'w') 

            # overwrite the file  
            for line in readlines:
                write_file.write(line)

            # close the file
            write_file.close()
            
replace_in_files(lib_path)
print 'hello'