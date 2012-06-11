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

class certTest1(unittest.TestCase):
    
    def test1Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1'
        authorization.amount = 10010
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="John Smith"
        contact.addressLine1="1 Main St."
        contact.city="Burlington"
        contact.state="MA"
        contact.zip="01803-3747"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "4457010000000009"
        card.expDate = "0112"
        card.cardValidationNum = "349"
        card.type = 'VI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("11111 ",response.authCode)
        self.assertEquals( "01",response.fraudResult.avsResult)
        self.assertEquals("M",response.fraudResult.cardValidationResult);
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.response)
        self.assertEquals("Approved",captureresponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)
        
    def test1AVS(self):
            
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1'
        authorization.amount = 000
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="John Smith"
        contact.addressLine1="1 Main St."
        contact.city="Burlington"
        contact.state="MA"
        contact.zip="01803-3747"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "4457010000000009"
        card.expDate = "0112"
        card.cardValidationNum = "349"
        card.type = 'VI'

        authorization.card = card
            
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("11111 ",response.authCode)
        self.assertEquals( "01",response.fraudResult.avsResult)
        self.assertEquals("M",response.fraudResult.cardValidationResult);
        
    def test1Sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '1'
        sale.amount = 10010
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="John Smith"
        contact.addressLine1="1 Main St."
        contact.city="Burlington"
        contact.state="MA"
        contact.zip="01803-3747"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "4457010000000009"
        card.expDate = "0112"
        card.cardValidationNum = "349"
        card.type = 'VI'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("11111 ",response.authCode)
        self.assertEquals( "01",response.fraudResult.avsResult)
        self.assertEquals("M",response.fraudResult.cardValidationResult);
       
        credit = litleXmlFields.credit()
        credit.litleTxnId = response.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)
        
    def test2Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '2'
        authorization.amount = 20020
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mike J. Hammer"
        contact.addressLine1="2 Main St."
        contact.addressLine2="Apt. 222"
        contact.city="Riverside"
        contact.state="RI"
        contact.zip="02915"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010000000003"
        card.expDate = "0212"
        card.cardValidationNum = "261"
        card.type = 'MC'

        authorization.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("22222",response.authCode)
        self.assertEquals( "10",response.fraudResult.avsResult)
        self.assertEquals("M",response.fraudResult.cardValidationResult);
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.response)
        self.assertEquals("Approved",captureresponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)
        
        
    def test2AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '2'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mike J. Hammer"
        contact.addressLine1="2 Main St."
        contact.addressLine2="Apt. 222"
        contact.city="Riverside"
        contact.state="RI"
        contact.zip="02915"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010000000003"
        card.expDate = "0212"
        card.cardValidationNum = "261"
        card.type = 'MC'

        authorization.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("22222",response.authCode)
        self.assertEquals( "10",response.fraudResult.avsResult)
        self.assertEquals("M",response.fraudResult.cardValidationResult);

        
    def test2Sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '2'
        sale.amount = 20020
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mike J. Hammer"
        contact.addressLine1="2 Main St."
        contact.addressLine2="Apt. 222"
        contact.city="Riverside"
        contact.state="RI"
        contact.zip="02915"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010000000003"
        card.expDate = "0212"
        card.cardValidationNum = "261"
        card.type = 'MC'

        sale.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        sale.fraudCheck = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("22222",response.authCode)
        self.assertEquals( "10",response.fraudResult.avsResult)
        self.assertEquals("M",response.fraudResult.cardValidationResult);
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = response.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)    
        
        
    def test3Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '3'
        authorization.amount = 30030
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Eileen Jones"
        contact.addressLine1="3 Main St."
        contact.city="Bloomfield"
        contact.state="CT"
        contact.zip="06002"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010000000003"
        card.expDate = "0312"
        card.cardValidationNum = "758"
        card.type = 'DI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("33333",response.authCode)
        self.assertEquals( "10",response.fraudResult.avsResult)
        self.assertEquals("M",response.fraudResult.cardValidationResult);
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.response)
        self.assertEquals("Approved",captureresponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)
        
        
    def test3AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '3'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Eileen Jones"
        contact.addressLine1="3 Main St."
        contact.city="Bloomfield"
        contact.state="CT"
        contact.zip="06002"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010000000003"
        card.expDate = "0312"
        card.cardValidationNum = "758"
        card.type = 'DI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("33333",response.authCode)
        self.assertEquals( "10",response.fraudResult.avsResult)
        self.assertEquals("M",response.fraudResult.cardValidationResult);
        
    def test3Sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '3'
        sale.amount = 30030
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Eileen Jones"
        contact.addressLine1="3 Main St."
        contact.city="Bloomfield"
        contact.state="CT"
        contact.zip="06002"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010000000003"
        card.expDate = "0312"
        card.cardValidationNum = "758"
        card.type = 'DI'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("33333",response.authCode)
        self.assertEquals( "10",response.fraudResult.avsResult)
        self.assertEquals("M",response.fraudResult.cardValidationResult);
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = response.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)
        
        
    def test4Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '4'
        authorization.amount = 40040
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Bob Black"
        contact.addressLine1="4 Main St."
        contact.city="Laurel"
        contact.state="MD"
        contact.zip="20708"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001000000005"
        card.expDate = "0412"
        card.cardValidationNum = "758"
        card.type = 'AX'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("44444",response.authCode)
        self.assertEquals( "12",response.fraudResult.avsResult)
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.response)
        self.assertEquals("Approved",captureresponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)
        
        
    def test4AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '4'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Bob Black"
        contact.addressLine1="4 Main St."
        contact.city="Laurel"
        contact.state="MD"
        contact.zip="20708"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001000000005"
        card.expDate = "0412"
        card.cardValidationNum = "758"
        card.type = 'AX'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("44444",response.authCode)
        self.assertEquals( "12",response.fraudResult.avsResult)
        
        
    def test4Sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '4'
        sale.amount = 40040
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Bob Black"
        contact.addressLine1="4 Main St."
        contact.city="Laurel"
        contact.state="MD"
        contact.zip="20708"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001000000005"
        card.expDate = "0412"
        card.cardValidationNum = "758"
        card.type = 'AX'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("44444",response.authCode)
        self.assertEquals( "12",response.fraudResult.avsResult)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = response.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)
        
        
    def test5Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '5'
        authorization.amount = 50050
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4457010200000007"
        card.expDate = "0512"
        card.cardValidationNum = "463"
        card.type = 'VI'

        authorization.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("55555 ",response.authCode)
        self.assertEquals( "32",response.fraudResult.avsResult)
        self.assertEquals("N",response.fraudResult.cardValidationResult);
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.response)
        self.assertEquals("Approved",captureresponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)
        
        
    def test5AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '5'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4457010200000007"
        card.expDate = "0512"
        card.cardValidationNum = "463"
        card.type = 'VI'

        authorization.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("55555 ",response.authCode)
        self.assertEquals( "32",response.fraudResult.avsResult)
        self.assertEquals("N",response.fraudResult.cardValidationResult);
        
        
    def test5Sale(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '5'
        authorization.amount = 50050
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4457010200000007"
        card.expDate = "0512"
        card.cardValidationNum = "463"
        card.type = 'VI'

        authorization.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("55555 ",response.authCode)
        self.assertEquals( "32",response.fraudResult.avsResult)
        self.assertEquals("N",response.fraudResult.cardValidationResult);
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = response.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)
        
        
    def test6Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '6'
        authorization.amount = 60060
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Joe Green"
        contact.addressLine1="6 Main St."
        contact.city="Derry"
        contact.state="NH"
        contact.zip="03038"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "4457010100000008"
        card.expDate = "0612"
        card.cardValidationNum = "992"
        card.type = 'VI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "110",response.response)
        self.assertEquals("Insufficient Funds",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        self.assertEquals("P",response.fraudResult.cardValidationResult);
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.response)
        self.assertEquals("Approved",captureresponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.response)
        self.assertEquals("Approved",creditresponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.response)
        self.assertEquals("Approved",voidresponse.message)
        
        
    def test6Sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '6'
        sale.amount = 60060
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Joe Green"
        contact.addressLine1="6 Main St."
        contact.city="Derry"
        contact.state="NH"
        contact.zip="03038"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "4457010100000008"
        card.expDate = "0612"
        card.cardValidationNum = "992"
        card.type = 'VI'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "110",response.response)
        self.assertEquals("Insufficient Funds",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        self.assertEquals("P",response.fraudResult.cardValidationResult);
        
        void = litleXmlFields.void()
        void.litleTxnId = response.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "360",voidresponse.response)
        self.assertEquals("No transaction found with specified litleTxnId",voidresponse.message)
        
        
    def test7Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '7'
        authorization.amount = 70070
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Jane Murray"
        contact.addressLine1="7 Main St."
        contact.city="Amesbury"
        contact.state="MA"
        contact.zip="01913"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010100000002"
        card.expDate = "0712"
        card.cardValidationNum = "251"
        card.type = 'MC'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "301",response.response)
        self.assertEquals("Invalid Account Number",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        self.assertEquals("N",response.fraudResult.cardValidationResult);
        
        
    def test7AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '7'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Jane Murray"
        contact.addressLine1="7 Main St."
        contact.city="Amesbury"
        contact.state="MA"
        contact.zip="01913"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010100000002"
        card.expDate = "0712"
        card.cardValidationNum = "251"
        card.type = 'MC'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "301",response.response)
        self.assertEquals("Invalid Account Number",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        self.assertEquals("N",response.fraudResult.cardValidationResult);
        
        
    def test7Sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '7'
        sale.amount = 70070
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Jane Murray"
        contact.addressLine1="7 Main St."
        contact.city="Amesbury"
        contact.state="MA"
        contact.zip="01913"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010100000002"
        card.expDate = "0712"
        card.cardValidationNum = "251"
        card.type = 'MC'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "301",response.response)
        self.assertEquals("Invalid Account Number",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        self.assertEquals("N",response.fraudResult.cardValidationResult);
        
        
    def test8Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '8'
        authorization.amount = 80080
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mark Johnson"
        contact.addressLine1="8 Main St."
        contact.city="Manchester"
        contact.state="NH"
        contact.zip="03101"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010100000002"
        card.expDate = "0812"
        card.cardValidationNum = "184"
        card.type = 'DI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "123",response.response)
        self.assertEquals("Call Discover",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        self.assertEquals("P",response.fraudResult.cardValidationResult);
        
        
    def test8AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '8'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mark Johnson"
        contact.addressLine1="8 Main St."
        contact.city="Manchester"
        contact.state="NH"
        contact.zip="03101"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010100000002"
        card.expDate = "0812"
        card.cardValidationNum = "184"
        card.type = 'DI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "123",response.response)
        self.assertEquals("Call Discover",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        self.assertEquals("P",response.fraudResult.cardValidationResult);
        
        
    def test8Sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '8'
        sale.amount = 80080
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mark Johnson"
        contact.addressLine1="8 Main St."
        contact.city="Manchester"
        contact.state="NH"
        contact.zip="03101"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010100000002"
        card.expDate = "0812"
        card.cardValidationNum = "184"
        card.type = 'DI'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "123",response.response)
        self.assertEquals("Call Discover",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        self.assertEquals("P",response.fraudResult.cardValidationResult);
        
        
    def test9Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '9'
        authorization.amount = 90090
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="James Miller"
        contact.addressLine1="9 Main St."
        contact.city="Boston"
        contact.state="MA"
        contact.zip="02134"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001010000003"
        card.expDate = "0912"
        card.cardValidationNum = "0421"
        card.type = 'AX'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "303",response.response)
        self.assertEquals("Pick Up Card",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        
        
    def test10Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '9'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="James Miller"
        contact.addressLine1="9 Main St."
        contact.city="Boston"
        contact.state="MA"
        contact.zip="02134"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001010000003"
        card.expDate = "0912"
        card.cardValidationNum = "0421"
        card.type = 'AX'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "303",response.response)
        self.assertEquals("Pick Up Card",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        
        
    def test11Auth(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '9'
        sale.amount = 90090
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="James Miller"
        contact.addressLine1="9 Main St."
        contact.city="Boston"
        contact.state="MA"
        contact.zip="02134"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001010000003"
        card.expDate = "0912"
        card.cardValidationNum = "0421"
        card.type = 'AX'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "303",response.response)
        self.assertEquals("Pick Up Card",response.message)
        self.assertEquals( "34",response.fraudResult.avsResult)
        
        
    def test12Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '10'
        authorization.amount = 40000
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4457010140000141"
        card.expDate = "0912"
        card.type = 'VI'

        authorization.card = card
        
        authorization.allowPartialAuth = True
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "010",response.response)
        self.assertEquals("Partially Approved",response.message)
        self.assertEquals( 32000L,response.approvedAmount)
        
        
    def test13Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '11'
        authorization.amount = 60000
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "5112010140000004"
        card.expDate = "1111"
        card.type = 'MC'

        authorization.card = card
        
        authorization.allowPartialAuth = True
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "010",response.response)
        self.assertEquals("Partially Approved",response.message)
        self.assertEquals( 48000L,response.approvedAmount)
        
        
    def test14Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '12'
        authorization.amount = 50000
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "375001014000009"
        card.expDate = "0412"
        card.type = 'AX'

        authorization.card = card
        
        authorization.allowPartialAuth = True
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "010",response.response)
        self.assertEquals("Partially Approved",response.message)
        self.assertEquals( 40000L,response.approvedAmount)
        
    
    def test15Auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '13'
        authorization.amount = 15000
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "6011010140000004"
        card.expDate = "0812"
        card.type = 'DI'

        authorization.card = card
        
        authorization.allowPartialAuth = True
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "010",response.response)
        self.assertEquals("Partially Approved",response.message)
        self.assertEquals( 12000L,response.approvedAmount)
        
def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(certTest1)
    return suite

if __name__ =='__main__':
    unittest.main()