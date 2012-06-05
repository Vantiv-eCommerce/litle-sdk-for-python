from SetupTest import *
import unittest

class TestForceCapture(unittest.TestCase):
    
    def test_simpleForceCaptureWithCard(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106L
        forcecapture.orderId = '12344'
        forcecapture.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        forcecapture.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(forcecapture)
        self.assertEquals(response.message, "Valid Format")
        self.assertEquals("Approved",response.transactionResponse.message)

        
    def test_simpleForceCaptureWithToken(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106L
        forcecapture.orderId = '12344'
        forcecapture.orderSource = 'ecommerce'
        
        token = litleXmlFields.cardTokenType()
        token.type = 'VI'
        token.expDate = "1210"
        token.litleToken = "123456789101112"
        token.cardValidationNum = "555"
        forcecapture.token = token
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(forcecapture)
        self.assertEquals(response.message, "Valid Format")
        self.assertEquals("Approved",response.transactionResponse.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestForceCapture)
    return suite