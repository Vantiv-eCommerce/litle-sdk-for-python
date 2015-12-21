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
        token.id = "id"

        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals(response.message, "Account number was successfully registered")
        
    def testSimpleTokenWithPaypage(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        token.paypageRegistrationId = '1233456789101112'
	token.id = 'id'

        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals(response.message, "Account number was successfully registered")
        
    def testSimpleTokenWithEcheck(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
	token.id = 'id'

        echeck = litleXmlFields.echeckForTokenType()
        echeck.accNum = "12344565"
        echeck.routingNum = "123476545"
        token.echeckForToken = echeck
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals(response.message, "Account number was successfully registered")
        
    def testSimpleTokenWithApplepay(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
	token.id = 'id'

        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "sign"
        applepay.version = '12345'
        header=litleXmlFields.applepayHeaderType()
        header.applicationData='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.ephemeralPublicKey ='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.publicKeyHash='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.transactionId='1024'
        applepay.header=header
        token.applepay = applepay
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals(response.message, "Account number was successfully registered")
        self.assertEqual(0, response.applepayResponse.transactionAmount)
        
    def testTokenEcheckMissingRequiredField(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
	token.id = 'id'

        echeck = litleXmlFields.echeckForTokenType()
        echeck.routingNum = "123476545"
        token.echeckForToken = echeck
        
        litle = litleOnlineRequest(config)
        with self.assertRaises(Exception):
            litle.sendRequest(token)

    def testCovertPaypageRegistrationIdIntoToken(self):
        tokenRequest = litleXmlFields.registerTokenRequest()
        tokenRequest.orderId = '12345'
        tokenRequest.paypageRegistrationId = '123456789012345678901324567890abcdefghi'
	tokenRequest.id = 'id'

        litleXml =  litleOnlineRequest(config)
        tokenResponse = litleXml.sendRequest(tokenRequest)
        self.assertEquals(tokenResponse.litleToken, "1111222233334444")

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestToken)
    return suite

if __name__ =='__main__':
    unittest.main()  
