#!/usr/bin/env python
import sys, os, re, string
lib_path = os.path.abspath('../litleSdkPythonTest/testConfig.py')
sys.path.append(lib_path)

print "Setup for Litle SDK Tests" 
user = raw_input( 'Enter your user, any value will work for testing: ' )
password = raw_input( 'Enter your password, any value will work for testing:  ' )
merchantId = raw_input( 'Enter your merchant Id, any value will work for testing:  ' )
proxy = raw_input( 'Enter your proxy, if no proxy hit enter:' )


write_file=open(lib_path,'w')
write_file.write('import os, sys\n')
#write_file.write("lib_path = os.path.abspath('../../lib')\n")
#write_file.write('sys.path.append(lib_path)\n')
write_file.write('from litleSdkPython.litleOnlineRequest import *\n')
write_file.write('config = Configuration()\n')
write_file.write('config.setUser("'+user+'")\n')
write_file.write('config.setPassword("'+password+'")\n')
write_file.write('config.setMerchantId("'+merchantId+'")\n')
write_file.write("config.setReportGroup('DefaultReportGroup')\n")
if (proxy != ""):
    write_file.write('config.setProxy("'+proxy+'")\n')
write_file.write("config.setUrl('Sandbox')\n")
write_file.close()
print 'Setup Finished, You May now run tests'