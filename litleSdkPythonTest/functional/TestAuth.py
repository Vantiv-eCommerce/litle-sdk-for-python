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
    
def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuth)
    return suite

if __name__ =='__main__':
    unittest.main()