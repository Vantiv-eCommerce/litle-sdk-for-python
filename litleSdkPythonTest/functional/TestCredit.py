from litleSdkPythonTest.all.SetupTest import *
import unittest

class TestCredit(unittest.TestCase):
    
    def test_simpleCreditWithCard(self):
        credit = litleXmlFields.credit()
        credit.amount = 106
        credit.orderId = "12344"
        credit.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(credit)
        self.assertEquals("Approved", response.transactionResponse.message)

    def test_simpleCreditWithPaypal(self):
        credit = litleXmlFields.credit()
        credit.amount = 106
        credit.orderId = "123456"
        credit.orderSource = 'ecommerce'
        
        paypal = litleXmlFields.payPal()
        paypal.payerId = "1234"
        credit.paypal = paypal
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(credit)
        self.assertEquals("Approved", response.transactionResponse.message)

    def test_paypalNotes(self):
        credit = litleXmlFields.credit()
        credit.amount = 106
        credit.orderId = "12344"
        credit.payPalNotes = "Hello"
        credit.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(credit)
        self.assertEquals("Approved", response.transactionResponse.message)

    def test_processingInstructionandAmexData(self):
        credit = litleXmlFields.credit()
        credit.amount = 2000
        credit.orderId = "12344"
        credit.orderSource = 'ecommerce'
        
        pI = litleXmlFields.processingInstructions()
        pI.bypassVelocityCheck = True
        credit.processingInstructions = pI
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(credit)
            
        self.assertEquals("Approved", response.transactionResponse.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCredit)
    return suite