from SetupTest import *
import unittest

class TestCaptureGivenAuth(unittest.TestCase):
    
    def test_simple_captureGivenAuth(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date('20021009')
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        CaptureGivenAuth.authInformation = AuthInfo
        
        CaptureGivenAuth.orderSource = "ecommerce"
        Card = litleXmlFields.cardType()
        Card.number = "4100000000000000"
        Card.expDate = "1210"
        Card.type = 'VI'
        Card.cardValidationNum = '1210'
    
        CaptureGivenAuth.card = Card
    
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(CaptureGivenAuth)
            
        self.assertEquals("Approved",response.message)
        