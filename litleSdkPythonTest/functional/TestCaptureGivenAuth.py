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
import pyxb

class TestCaptureGivenAuth(unittest.TestCase):
    
    def testSimpleCaptureGivenAuth(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 20)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        CaptureGivenAuth.authInformation = AuthInfo
        CaptureGivenAuth.orderSource = "ecommerce"
        Card = litleXmlFields.cardType()
        Card.number = "4100000000000000"
        Card.expDate = "1210"
        Card.type = 'VI'
        Card.cardValidationNum = '1210'
        CaptureGivenAuth.card = Card
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        self.assertEquals("Approved",response.message)
        
    def testSimpleCaptureGivenAuthWithToken(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        CaptureGivenAuth.authInformation = AuthInfo
        CaptureGivenAuth.orderSource = "ecommerce"
        Token = litleXmlFields.cardTokenType()
        Token.litleToken = "123456789101112"
        Token.expDate = "1210"
        Token.type = 'VI'
        Token.cardValidationNum = '555'
        CaptureGivenAuth.token = Token
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        self.assertEquals("Approved",response.message)
        
    def testComplexCaptureGivenAuth(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        CaptureGivenAuth.authInformation = AuthInfo
        Contact = litleXmlFields.contact();
        Contact.name="Bob"
        Contact.city="lowell"
        Contact.state="MA"
        Contact.email="litle.com"
        CaptureGivenAuth.billToAddress = Contact
        ProcessingInstruct = litleXmlFields.processingInstructions()
        ProcessingInstruct.bypassVelocityCheck = True
        CaptureGivenAuth.processingInstructions = ProcessingInstruct
        CaptureGivenAuth.orderSource = "ecommerce"
        Card = litleXmlFields.cardType()
        Card.number = "4100000000000000"
        Card.expDate = "1210"
        Card.type = 'VI'
        Card.cardValidationNum = '1210'
        CaptureGivenAuth.card = Card
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        self.assertEquals("Approved",response.message)
        
        
    def testAuthInfo(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        FraudResult = litleXmlFields.fraudResult()
        FraudResult.avsResult = "12"
        FraudResult.cardValidationResult = "123"
        FraudResult.authenticationResult = "1"
        FraudResult.advancedAvsResult = "123"
        AuthInfo.fraudResult = FraudResult
        CaptureGivenAuth.authInformation = AuthInfo
        CaptureGivenAuth.orderSource = "ecommerce"
        Card = litleXmlFields.cardType()
        Card.number = "4100000000000000"
        Card.expDate = "1210"
        Card.type = 'VI'
        Card.cardValidationNum = '555'
        CaptureGivenAuth.card = Card
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        self.assertEquals("Approved",response.message)
   
def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCaptureGivenAuth)
    return suite

if __name__ =='__main__':
    unittest.main()