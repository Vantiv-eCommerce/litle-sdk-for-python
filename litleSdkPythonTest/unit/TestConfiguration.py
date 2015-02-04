#Copyright (c) 2011-2015 Litle & Co.
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

import os, sys
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest
from mock import *

class TestConfiguration(unittest.TestCase):

    def testV8BackwardsCompatibility(self):
        config = Configuration()
        config.setUser("User")
        config.setPassword("Pass")
        config.setMerchantId("123")
        config.setUrl("Sandbox")
        config.setProxy("1")
        config.setVersion("2")
        config.setReportGroup("3")
        config.setTimeout("4")
        config.setPrintXml(True)
        
        self.assertEquals(config.username, "User")
        self.assertEquals(config.password, "Pass")
        self.assertEquals(config.merchantId, "123")
        self.assertEquals(config.url, "https://www.testlitle.com/sandbox/communicator/online")
        self.assertEquals(config.proxy, "1")
        self.assertEquals(config.version, "2")
        self.assertEquals(config.reportGroup, "3")
        self.assertEquals(config.timeout, "4")
        self.assertEquals(config.printXml, True)
        

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestConfiguration)
    return suite

if __name__ =='__main__':
    unittest.main()