from SetupTest import *
import unittest

class certTest5(unittest.TestCase):
    
    def test50(self):
        
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '50'
        token.accountNumber = "4457119922390123"
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(token)
        self.assertEquals("445711",response.transactionResponse.bin)
        self.assertEquals( "VI",response.transactionResponse.type)
        self.assertEquals( "801",response.transactionResponse.response)
        self.assertEquals("1111222233330123",response.transactionResponse.litleToken)
        self.assertEquals("Account number was successfully registered",response.transactionResponse.message)
        
        
    def test51(self):
        
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '51'
        token.accountNumber = "4457119999999999"
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(token)
        self.assertEquals( "820",response.transactionResponse.response)
        self.assertEquals("Credit card number was invalid",response.transactionResponse.message)
        
        
    def test52(self):
        
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '52'
        token.accountNumber = "4457119922390123"
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(token)
        self.assertEquals("445711",response.transactionResponse.bin)
        self.assertEquals( "VI",response.transactionResponse.type)
        self.assertEquals( "802",response.transactionResponse.response)
        self.assertEquals("1111222233330123",response.transactionResponse.litleToken)
        self.assertEquals("Account number was previously registered",response.transactionResponse.message)
        
        
    def test53(self):
        
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '53'
        echeck = litleXmlFields.echeckForTokenType()
        echeck.accNum = "1099999998"
        echeck.routingNum = "114567895"
        token.echeckForToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(token)
        self.assertEquals("998",response.transactionResponse.eCheckAccountSuffix)
        self.assertEquals( "EC",response.transactionResponse.type)
        self.assertEquals( "801",response.transactionResponse.response)
        self.assertEquals("111922223333000998",response.transactionResponse.litleToken)
        self.assertEquals("Account number was successfully registered",response.transactionResponse.message)
        
        
    def test54(self):
        
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '54'
        echeck = litleXmlFields.echeckForTokenType()
        echeck.accNum = "1022222102"
        echeck.routingNum = "1145_7895"
        token.echeckForToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(token)
        self.assertEquals( "900",response.transactionResponse.response)
        self.assertEquals("Invalid bank routing number",response.transactionResponse.message)
        
        
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
        response = litleXml.litleXmlMapper(auth)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("801", response.transactionResponse.tokenReponse.tokenResponseCode)
        self.assertEquals("Account number was successfully registered", response.transactionResponse.tokenResponse.tokenMessage)
        self.assertEquals('EC', response.transactionResponse.tokenResponse.type)
        self.assertEquals("543510", response.transactionResponse.tokenResponse.bin)
        
        
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
        response = litleXml.litleXmlMapper(auth)
        self.assertEquals( "301",response.transactionResponse.response)
        self.assertEquals("Invalid account number",response.transactionResponse.message)
        
        
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
        response = litleXml.litleXmlMapper(auth)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("802", response.transactionResponse.tokenReponse.tokenResponseCode)
        self.assertEquals("Account number was previously registered", response.transactionResponse.tokenResponse.tokenMessage)
        self.assertEquals('MC', response.transactionResponse.tokenResponse.type)
        self.assertEquals("543510", response.transactionResponse.tokenResponse.bin)
        
        
#    def test59(self):
#        
#        auth = litleXmlFields.authorization()
#        auth.orderId = "59"
#        auth.amount = 15000
#        auth.orderSource = 'ecommerce'
#        
#        token = litleXmlFields.cardTokenType()
#        token.litleToken = "1712990000040196"
#        token.expDate = "1112"
#        auth.token = token
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(auth)
#        self.assertEquals("822", response.transactionResponse.response)
#        self.assertEquals("Token was not found", response.transactionResponse.message)
#        
#        
#    def test60(self):
#        
#        auth = litleXmlFields.authorization()
#        auth.orderId = "60"
#        auth.amount = 15000
#        auth.orderSource = 'ecommerce'
#        
#        token = litleXmlFields.cardTokenType()
#        token.litleToken = "1712999999999999"
#        token.expDate = "1112"
#        auth.token = token
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(auth)
#        self.assertEquals("823", response.transactionResponse.response)
#        self.assertEquals("Token was invalid", response.transactionResponse.message)
#
#    def test61(self):
#        
#        sale = litleXmlFields.echeckSale()
#        sale.orderId = "61"
#        sale.amount = 15000
#        sale.orderSource = 'ecommerce'
#        
#        billtoaddress = litleXmlFields.contact()
#        billtoaddress.firstName = "Tom"
#        billtoaddress.lastName = "Black"
#        sale.billToAddress = billtoaddress
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accNum = "1099999003"
#        echeck.accType = 'Checking'
#        echeck.routingNum = "114567895"
#        sale.echeckOrEcheckToken = echeck
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(sale)
#        self.assertEquals("801", response.transactionResponse.tokenReponse.tokenResponseCode)
#        self.assertEquals("Account number was successfully registered", response.transactionResponse.tokenResponse.tokenMessage)
#        self.assertEquals('EC', response.transactionResponse.tokenResponse.type)
#        self.assertEquals("111922223333444999", response.transactionResponse.tokenResponse.litleToken)
#        
#        
#    def test62(self):
#        
#        sale = litleXmlFields.echeckSale()
#        sale.orderId = "62"
#        sale.amount = 15000
#        sale.orderSource = 'ecommerce'
#        
#        billtoaddress = litleXmlFields.contact()
#        billtoaddress.firstName = "Tom"
#        billtoaddress.lastName = "Black"
#        sale.billToAddress = billtoaddress
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accNum = "1099999999"
#        echeck.accType = 'Checking'
#        echeck.routingNum = "114567895"
#        sale.echeckOrEcheckToken = echeck
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(sale)
#        self.assertEquals("801", response.transactionResponse.tokenReponse.tokenResponseCode)
#        self.assertEquals("Account number was successfully registered", response.transactionResponse.tokenResponse.tokenMessage)
#        self.assertEquals('EC', response.transactionResponse.tokenResponse.type)
#        self.assertEquals("999", response.transactionResponse.tokenResponse.eCheckAccountSuffix)
#        self.assertEquals("111922223333444999", response.transactionResponse.tokenResponse.litleToken)
##        
#    def test63(self):
#        
#        sale = litleXmlFields.echeckSale()
#        sale.orderId = "63"
#        sale.amount = 15000
#        sale.orderSource = 'ecommerce'
#        
#        billtoaddress = litleXmlFields.contact()
#        billtoaddress.firstName = "Tom"
#        billtoaddress.lastName = "Black"
#        sale.billToAddress = billtoaddress
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accNum = "1099999999"
#        echeck.accType = 'Checking'
#        echeck.routingNum = "214567892"
#        sale.echeckOrEcheckToken = echeck
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(sale)
#        self.assertEquals("801", response.transactionResponse.tokenReponse.tokenResponseCode)
#        self.assertEquals("Account number was successfully registered", response.transactionResponse.tokenResponse.tokenMessage)
#        self.assertEquals('EC', response.transactionResponse.tokenResponse.type)
#        self.assertEquals("999", response.transactionResponse.tokenResponse.eCheckAccountSuffix)
#        self.assertEquals("111922223333555999", response.transactionResponse.tokenResponse.litleToken)


        