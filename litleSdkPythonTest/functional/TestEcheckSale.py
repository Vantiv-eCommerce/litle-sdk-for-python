from litleSdkPythonTest.all.SetupTest import *
import unittest

class TestEcheckSale(unittest.TestCase):
    
    def test_simpleEcheckSaleWithEcheck(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum ="123455"
        echecksale.echeckOrEcheckToken = echeck
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assertEquals("Approved",response.transactionResponse.message)

    def test_noAmount(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assert_(response.message.count("Error validating xml data against the schema"))

    def test_echeckSaleWithShipTo(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.amount = 123456
        echecksale.verify = True
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum ="123455"
        echecksale.echeckOrEcheckToken = echeck
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
        echecksale.shipToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assertEquals("Approved",response.transactionResponse.message)
      
    def test_echeckSaleWithEcheckToken(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.amount = 123456
        echecksale.verify = True
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        
        token = litleXmlFields.echeckToken()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum = "123456789"
        token.checkNum ="123455"
        echecksale.echeckOrEcheckToken = token
        
        custombilling = litleXmlFields.customBilling()
        custombilling.phone = "123456789"
        custombilling.descriptor = "good"
        echecksale.customBilling = custombilling
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assertEquals("Approved",response.transactionResponse.message)

    def test_echeckSaleMissingBilling(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.amount = 123456
        
        token = litleXmlFields.echeckTokenType()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum = "123456789"
        token.checkNum ="123455"
        echecksale.echeckToken = token
        
        echecksale.verify = True
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assert_(response.message.count("Error validating xml data against the schema"))

    def test_simpleEcheckSale(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.litleTxnId = 123456789101112
        echecksale.amount = 12
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assertEquals("Approved",response.transactionResponse.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEcheckSale)
    return suite