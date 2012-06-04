from SetupTest import *
import unittest

class TestToken(unittest.TestCase):
    
    def test_simpleToken(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        token.accountNumber = '1233456789103801'
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals(response.transactionResponse.message, "Account number was successfully registered")
        
    def test_simpleTokenWithPaypage(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        token.paypageRegistrationId = '1233456789101112'
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals(response.transactionResponse.message, "Account number was successfully registered")
        
    def test_simpleTokenWithEcheck(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        echeck = litleXmlFields.echeckForTokenType()
        echeck.accNum = "12344565"
        echeck.routingNum = "123476545"
        token.echeckForToken = echeck
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assertEquals(response.transactionResponse.message, "Account number was successfully registered")
        
    def test_tokenEcheckMissingRequiredField(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        echeck = litleXmlFields.echeckForTokenType()
        echeck.routingNum = "123476545"
        token.echeckForToken = echeck
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(token)
        self.assert_(response.message.count("Error validating xml data against the schema"))