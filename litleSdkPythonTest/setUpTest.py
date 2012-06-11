#Copyright (c) 2011-2012 Litle & Co.
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

#!/usr/bin/env python
import sys
import os
import re
import string

lib_path = os.path.abspath('testConfig.py')
sys.path.append(lib_path)

print "Setup for Litle SDK Tests" 
user = raw_input('Enter your user, any value will work for testing: ')
password = raw_input('Enter your password, any value will work for testing:  ')
merchantId = raw_input('Enter your merchant Id, any value will work for testing:  ')
proxy = raw_input('Enter your proxy, if no proxy hit enter: ')


write_file = open(lib_path, 'w')
write_file.write('import os, sys\n')
write_file.write('from litleSdkPython.litleOnlineRequest import *\n')
write_file.write('config = Configuration()\n')
write_file.write('config.setUser("' + user + '")\n')
write_file.write('config.setPassword("' + password + '")\n')
write_file.write('config.setMerchantId("' + merchantId + '")\n')
write_file.write("config.setReportGroup('DefaultReportGroup')\n")
if (proxy != ""):
    write_file.write('config.setProxy("' + proxy + '")\n')
write_file.write("config.setUrl('Sandbox')\n")
write_file.close()
print 'Setup Finished, You May now run tests'
