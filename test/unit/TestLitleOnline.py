from SetupTest import *
import unittest
from mock import *

class TestLitleOnline(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_auth(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'
        authorization.card = card

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(authorization)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<authorization.*?<card>.*?<number>4100000000000000</number>.*?</card>.*?</authorization>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)


#    def test_authwithoverrides(self):
#        auth = litleXmlFields.authorization()
#        auth.reportGroup = "Planets"
#        auth.orderId = "12344"
#        auth.amount = 106
#        auth.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000002"
#        card.expDate = "1210"
#        auth.card = card
#        
#        # create mock communication
#        # set the communication to the mocked communication
#        # create an override online request
#            # set the merchant ID to "9001"
#        # get an auth response from sending auth and override
#        litleXml =  litleOnlineRequest(config)
#        
#        authResponse = litleXml.sendRequest(auth, override)
#        assertEquals(123, authResponse.litleTxnId)
#
#    def test_authreversal(self):
#        authreversal = litleXmlFields.authReversal()
#        authreversal.litleTxnId = 12345678000
#        authreversal.amount = 106
#        authreversal.payPalNotes = "Notes"
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an authreversal response from sending auth and override
#        litleXml =  litleOnlineRequest(config)
#        
#        authReversalResponse = litleXml.sendRequest(authreversal)
#        assertEquals(123, authReversalResponse.litleTxnId)
#
#    def test_authreversalwithoverrides(self):
#        authreversal = litleXmlFields.authReversal()
#        authreversal.litleTxnId = 12345678000
#        authreversal.amount = 106
#        authreversal.payPalNotes = "Notes"
#        
#        # create mock communication
#        # set the communication to the mocked communication
#        # create an override online request
#            # set the version to "8.11"
#        # get an authreversal response from sending auth and override
#        litleXml =  litleOnlineRequest(config)
#        
#        authReversalResponse = litleXml.sendRequest(authreversal, override)
#        assertEquals(123, authReversalResponse.litleTxnId)
#
#    def test_capture(self):
#        capture = litleXmlFields.capture()
#        capture.litleTxnId = 123456000
#        capture.amount = 106
#        capture.payPalNotes = "Notes"
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an capture response from sending capture
#        litleXml =  litleOnlineRequest(config)
#        
#        captureResponse = litleXml.sendRequest(capture)
#        assertEquals(123, captureResponse.litleTxnId)
#
#    def test_capturewithoverrides(self):
#        capture = litleXmlFields.capture()
#        capture.litleTxnId = 123456000
#        capture.amount = 106
#        capture.payPalNotes = "Notes"
#        
#        # create mock communication
#        # set the communication to the mocked communication
#        # create an override online request
#            # set the authentication password to "supersecret"
#        # get an capture response from sending capture and override
#        litleXml =  litleOnlineRequest(config)
#        
#        captureResponse = litleXml.sendRequest(capture, override)
#        assertEquals(123, captureResponse.litleTxnId)
#
#    def test_capturegivenauth(self):
#        capturegivenauth = litleXmlFields.captureGivenAuth()
#        capturegivenauth.amount = 106
#        capturegivenauth.orderId = "12344"
#        
#        authinfo = litleXmlFields.authInformation()
#        # create an authdate by creating an instance of a calender
#            # set the auth date to 2002, October 9
#        authinfo.authDate = authdate
#        authinfo.authCode = "543216"
#        authinfo.authAmount =12345
#        capturegivenauth.authInformation = authinfo
#        
#        capturegivenauth.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000001"
#        card.expDate = "1210"
#        capturegivenauth.card = card
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an capture given auth response from sending capturegivenauth
#        litleXml =  litleOnlineRequest(config)
#        
#        capturegivenauthResponse = litleXml.sendRequest(capturegivenauth)
#        assertEquals(123, capturegivenauthResponse.litleTxnId)
#
#    def test_capturegivenauthwithoverrides(self):
#        capturegivenauth = litleXmlFields.captureGivenAuth()
#        capturegivenauth.amount = 106
#        capturegivenauth.orderId = "12344"
#        
#        authinfo = litleXmlFields.authInformation()
#        # create an authdate by creating an instance of a calender
#            # set the auth date to 2002, October 9
#        authinfo.authDate = authdate
#        authinfo.authCode = "543216"
#        authinfo.authAmount =12345
#        capturegivenauth.authInformation = authinfo
#        
#        capturegivenauth.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000001"
#        card.expDate = "1210"
#        capturegivenauth.card = card
#        
#        # create mock communication
#        # set the communication to the mocked communication
#        # create an override online request
#            # set the authentication user to "neweruser"
#        # get an capture given auth response from sending capturegivenauth
#        litleXml =  litleOnlineRequest(config)
#        
#        capturegivenauthResponse = litleXml.sendRequest(capturegivenauth)
#        assertEquals(123, capturegivenauthResponse.litleTxnId)
#
#    def test_credit(self):
#        credit = litleXmlFields.credit()
#        credit.orderId = "12344"
#        credit.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000001"
#        card.expDate = "1210"
#        credit.card = card
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an credit response from sending credit
#        litleXml =  litleOnlineRequest(config)
#        
#        creditResponse = litleXml.sendRequest(credit)
#        assertEquals(123, creditResponse.litleTxnId)
#
#    def test_echeckcredit(self):
#        echeckcredit = litleXmlFields.echeckCredit()
#        echeckcredit.amount = 12
#        echeckcredit.litleTxnId = 123456789101112
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an echeck credit response from sending echeckcredit
#        litleXml =  litleOnlineRequest(config)
#        
#        echeckcreditResponse = litleXml.sendRequest(echeckcredit)
#        assertEquals(123, echeckcreditResponse.litleTxnId)
#
#    def test_echeckredeposit(self):
#        echeckredeposit = litleXmlFields.echeckRedeposit()
#        echeckredeposit.litleTxnId = 123456
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an echeck redeposit  response from sending echeckredeposit
#        litleXml =  litleOnlineRequest(config)
#        
#        echeckredepositResponse = litleXml.sendRequest(echeckredeposit)
#        assertEquals(123, echeckredepositResponse.litleTxnId)
#
#    def test_echecksale(self):
#        echecksale = litleXmlFields.echeckSale()
#        echecksale.amount = 123456
#        echecksale.orderId = "12345"
#        echecksale.orderSource = 'ecommerce'
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accType = 'Checking'
#        echeck.accNum = "1234567890"
#        echeck.routingNum = "123456789"
#        echeck.checkNum = "123455"
#        echecksale.echeck = echeck
#        
#        contact = litleXmlFields.conact()
#        contact.name = "Bob"
#        contact.city = "lowell"
#        contact.state = "MA"
#        contact.email = "litle.com"
#        echecksale.billToAddress = contact
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an echeck sale  response from sending echecksale
#        litleXml =  litleOnlineRequest(config)
#        
#        echecksaleResponse = litleXml.sendRequest(echecksale)
#        assertEquals(123, echecksaleResponse.litleTxnId)
#
#    def test_echeckverification(self):
#        echeckverification = litleXmlFields.echeckVerification()
#        echeckverification.amount = 123456
#        echeckverification.orderId = "12345"
#        echeckverification.orderSource = 'ecommerce'
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accType = 'Checking'
#        echeck.accNum = "1234567890"
#        echeck.routingNum = "123456789"
#        echeck.checkNum = "123455"
#        echeckverification.echeck = echeck
#        
#        contact = litleXmlFields.contact()
#        contact.name = "Bob"
#        contact.city = "lowell"
#        contact.state = "MA"
#        contact.email = "litle.com"
#        echeckverification.billToAddress = contact
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an echeck verification  response from sending echeckverification
#        litleXml =  litleOnlineRequest(config)
#        
#        echeckverificationResponse = litleXml.sendRequest(echeckverification)
#        assertEquals(123, echeckverificationResponse.litleTxnId)
#
#    def test_forcecapture(self):
#        forcecapture = litleXmlFields.forceCapture()
#        forcecapture.amount = 106
#        forcecapture.orderId = "12344"
#        forcecapture.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000001"
#        card.expDate = "1210"
#        forcecapture.card = card
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an force capture  response from sending forcecapture
#        litleXml =  litleOnlineRequest(config)
#        
#        forcecaptureResponse = litleXml.sendRequest(forcecapture)
#        assertEquals(123, forcecaptureResponse.litleTxnId)
#
#    def test_sale(self):
#        sale = litleXmlFields.sale()
#        sale.amount = 106
#        sale.litleTxnId = 123456
#        sale.orderId = "12344"
#        sale.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000002"
#        card.expDate = "1210"
#        sale.card = card
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an sale  response from sending sale
#        litleXml =  litleOnlineRequest(config)
#        
#        saleResponse = litleXml.sendRequest(sale)
#        assertEquals(123, saleResponse.litleTxnId)
#
#    def test_token(self):
#        token = litleXmlFields.registerTokenRequestType()
#        token.orderId = "12344"
#        token.accountNumber = "123456789103801"
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an token  response from sending token
#        litleXml =  litleOnlineRequest(config)
#        
#        tokenResponse = litleXml.sendRequest(token)
#        assertEquals(123, tokenResponse.litleTxnId)
#
#    def test_litleonlineexception(self):
#        auth = litleXmlFields.authorization()
#        auth.reportGroup = "Planets"
#        auth.orderId = "12344"
#        auth.amount = 106
#        auth.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000002"
#        card.expDate = "1210"
#        auth.card = card
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # try to get an auth  response from sending auth
#        # it will return a schema validation error
#        litleXml =  litleOnlineRequest(config)
#        
#        authResponse = litleXml.sendRequest(auth)
#        self.assert_(authResponse.message.count("Error validating xml data against the schema"))
#
#    def test_pyxbexception(self):
#        auth = litleXmlFields.authorization()
#        auth.reportGroup = "Planets"
#        auth.orderId = "12344"
#        auth.amount = 106
#        auth.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000002"
#        card.expDate = "1210"
#        auth.card = card
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # try to get an auth  response from sending auth
#        # it will return a schema validation error
#        litleXml =  litleOnlineRequest(config)
#        
#        authResponse = litleXml.sendRequest(auth)
#        self.assert_(authResponse.message.count("Error validating xml data against the schema"))
#
#    def test_defaultreportgroup(self):
#        auth = litleXmlFields.authorization()
#        auth.orderId = "12344"
#        auth.amount = 106
#        auth.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000002"
#        card.expDate = "1210"
#        auth.card = card
#        
#        # create mock communication
#        # set the communication to the mocked communication
#        
#        # get an auth  response from sending auth
#        litleXml =  litleOnlineRequest(config)
#        
#        authResponse = litleXml.sendRequest(auth)
#        assertEquals("Default Report Group", authResponse.transactionResponse.reportGroup)
#
#    def test_echeckvoid(self):
#        echeckvoid = litleXmlFields.echeckVoid()
#        echeckvoid.litleTxnId = 12345
#        
#        # create mock communication
#        # set the communication to the mocked communication
#
#        # get an echeck void  response from sending echeckvoid
#        litleXml =  litleOnlineRequest(config)
#        
#        echeckvoidResponse = litleXml.sendRequest(echeckvoid)
#        assertEquals(123, tokenResponse.litleTxnId)
