from SetupTest import *
import unittest

class TestEcheckVerification(unittest.TestCase):
    
    def test_simpleEcheckVerification(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123456L
        echeckverification.orderId = '12345'
        echeckverification.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        echeckverification.echeckOrEcheckToken = echeck
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echeckverification.billToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckverification)
        self.assertEquals(response.message, "Valid Format")
        self.assertEquals("Approved",response.transactionResponse.message)

    
    def test_echeckVerificationWithEcheckToken(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123456L
        echeckverification.orderId = '12345'
        echeckverification.orderSource = 'ecommerce'
        
        token = litleXmlFields.echeckToken()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum = "123456789"
        token.checkNum = "123455"
        echeckverification.echeckOrEcheckToken = token
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echeckverification.billToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckverification)
        self.assertEquals(response.message, "Valid Format")
        self.assertEquals("Approved",response.transactionResponse.message)

        
    def test_MissingBillingField(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123L
        echeckverification.orderId = '12345'
        echeckverification.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        echeckverification.echeckOrEcheckToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckverification)
        self.assert_(response.message.count("Error validating xml data against the schema"))