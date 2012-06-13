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

class certTest3(unittest.TestCase):
#    
    def test32(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '32'
        authorization.amount = 10010
        authorization.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.name = "John Smith"
        billtoaddress.addressLine1 = "1 Main St."
        billtoaddress.city = "Burlington"
        billtoaddress.state = "MA"
        billtoaddress.zip = "01803-3747"
        billtoaddress.country = 'US'
        authorization.billToAddress = billtoaddress
        
        card = litleXmlFields.cardType()
        card.number = "4457010000000009"
        card.expDate = "0112"
        card.type = 'VI'
        card.cardValidationNum = "349"
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("11111 ", response.authCode)
        self.assertEquals("01", response.fraudResult.avsResult)
        self.assertEquals("M", response.fraudResult.cardValidationResult)
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.litleTxnId
        capture.amount = 5005
        captureResponse = litleXml.sendRequest(capture)
        self.assertEquals("000", captureResponse.response)
        self.assertEquals("Approved", captureResponse.message)
        
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = response.litleTxnId
        reversalResponse = litleXml.sendRequest(reversal)
        self.assertEquals("111", reversalResponse.response)
        self.assertEquals("Authorization amount has already been depleted", reversalResponse.message)

    def test33(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '33'
        authorization.amount = 20020
        authorization.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.name = "Mike J. Hammer"
        billtoaddress.addressLine1 = "2 Main St."
        billtoaddress.addressLine2 = "Apt. 222"
        billtoaddress.city = "Riverside"
        billtoaddress.state = "RI"
        billtoaddress.zip = "02915"
        billtoaddress.country = 'US'
        authorization.billToAddress = billtoaddress
        
        card = litleXmlFields.cardType()
        card.number = "5112010000000003"
        card.expDate = "0212"
        card.type = 'MC'
        card.cardValidationNum = "261"
        authorization.card = card
        
        fraud = litleXmlFields.fraudCheckType()
        fraud.authenticationValue = "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = fraud
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals("000", response.response)
        self.assertEquals("Approved", response.message)
        self.assertEquals("22222", response.authCode)
        self.assertEquals("10", response.fraudResult.avsResult)
        self.assertEquals("M", response.fraudResult.cardValidationResult)
        
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = response.litleTxnId
        reversalResponse = litleXml.sendRequest(reversal)
        self.assertEquals("000", reversalResponse.response)
        self.assertEquals("Approved", reversalResponse.message)

    def test34(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '34'
        authorization.amount = 30030
        authorization.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.name = "Eileen Jones"
        billtoaddress.addressLine1 = "3 Main St."
        billtoaddress.city = "Bloomfield"
        billtoaddress.state = "CT"
        billtoaddress.zip = "06002"
        billtoaddress.country = 'US'
        authorization.billToAddress = billtoaddress
        
        card = litleXmlFields.cardType()
        card.number = "6011010000000003"
        card.expDate = "0312"
        card.type = 'DI'
        card.cardValidationNum = "758"
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("33333", response.authCode)
        self.assertEquals("10", response.fraudResult.avsResult)
        self.assertEquals("M", response.fraudResult.cardValidationResult)
        
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = response.litleTxnId
        reversalResponse = litleXml.sendRequest(reversal)
        self.assertEquals("000", reversalResponse.response)
        self.assertEquals("Approved", reversalResponse.message)
        
    def test35(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '35'
        authorization.amount = 40040
        authorization.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.name = "Bob Black"
        billtoaddress.addressLine1 = "4 Main St."
        billtoaddress.city = "Laurel"
        billtoaddress.state = "MD"
        billtoaddress.zip = "20708"
        billtoaddress.country = 'US'
        authorization.billToAddress = billtoaddress
        
        card = litleXmlFields.cardType()
        card.number = "375001000000005"
        card.expDate = "0412"
        card.type = 'AX'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("44444", response.authCode)
        self.assertEquals("12", response.fraudResult.avsResult)
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.litleTxnId
        capture.amount = 20020
        captureResponse = litleXml.sendRequest(capture)
        self.assertEquals("000", captureResponse.response)
        self.assertEquals("Approved", captureResponse.message)
        
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = response.litleTxnId
        reversalResponse = litleXml.sendRequest(reversal)
        self.assertEquals("000", reversalResponse.response)
        self.assertEquals("Approved", reversalResponse.message)
        
    def test36(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '36'
        authorization.amount = 20500
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "375000026600004"
        card.expDate = "0512"
        card.type = 'AX'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = response.litleTxnId
        reversal.amount = 10000
        reversalResponse = litleXml.sendRequest(reversal)
        self.assertEquals("336", reversalResponse.response)
        self.assertEquals("Reversal Amount does not match Authorization amount", reversalResponse.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(certTest3)
    return suite

if __name__ =='__main__':
    unittest.main()