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
import base64
import os, sys
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest

class TestAuth(unittest.TestCase):
    
    def testSimpleAuthWithCard(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
    
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'
    
        authorization.card = card
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
            
        self.assertEquals("000",response.response)
    
    #8.29
    def testSimpleAuthWithSecondaryAmountAndApplepay(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.secondaryAmount = '10'
        
        
        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "yoyo"
        applepay.version = '8.29'
        header=litleXmlFields.applepayHeaderType()
        header.applicationData='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.ephemeralPublicKey ='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.publicKeyHash='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.transactionId='1024'
        applepay.header=header
        authorization.applepay = applepay
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
            
        self.assertEquals("Approved",response.message)
        self.assertEquals(106,response.applepayResponse.transactionAmount) #test for response
        
    def testSimpleAuthWithPaypal(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
    
        paypal = litleXmlFields.payPal()
        paypal.payerId = "1234"
        paypal.token = "1234"
        paypal.transactionId = '123456'
        
    
        authorization.paypal = paypal
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
            
        self.assertEquals("Approved",response.message)
       
    
    def testPosWithoutCapabilityAndEntryMode(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '123456'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
    
        pos = litleXmlFields.pos()
        pos.cardholderId = "pin"
        authorization.pos = pos
            
        card = litleXmlFields.cardType()
        card.number = "4100000000000002"
        card.expDate = "1210"
        card.type = 'VI'
        card.cardValidationNum = '1213'
    
        authorization.card = card
    
        litle = litleOnlineRequest(config)
        with self.assertRaises(Exception):
            litle.sendRequest(authorization)

    def testAccountUpdate(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
    
        card = litleXmlFields.cardType()
        card.number = "4100100000000000"
        card.expDate = "1210"
        card.type = 'VI'
        card.cardValidationNum = '1213'
    
        authorization.card = card
    
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
            
        self.assertEquals("4100100000000000",response.accountUpdater.originalCardInfo.number)

    def testTrackData(self):
        authorization = litleXmlFields.authorization()
        authorization.id = 'AX54321678'
        authorization.reportGroup = 'RG27'
        authorization.orderId = '12z58743y1'
        authorization.amount = 12522
        authorization.orderSource = 'retail'

        billToAddress = litleXmlFields.contact()
        billToAddress.zip = '95032'
        authorization.billToAddress = billToAddress

        card = litleXmlFields.cardType()
        card.track = "%B40000001^Doe/JohnP^06041...?;40001=0604101064200?"
        authorization.card = card

        pos = litleXmlFields.pos()
        pos.capability = 'magstripe'
        pos.entryMode = 'completeread'
        pos.cardholderId = 'signature'
        authorization.pos = pos

        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)

        self.assertEquals('Approved', response.message)

    def testListOfTaxAmounts(self):
        authorization = litleXmlFields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'

        enhanced = litleXmlFields.enhancedData()
        dt1 = litleXmlFields.detailTax()
        dt1.taxAmount = 100
        enhanced.detailTax.append(dt1)
        dt2 = litleXmlFields.detailTax()
        dt2.taxAmount = 200
        enhanced.detailTax.append(dt2)
        authorization.enhancedData = enhanced

        card = litleXmlFields.cardType()
        card.number = '4100000000000001'
        card.expDate = '1215'
        card.type = 'VI'
        authorization.card = card

        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)

        self.assertEquals('Approved', response.message)
        
    def testAuthenticationValueMaxlength(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.secondaryAmount = '10'
        
        card = litleXmlFields.cardType()
        card.number = '4100000000000001'
        card.expDate = '1215'
        card.type = 'VI'
        authorization.card = card
        
        fraudCheck=litleXmlFields.fraudCheckType()
        encoded = base64.b64encode('data to be encodedaaaaaaaaaabbbbbbbbbbcc') #generating a base64 encoded data of length 56, expect no exception
        fraudCheck.authenticationValue=encoded
        authorization.cardholderAuthentication=fraudCheck
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals('Approved', response.message)
    
    def testOrderSourceTypeWithApplePay(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'applepay'
         
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type='VI'
        
        authorization.card = card
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals('Approved', response.message)
def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuth)
    return suite

if __name__ =='__main__':
    unittest.main()