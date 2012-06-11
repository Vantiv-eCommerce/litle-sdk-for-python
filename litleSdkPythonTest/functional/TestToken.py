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

import os, sys
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest

class TestToken(unittest.TestCase):
    
    def testSimpleToken(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        token.accountNumber = '1233456789103801'
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals(response.message, "Account number was successfully registered")
        
    def testSimpleTokenWithPaypage(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        token.paypageRegistrationId = '1233456789101112'
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals(response.message, "Account number was successfully registered")
        
    def testSimpleTokenWithEcheck(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        echeck = litleXmlFields.echeckForTokenType()
        echeck.accNum = "12344565"
        echeck.routingNum = "123476545"
        token.echeckForToken = echeck
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals(response.message, "Account number was successfully registered")
        
    def testTokenEcheckMissingRequiredField(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        echeck = litleXmlFields.echeckForTokenType()
        echeck.routingNum = "123476545"
        token.echeckForToken = echeck
        
        litle = litleOnlineRequest(config)
        with self.assertRaises(Exception):
            litle.sendRequest(token)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestToken)
    return suite

if __name__ =='__main__':
    unittest.main()  