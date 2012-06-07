from litleSdkPythonTest.all.SetupTest import *
import unittest
import pyxb

class TestCaptureGivenAuth(unittest.TestCase):
    
    def test_simple_captureGivenAuth(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 20)
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
        self.assertEquals("Approved",response.transactionResponse.message)
        
    def test_simple_captureGivenAuth_with_token(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        CaptureGivenAuth.authInformation = AuthInfo
        CaptureGivenAuth.orderSource = "ecommerce"
        Token = litleXmlFields.cardTokenType()
        Token.litleToken = "123456789101112"
        Token.expDate = "1210"
        Token.type = 'VI'
        Token.cardValidationNum = '555'
        CaptureGivenAuth.token = Token
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        self.assertEquals("Approved",response.transactionResponse.message)
        
    def test_complex_captureGivenAuth(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        CaptureGivenAuth.authInformation = AuthInfo
        Contact = litleXmlFields.contact();
        Contact.name="Bob"
        Contact.city="lowell"
        Contact.state="MA"
        Contact.email="litle.com"
        CaptureGivenAuth.billToAddress = Contact
        ProcessingInstruct = litleXmlFields.processingInstructions()
        ProcessingInstruct.bypassVelocityCheck = True
        CaptureGivenAuth.processingInstructions = ProcessingInstruct
        CaptureGivenAuth.orderSource = "ecommerce"
        Card = litleXmlFields.cardType()
        Card.number = "4100000000000000"
        Card.expDate = "1210"
        Card.type = 'VI'
        Card.cardValidationNum = '1210'
        CaptureGivenAuth.card = Card
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        self.assertEquals("Approved",response.transactionResponse.message)
        
        
    def test_authInfo(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        FraudResult = litleXmlFields.fraudResult()
        FraudResult.avsResult = "12"
        FraudResult.cardValidationResult = "123"
        FraudResult.authenticationResult = "1"
        FraudResult.advancedAvsResult = "123"
        AuthInfo.fraudResult = FraudResult
        CaptureGivenAuth.authInformation = AuthInfo
        CaptureGivenAuth.orderSource = "ecommerce"
        Card = litleXmlFields.cardType()
        Card.number = "4100000000000000"
        Card.expDate = "1210"
        Card.type = 'VI'
        Card.cardValidationNum = '555'
        CaptureGivenAuth.card = Card
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        self.assertEquals("Approved",response.transactionResponse.message)
   
def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCaptureGivenAuth)
    return suite