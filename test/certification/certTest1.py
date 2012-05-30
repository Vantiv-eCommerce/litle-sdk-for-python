from SetupTest import *
import unittest

class TestAuth(unittest.TestCase):
    
    def test_auth(self):
        
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
        response = litleXml.litleXmlMapper(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("11111 ",response.transactionResponse.authCode)
        self.assertEquals( "01",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M",response.transactionResponse.fraudResult.cardValidationResult);
        
if __name__ == '__main__':
    unittest.main()        