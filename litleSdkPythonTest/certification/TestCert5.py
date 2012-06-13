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

class certTest5(unittest.TestCase):
    
    def test50(self):
        
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '50'
        token.accountNumber = "4457119922390123"
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals("445711",response.bin)
        self.assertEquals( "VI",response.type)
        self.assertEquals( "801",response.response)
        self.assertEquals("1111222233330123",response.litleToken)
        self.assertEquals("Account number was successfully registered",response.message)
        
        
    def test51(self):
        
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '51'
        token.accountNumber = "4457119999999999"
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals( "820",response.response)
        self.assertEquals("Credit card number was invalid",response.message)
        
        
    def test52(self):
        
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '52'
        token.accountNumber = "4457119922390123"
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals("445711",response.bin)
        self.assertEquals( "VI",response.type)
        self.assertEquals( "802",response.response)
        self.assertEquals("1111222233330123",response.litleToken)
        self.assertEquals("Account number was previously registered",response.message)
        
        
    def test53(self):
        
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '53'
        echeck = litleXmlFields.echeckForTokenType()
        echeck.accNum = "1099999998"
        echeck.routingNum = "114567895"
        token.echeckForToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals("998",response.eCheckAccountSuffix)
        self.assertEquals( "EC",response.type)
        self.assertEquals( "801",response.response)
        self.assertEquals("111922223333000998",response.litleToken)
        self.assertEquals("Account number was successfully registered",response.message)
        
        
    def test54(self):
        
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '54'
        echeck = litleXmlFields.echeckForTokenType()
        echeck.accNum = "1022222102"
        echeck.routingNum = "1145_7895"
        token.echeckForToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals( "900",response.response)
        self.assertEquals("Invalid bank routing number",response.message)
        
        
    def test55(self):
        
        auth = litleXmlFields.authorization()
        auth.orderId = "55"
        auth.amount = 15000
        auth.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "5435101234510196"
        card.expDate = "1112"
        card.type = 'MC'
        card.cardValidationNum = "987"
        auth.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(auth)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("801", response.tokenResponse.tokenResponseCode)
        self.assertEquals("Account number was successfully registered", response.tokenResponse.tokenMessage)
        self.assertEquals('MC', response.tokenResponse.type)
        self.assertEquals("543510", response.tokenResponse.bin)
        
        
    def test56(self):
        
        auth = litleXmlFields.authorization()
        auth.orderId = "56"
        auth.amount = 15000
        auth.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "5435109999999999"
        card.expDate = "1112"
        card.type = 'MC'
        card.cardValidationNum = "987"
        auth.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(auth)
        self.assertEquals( "301",response.response)
        self.assertEquals("Invalid account number",response.message)
        
        
    def test57(self):
        
        auth = litleXmlFields.authorization()
        auth.orderId = "57"
        auth.amount = 15000
        auth.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "5435101234510196"
        card.expDate = "1112"
        card.type = 'MC'
        card.cardValidationNum = "987"
        auth.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(auth)
        self.assertEquals( "000",response.response)
        self.assertEquals("Approved",response.message)
        self.assertEquals("802", response.tokenResponse.tokenResponseCode)
        self.assertEquals("Account number was previously registered", response.tokenResponse.tokenMessage)
        self.assertEquals('MC', response.tokenResponse.type)
        self.assertEquals("543510", response.tokenResponse.bin)
        
        
    def test59(self):
        
        auth = litleXmlFields.authorization()
        auth.orderId = "59"
        auth.amount = 15000
        auth.orderSource = 'ecommerce'
        
        token = litleXmlFields.cardTokenType()
        token.litleToken = "1712990000040196"
        token.expDate = "1112"
        auth.token = token
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(auth)
        self.assertEquals("822", response.response)
        self.assertEquals("Token was not found", response.message)
        
        
    def test60(self):
        
        auth = litleXmlFields.authorization()
        auth.orderId = "60"
        auth.amount = 15000
        auth.orderSource = 'ecommerce'
        
        token = litleXmlFields.cardTokenType()
        token.litleToken = "1712999999999999"
        token.expDate = "1112"
        auth.token = token
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(auth)
        self.assertEquals("823", response.response)
        self.assertEquals("Token was invalid", response.message)

    def test61(self):
        
        sale = litleXmlFields.echeckSale()
        sale.orderId = "61"
        sale.amount = 15000
        sale.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.firstName = "Tom"
        billtoaddress.lastName = "Black"
        sale.billToAddress = billtoaddress
        
        echeck = litleXmlFields.echeck()
        echeck.accNum = "1099999003"
        echeck.accType = 'Checking'
        echeck.routingNum = "114567895"
        sale.echeckOrEcheckToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals("801", response.tokenResponse.tokenResponseCode)
        self.assertEquals("Account number was successfully registered", response.tokenResponse.tokenMessage)
        self.assertEquals('EC', response.tokenResponse.type)
        self.assertEquals("111922223333444003", response.tokenResponse.litleToken)
        
        
    def test62(self):
        
        sale = litleXmlFields.echeckSale()
        sale.orderId = "62"
        sale.amount = 15000
        sale.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.firstName = "Tom"
        billtoaddress.lastName = "Black"
        sale.billToAddress = billtoaddress
        
        echeck = litleXmlFields.echeck()
        echeck.accNum = "1099999999"
        echeck.accType = 'Checking'
        echeck.routingNum = "114567895"
        sale.echeckOrEcheckToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals("801", response.tokenResponse.tokenResponseCode)
        self.assertEquals("Account number was successfully registered", response.tokenResponse.tokenMessage)
        self.assertEquals('EC', response.tokenResponse.type)
        self.assertEquals("999", response.tokenResponse.eCheckAccountSuffix)
        self.assertEquals("111922223333444999", response.tokenResponse.litleToken)
        
    def test63(self):
        
        sale = litleXmlFields.echeckSale()
        sale.orderId = "63"
        sale.amount = 15000
        sale.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.firstName = "Tom"
        billtoaddress.lastName = "Black"
        sale.billToAddress = billtoaddress
        
        echeck = litleXmlFields.echeck()
        echeck.accNum = "1099999999"
        echeck.accType = 'Checking'
        echeck.routingNum = "214567892"
        sale.echeckOrEcheckToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals("801", response.tokenResponse.tokenResponseCode)
        self.assertEquals("Account number was successfully registered", response.tokenResponse.tokenMessage)
        self.assertEquals('EC', response.tokenResponse.type)
        self.assertEquals("999", response.tokenResponse.eCheckAccountSuffix)
        self.assertEquals("111922223333555999", response.tokenResponse.litleToken)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(certTest5)
    return suite

if __name__ =='__main__':
    unittest.main()