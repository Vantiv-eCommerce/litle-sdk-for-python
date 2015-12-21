#Copyright (c) 2011-2012 Litle & Co.
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.
import base64
import os, sys
from litleSdkPython import litleXmlFields
from litleSdkPython.litleXmlFields import advancedFraudChecksType
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest
from mock import *

class TestLitleOnline(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def testAuth(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
	authorization.id="id"
        
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
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
    
    def testAuthWithSecondaryAmountAndApplePayAndWallet(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.secondaryAmount = 10
	authorization.id="id"
        
        wallet=litleXmlFields.wallet()
        wallet.walletSourceType='MasterPass'
        wallet.walletSourceTypeId='12345'
        
        
        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "yoyo"
        applepay.version = '12345'
        header=litleXmlFields.applepayHeaderType()
        header.applicationData='applicationData'
        header.ephemeralPublicKey ='UWIRNRSKSXMXEYEINR'
        header.publicKeyHash='UYTGHJKMNBVFYWUWI'
        header.transactionId='1024'
        applepay.header=header
        authorization.applepay = applepay
        
        authorization.wallet=wallet

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(authorization)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<authorization.*?<applepay>.*?<data>4100000000000000</data>.*?</applepay>.*?<wallet.*?</wallet>.*?</authorization>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testAuthWithcustomAttributeOneToFive(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
	authorization.id="id"
        
        advancedFraudChecksType=litleXmlFields.advancedFraudChecksType()
        advancedFraudChecksType.customAttribute1='stringlength200'
        advancedFraudChecksType.customAttribute2='stringlength200'
        advancedFraudChecksType.customAttribute3='stringlength200'
        advancedFraudChecksType.customAttribute4='stringlength200'
        advancedFraudChecksType.customAttribute5='stringlength200'
        
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'
        authorization.card = card
        
        authorization.advancedFraudChecks=advancedFraudChecksType

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(authorization)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<authorization.*?<card>.*?<number>4100000000000000</number>.*?</card>.*?<advancedFraudChecks.*?<customAttribute4>stringlength200</customAttribute4>.*?</advancedFraudChecks></authorization>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testAuthReversal(self):
        authreversal = litleXmlFields.authReversal()
        authreversal.litleTxnId = 12345678000
        authreversal.amount = 106
        authreversal.payPalNotes = "Notes"
	authreversal.id="id"
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(authreversal)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<authReversal.*?<litleTxnId>12345678000</litleTxnId>.*?</authReversal>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testCapture(self):
        capture = litleXmlFields.capture()
        capture.litleTxnId = 123456000
        capture.amount = 106
        capture.payPalNotes = "Notes"
	capture.id="id"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(capture)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<capture.*?<litleTxnId>123456000</litleTxnId>.*?</capture>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testCaptureWithoutCustomBilling(self):
        capture = litleXmlFields.capture()
        capture.litleTxnId = 123456000
        capture.amount = 106
        capture.payPalNotes = "Notes"
	capture.id="id"
        
        customBilling=litleXmlFields.customBilling()
        customBilling.phone='6174445555'
        customBilling.descriptor='description'
        
        capture.customBilling=customBilling
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        with self.assertRaises(Exception):
            litle.sendRequest(authorization)

    def testCaptureGivenAuth(self):
        capturegivenauth = litleXmlFields.captureGivenAuth()
        capturegivenauth.amount = 106
        capturegivenauth.orderId = "12344"
	capturegivenauth.id="id"
        
        authinfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        authinfo.authDate = date
        authinfo.authCode = "543216"
        authinfo.authAmount = 12345
        capturegivenauth.authInformation = authinfo
        
        capturegivenauth.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        capturegivenauth.card = card
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(capturegivenauth)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<captureGivenAuth.*?<card>.*?<number>4100000000000001</number>.*?</card>.*?</captureGivenAuth>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
        
    def testCaptureGivenAuthWithSecondaryAmount(self):
        capturegivenauth = litleXmlFields.captureGivenAuth()
        capturegivenauth.amount = 106
        capturegivenauth.orderId = "12344"
        capturegivenauth.secondaryAmount=100
	capturegivenauth.id="id"
        
        authinfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        authinfo.authDate = date
        authinfo.authCode = "543216"
        authinfo.authAmount = 12345
        capturegivenauth.authInformation = authinfo
        
        capturegivenauth.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        capturegivenauth.card = card
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(capturegivenauth)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<captureGivenAuth.*?<secondaryAmount>100</secondaryAmount>.*?<card>.*?<number>4100000000000001</number>.*?</card>.*?</captureGivenAuth>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testCredit(self):
        credit = litleXmlFields.credit()
        credit.orderId = "12344"
        credit.orderSource = 'ecommerce'
	credit.id="id"
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(credit)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<credit.*?<card>.*?<number>4100000000000001</number>.*?</card>.*?</credit>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testCreditWithSecondaryAmountFirst(self):
        credit = litleXmlFields.credit()
        credit.orderId = "12344"
        credit.orderSource = 'ecommerce'
        credit.secondaryAmount=100
	credit.id="id"
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(credit)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<credit.*?<secondaryAmount>100</secondaryAmount>.*?<card>.*?<number>4100000000000001</number>.*?</card>.*?</credit>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testCreditWithSecondaryAmountSecond(self):
        credit = litleXmlFields.credit()
        credit.litleTxnId=1000
        credit.secondaryAmount=100
	credit.id="id"
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(credit)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<credit.*?<secondaryAmount>100</secondaryAmount>*?</credit>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testEcheckCredit(self):
        echeckcredit = litleXmlFields.echeckCredit()
        echeckcredit.amount = 12
        echeckcredit.litleTxnId = 123456789101112
	echeckcredit.id="id"
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckcredit)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckCredit.*?<litleTxnId>123456789101112</litleTxnId>.*?</echeckCredit>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testEcheckCreditWithSecondaryAmountFirst(self):
        echeckcredit = litleXmlFields.echeckCredit()
        echeckcredit.amount = 12
        echeckcredit.litleTxnId = 123456789101112
        echeckcredit.secondaryAmount=100
	echeckcredit.id="id"
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckcredit)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckCredit.*?<litleTxnId>123456789101112</litleTxnId>.*?<secondaryAmount>100</secondaryAmount>.*?</echeckCredit>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testEcheckCreditWithSecondaryAmountSecond(self):
        echeckcredit = litleXmlFields.echeckCredit()
        echeckcredit.amount = 12
        echeckcredit.orderId = '123456789101112'
        echeckcredit.secondaryAmount=100
	echeckcredit.id="id"
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckcredit)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckCredit.*?<secondaryAmount>100</secondaryAmount>.*?</echeckCredit>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testEcheckRedeposit(self):
        echeckredeposit = litleXmlFields.echeckRedeposit()
        echeckredeposit.litleTxnId = 123456
	echeckredeposit.id="id"
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckredeposit)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckRedeposit.*?<litleTxnId>123456</litleTxnId>.*?</echeckRedeposit>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testEcheckSale(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
	echecksale.id="id"        

        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "12345657890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echecksale.echeckOrEcheckToken = echeck
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echecksale)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckSale.*?<echeck>.*?<accNum>12345657890</accNum>.*?</echeck>.*?</echeckSale>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testEcheckSaleWithSecondaryAmountAndCCD(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        echecksale.secondaryAmount= 100
	echecksale.id="id" 
         
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "12345657890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echeck.ccdPaymentInformation = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
        echecksale.echeckOrEcheckToken = echeck
         
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
         
        comm = Communications(config)
        comm.http_post = MagicMock()
 
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echecksale)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckSale.*?<secondaryAmount>100</secondaryAmount>.*?<ccdPaymentInformation>12345678901234567890123456789012345678901234567890123456789012345678901234567890</ccdPaymentInformation>.*?</echeckSale>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
    
    def testEcheckSaleWithSecondaryAmountAndCCD(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        echecksale.secondaryAmount= 100
	echecksale.id="id" 
         
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "12345657890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echeck.ccdPaymentInformation = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
        echecksale.echeckOrEcheckToken = echeck
         
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
         
        comm = Communications(config)
        comm.http_post = MagicMock()
 
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echecksale)    
        
    def testEcheckSaleWithSecoundaryAmountAndCCDLongerThan80(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.secondaryAmount = 10
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
	echecksale.id="id" 
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum ="123455"
        with self.assertRaises(Exception):
            echeck.ccdPaymentInformation = "123456789012345678901234567890123456789012345678901234567890123456789012345678901"

    
    def testEcheckTxnsCanHavePpdAsOrderSource(self):
        echeckSale = litleXmlFields.echeckSale()
        echeckSale.orderSource = litleXmlFields.orderSourceType.echeckppd
	echeckSale.id="id" 
         
        comm = Communications(config)
        comm.http_post = MagicMock()
         
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckSale)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckSale.*?<orderSource>echeckppd</orderSource>.*?</echeckSale>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testEcheckVoid(self):
        echeckvoid = litleXmlFields.echeckVoid()
        echeckvoid.litleTxnId = 12345
	echeckvoid.id="id" 
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckvoid)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckVoid.*?<litleTxnId>12345</litleTxnId>.*?</echeckVoid>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testEcheckVerification(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123456
        echeckverification.orderId = "12345"
        echeckverification.orderSource = 'ecommerce'
	echeckverification.id="id" 
        
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
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckverification)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckVerification.*?<echeck>.*?<accNum>12345657890</accNum>.*?</echeck>.*?</echeckVerification>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testForceCapture(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106
        forcecapture.orderId = "12344"
        forcecapture.orderSource = 'ecommerce'
	forcecapture.id="id" 
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        forcecapture.card = card
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(forcecapture)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<forceCapture.*?<card>.*?<number>4100000000000001</number>.*?</card>.*?</forceCapture>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testForceCaptureWithSecondaryAmount(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106
        forcecapture.orderId = "12344"
        forcecapture.orderSource = 'ecommerce'
        forcecapture.secondaryAmount = 100
	forcecapture.id="id" 
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        forcecapture.card = card
         
        comm = Communications(config)
        comm.http_post = MagicMock()
 
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(forcecapture)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<forceCapture.*?<secondaryAmount>100</secondaryAmount>.*?<card>.*?<number>4100000000000001</number>.*?</card>.*?</forceCapture>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testSale(self):
        sale = litleXmlFields.sale()
        sale.amount = 106
        sale.litleTxnId = 123456
        sale.orderId = "12344"
        sale.orderSource = 'ecommerce'
	sale.id="id" 
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000002"
        card.expDate = "1210"
        sale.card = card
        
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(sale)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<sale.*?<card>.*?<number>4100000000000002</number>.*?</card>.*?</sale>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testSaleWithSecondaryAmountAndApplepayAndWallet(self):
        sale = litleXmlFields.sale()
        sale.amount = 106
        sale.litleTxnId = 123456
        sale.orderId = "12344"
        sale.orderSource = 'ecommerce'
        sale.secondaryAmount=100
	sale.id="id" 
    
        wallet=litleXmlFields.wallet()
        wallet.walletSourceType='MasterPass'
        wallet.walletSourceTypeId='12345'
        
        
        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "yoyo"
        applepay.version = '12345'
        header=litleXmlFields.applepayHeaderType()
        header.applicationData='applicationData'
        header.ephemeralPublicKey ='UWIRNRSKSXMXEYEINR'
        header.publicKeyHash='UYTGHJKMNBVFYWUWI'
        header.transactionId='1024'
        applepay.header=header
        sale.applepay = applepay
        
        sale.wallet=wallet

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(sale)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<sale.*?<applepay>.*?<data>4100000000000000</data>.*?</applepay>.*?<wallet.*?</wallet>.*?</sale>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
        
        
    def testToken(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = "12344"
        token.accountNumber = "1233456789103801"
	token.id="id"         

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(token)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<registerTokenRequest.*?<accountNumber>1233456789103801</accountNumber>.*?</registerTokenRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
    def testTokenWithApplepay(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = "12344"
	token.id="id"
        
        
        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "yoyo"
        applepay.version = '12345'
        header=litleXmlFields.applepayHeaderType()
        header.applicationData='applicationData'
        header.ephemeralPublicKey ='UWIRNRSKSXMXEYEINR'
        header.publicKeyHash='UYTGHJKMNBVFYWUWI'
        header.transactionId='1024'
        applepay.header=header
        token.applepay = applepay
         
        comm = Communications(config)
        comm.http_post = MagicMock()
 
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(token)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<registerTokenRequest.*?<applepay>.*?<data>4100000000000000</data>.*?</applepay>.*?</registerTokenRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testExtraField(self):
        auth = litleXmlFields.authorization()
        auth.orderId = '1234'
        auth.amount = 106
        auth.orderSource = 'ecommerce'
        auth.extraField = "extra"
	auth.id="id"
        
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'
        auth.card = card

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(auth)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<authorization.*?</orderSource><card>.*?<number>4100000000000000</number>.*?</card>.*?</authorization>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testExtraChoices(self):
        auth = litleXmlFields.authorization()
        auth.orderId = '1234'
        auth.amount = 106
        auth.orderSource = 'ecommerce'
	auth.id="id"
        
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'
        auth.card = card

        paypal = litleXmlFields.payPal()
        paypal.payerId = "1234"
        paypal.token = "1234"
        paypal.transactionId = '123456'
        auth.paypal = paypal

        litle = litleOnlineRequest(config)
        with self.assertRaises(Exception):
            litle.sendRequest(auth)

    def testInvalidEnum(self):
        auth = litleXmlFields.authorization()
        auth.orderId = '1234'
        auth.amount = 106
        auth.orderSource = 'ecommerce'
        auth.extraField = "extra"
	auth.id="id"
        
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        
        with self.assertRaises(pyxb.BadTypeValueError):
            card.type = 'VC'
            auth.card = card

    def testCustomerInfoDob(self):
        auth = litleXmlFields.authorization();
        auth.reportGroup = 'Planets'
        auth.orderId = '12344'
        auth.amount = 106
        auth.orderSource = 'ecommerce'
	auth.id="id"

        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = '4100000000000002'
        card.expDate = '1210'
        auth.card = card
        customerInfo = litleXmlFields.customerInfo()
        customerInfo.dob = '1980-04-14'
        auth.customerInfo = customerInfo

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(auth)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<authorization.*?<dob>1980-04-14</dob>.*?</authorization>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testCancelSubscription(self):
        cancel = litleXmlFields.cancelSubscription()
        cancel.subscriptionId = '12345'

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(cancel)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<cancelSubscription><subscriptionId>12345</subscriptionId></cancelSubscription></litleOnlineRequest>*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testUpdateSubscription(self):
        update = litleXmlFields.updateSubscription()
        update.billingDate = '2013-08-07'
        billToAddress = litleXmlFields.contact()
        billToAddress.name = 'Greg Dake'
        billToAddress.city = 'Lowell'
        billToAddress.state = 'MA'
        billToAddress.email = "sdksupport@litle.com"
        update.billToAddress = billToAddress
        card = litleXmlFields.cardType()
        card.number = '4100000000000001'
        card.expDate = '1215'
        card.type = 'VI'
        update.card = card
        update.planCode = 'abcdefg'
        update.subscriptionId = '12345'

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(update)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<updateSubscription><subscriptionId>12345</subscriptionId><planCode>abcdefg</planCode><billToAddress><name>Greg Dake</name><city>Lowell</city><state>MA</state><email>sdksupport@litle.com</email></billToAddress><card><type>VI</type><number>4100000000000001</number><expDate>1215</expDate></card><billingDate>2013-08-07</billingDate></updateSubscription></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testUpdatePlan(self):
        update = litleXmlFields.updatePlan()
        update.active = True
        update.planCode = 'abc'

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(update)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<updatePlan><planCode>abc</planCode><active>true</active></updatePlan></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testCreatePlan(self):
        create = litleXmlFields.createPlan()
        create.planCode = 'abc'
        create.active = True

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(create)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<createPlan><planCode>abc</planCode><active>true</active></createPlan></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testActivate(self):
        activate = litleXmlFields.activate()
        activate.amount = 100
	activate.id="id"


        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(activate)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<activate.*?<amount>100</amount></activate></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testDeactivate(self):
        deactivate = litleXmlFields.deactivate()
        deactivate.orderId = '123'
	deactivate.id="id"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(deactivate)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<deactivate.*?<orderId>123</orderId></deactivate></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testLoad(self):
        load = litleXmlFields.load()
        load.orderId = '123'
	load.id="id"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(load)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<load.*?<orderId>123</orderId></load></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testUnload(self):
        unload = litleXmlFields.unload()
        unload.orderId = '123'
	unload.id="id"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(unload)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<unload.*?<orderId>123</orderId></unload></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testBalanceInquiry(self):
        balanceInquiry = litleXmlFields.balanceInquiry()
        balanceInquiry.orderId = '123'
	balanceInquiry.id="id"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(balanceInquiry)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<balanceInquiry.*?<orderId>123</orderId></balanceInquiry></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testActivateReversal(self):
        activateReversal = litleXmlFields.activateReversal()
        activateReversal.litleTxnId = '123'
	activateReversal.id="id"


        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(activateReversal)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<activateReversal.*?<litleTxnId>123</litleTxnId></activateReversal></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testDeactivateReversal(self):
        deactivateReversal = litleXmlFields.deactivateReversal()
        deactivateReversal.litleTxnId = '123'
	deactivateReversal.id="id"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(deactivateReversal)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<deactivateReversal.*?<litleTxnId>123</litleTxnId></deactivateReversal></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testLoadReversal(self):
        loadReversal = litleXmlFields.loadReversal()
        loadReversal.litleTxnId = '123'
	loadReversal.id="id"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(loadReversal)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<loadReversal.*?<litleTxnId>123</litleTxnId></loadReversal></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testUnloadReversal(self):
        unloadReversal = litleXmlFields.unloadReversal()
        unloadReversal.litleTxnId = '123'
	unloadReversal.id="id"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(unloadReversal)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<unloadReversal.*?<litleTxnId>123</litleTxnId></unloadReversal></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testRefundReversal(self):
        refundReversal = litleXmlFields.refundReversal()
        refundReversal.litleTxnId = '123'
	refundReversal.id="id"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(refundReversal)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<refundReversal.*?<litleTxnId>123</litleTxnId></refundReversal></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def testDepositReversal(self):
        depositReversal = litleXmlFields.depositReversal()
        depositReversal.litleTxnId = '123'
	depositReversal.id="id"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(depositReversal)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<depositReversal.*?<litleTxnId>123</litleTxnId></depositReversal></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testfraudcheck(self):
        fraudCheck=litleXmlFields.fraudCheck()
        
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        
        fraudCheck.billToAddress=contact
        fraudCheck.shipToAddress=contact
        fraudCheck.amount=100
	fraudCheck.id="id"
        
        advancedFraudChecks=litleXmlFields.advancedFraudChecksType()
        advancedFraudChecks.customAttribute1='stringlength200'
        advancedFraudChecks.customAttribute2='stringlength200'
        advancedFraudChecks.customAttribute3='stringlength200'
        advancedFraudChecks.customAttribute4='stringlength200'
        advancedFraudChecks.customAttribute5='stringlength200'
        
        fraudCheck.advancedFraudChecks=advancedFraudChecks
        
        comm = Communications(config)
        comm.http_post = MagicMock()
        
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(fraudCheck)

        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<fraudCheck.*?</fraudCheck></litleOnlineRequest>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
        
    def testAuthenticationValueMaxlength(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.secondaryAmount = '10'
	authorization.id="id"
        
        
        fraudCheck=litleXmlFields.fraudCheckType()
        encoded = base64.b64encode('data to be encodedaaaaaaaaaabbbbbbbbbbcc') #generating a base64 encoded data of length 56, expect no exception
        self.assertEquals(56,len(encoded))
        fraudCheck.authenticationValue=encoded
        authorization.cardholderAuthentication=fraudCheck
        
        comm = Communications(config) #create an communication using config
        comm.http_post = MagicMock() #go deep into mock, some magic happened and http_post was set for com

        litle = litleOnlineRequest(config) #initial litleonlinerequest
        litle.setCommunications(comm) #use previous settled comm
        litle._processResponse = MagicMock(return_value=None) 
        litle.sendRequest(authorization) 

    def queryTransaction(self):
        queryTransaction = litleXmlFields.queryTransaction()
	queryTransaction.id = 'id'
        queryTransaction.origId = '1234'
        queryTransaction.origActionType = 'A'
        
        comm = Communications(config) #create an communication using config
        comm.http_post = MagicMock() #go deep into mock, some magic happened and http_post was set for com

        litle = litleOnlineRequest(config) #initial litleonlinerequest
        litle.setCommunications(comm) #use previous settled comm
        litle._processResponse = MagicMock(return_value=None) 
        litle.sendRequest(queryTransaction) 
	
  	comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?.*<origId>1234.*<origActionType>A.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)


        

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLitleOnline)
    return suite

if __name__ =='__main__':
    unittest.main()
