from SetupTest import *
import unittest

class TestAuth(unittest.TestCase):
    
    def test_simple_auth_with_card(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
    
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'
    
        authorization.card = card
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
            
        self.assertEquals("000",response.transactionResponse.response)


    def test_simple_auth_with_paypal(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
    
        paypal = litleXmlFields.payPal()
        paypal.payerId = "1234"
        paypal.token = "1234"
        paypal.transactionId = '123456'
        
    
        authorization.paypal = paypal
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
            
        self.assertEquals("Approved",response.transactionResponse.message)
       

    def test_pos_without_capability_and_entryMode(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '123456'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
    
        pos = litleXmlFields.pos()
        pos.cardholderId = "pin"
        authorization.pos = pos
            
        card = litleXmlFields.cardType()
        card.number = "4100000000000002"
        card.expDate = "1210"
        card.type = 'VI'
        card.cardValidationNum = '1213'
    
        authorization.card = card
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
            
        self.assert_(response.message.count("Error validating xml data against the schema"))

    def test_accountUpdate(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
    
        card = litleXmlFields.cardType()
        card.number = "4100100000000000"
        card.expDate = "1210"
        card.type = 'VI'
        card.cardValidationNum = '1213'
    
        authorization.card = card
    
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
            
        self.assertEquals("4100100000000000",response.transactionResponse.accountUpdater.originalCardInfo.number)
    

