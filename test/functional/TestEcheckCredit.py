from test.all.SetupTest import *
import unittest

class TestEcheckCredit(unittest.TestCase):
    
    def test_simpleEcheckCredit(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.litleTxnId = 123456789101112
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckCredit)
        self.assertEquals("Approved", response.transactionResponse.message)

    def test_noLitleTxnId(self):
        echeckCredit = litleXmlFields.echeckCredit()

        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckCredit)
        self.assert_(response.message.count("Error validating xml data against the schema"))

    def test_echeckCreditWithEcheck(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.orderId = "12345"
        echeckCredit.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum ="123456789"
        echeck.checkNum = "123455"
        echeckCredit.echeckOrEcheckToken = echeck
        
        billToAddress = litleXmlFields.contact()
        billToAddress.name = "Bob"
        billToAddress.City ="Lowell"
        billToAddress.State = "MA"
        billToAddress.email = "litle.com"
        echeckCredit.billToAddress = billToAddress
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckCredit)
        self.assertEquals("Approved", response.transactionResponse.message)

    def test_echeckCreditWithToken(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.orderId = "12345"
        echeckCredit.orderSource = 'ecommerce'
        
        token = litleXmlFields.echeckToken()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum ="123456789"
        token.checkNum = "123455"
        echeckCredit.echeckOrEcheckToken = token
        
        billToAddress = litleXmlFields.contact()
        billToAddress.name = "Bob"
        billToAddress.City ="Lowell"
        billToAddress.State = "MA"
        billToAddress.email = "litle.com"
        echeckCredit.billToAddress = billToAddress
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckCredit)
        self.assertEquals("Approved", response.transactionResponse.message)

    def test_missingBilling(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.orderId = "12345"
        echeckCredit.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum ="123456789"
        echeck.checkNum = "123455"
        echeckCredit.echeckOrEcheckToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckCredit)
        self.assert_(response.message.count("Error validating xml data against the schema"))

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEcheckCredit)
    return suite