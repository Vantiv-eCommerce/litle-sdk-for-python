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

import os, sys
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest
from mock import *
from array import *

class TestPostGenerationScript(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_minOccurs_zero_on_orderId_orderSource_amount_billToAddress(self):
        authorization = litleXmlFields.authorization()        
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

    def test_minOccurs_zero_on_number_expDate(self):
        authorization = litleXmlFields.authorization()        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        authorization.card = card

        comm = Communications(config)
        comm.http_post = MagicMock()
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(authorization)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<authorization.*?<card>.*?.*?</card>.*?</authorization>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def test_minOccurs_postDate_message_response_responseTime(self):
      
        outputString = "<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><echeckRedepositResponse id='' reportGroup='Planets' customerId=''><litleTxnId>273132193500575000</litleTxnId></echeckRedepositResponse></litleOnlineResponse>"
        litleXml = litleOnlineRequest(config)
        xml_object = litleXml._processResponse(outputString)
        self.assertEqual(xml_object.litleTxnId, 273132193500575000)
        
    def test_minOccurs_accountInfo_tokenInfo_cardInfo_cardTokenInfo_code(self):
      
        outputString = "<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><echeckRedepositResponse id='' reportGroup='Planets' customerId=''><litleTxnId>273132193500575000</litleTxnId><accountUpdater><extendedCardResponse></extendedCardResponse></accountUpdater></echeckRedepositResponse></litleOnlineResponse>"
        litleXml = litleOnlineRequest(config)
        xml_object = litleXml._processResponse(outputString)
        self.assertEqual(xml_object.litleTxnId, 273132193500575000)
        
    def test_minOccurs_authInformation(self):
        capturegivenauth = litleXmlFields.captureGivenAuth()
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
        
    def test_minOccurs_authDate_authCode_capability_entryMode_cardHolderId_litleToken(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        AuthInfo.authAmount = 12345
        CaptureGivenAuth.authInformation = AuthInfo
        Pos = litleXmlFields.pos()
        CaptureGivenAuth.pos = Pos
        CaptureGivenAuth.orderSource = "ecommerce"
        Token = litleXmlFields.cardTokenType()
        Token.expDate = "1210"
        Token.type = 'VI'
        Token.cardValidationNum = '555'
        CaptureGivenAuth.token = Token
      
        comm = Communications(config)
        comm.http_post = MagicMock()
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(CaptureGivenAuth)
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<captureGivenAuth.*?<token>.*?</token>.*?</captureGivenAuth>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def test_minOccurs_echeckOrEcheckToken(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.orderId = "12345"
        echeckCredit.orderSource = 'ecommerce'
        
        comm = Communications(config)
        comm.http_post = MagicMock()
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckCredit)
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
    
    def test_minOccurs_routingNum_accType_accNum(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.orderId = "12345"
        echeckCredit.orderSource = 'ecommerce'
        echeck = litleXmlFields.echeck()
        echeckCredit.echeckOrEcheckToken = echeck
        
        comm = Communications(config)
        comm.http_post = MagicMock()
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckCredit)
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def test_minOccurs_taxAmount_itemDescription(self):
        Capture = litleXmlFields.capture()
        Capture.litleTxnId = 123456000
        Capture.amount = 106
        Capture.payPalNotes = "Notes"
        Enhanced = litleXmlFields.enhancedData()
        LineItem = litleXmlFields.lineItemData()
        LineItem.lineItemTotalWithTax = 123
        iterator = {LineItem : LineItem}
        Enhanced.lineItemData = iter(iterator)
        Capture.enhancedData = Enhanced
    
        comm = Communications(config)
        comm.http_post = MagicMock()
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(Capture)
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

    def test_minOccurs_payerId_transactionId_healthcareAmounts_IIASFlag_totalHealthCareAmount(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        amexData = litleXmlFields.amexAggregatorData()
        authorization.amexAggregatorData = amexData
        healthCare = litleXmlFields.healthcareIIAS()
        authorization.healthcareIIAS = healthCare
        healthCareAmt = litleXmlFields.healthcareAmounts()
        authorization.healthcareAmounts = healthCareAmt
        paypal = litleXmlFields.payPal()
        paypal.token = "1234"
        authorization.paypal = paypal
        
        comm = Communications(config)
        comm.http_post = MagicMock()
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(authorization)
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def test_minOccurs_tokenResponseCode_tokenMessage(self):
        outputString = "<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><authorizationResponse id='' reportGroup='DefaultReportGroup' customerId=''><litleTxnId>057484783403434000</litleTxnId><orderId>12344</orderId><response>000</response><responseTime>2012-06-05T16:36:39</responseTime><message>Approved</message><tokenResponse><litleToken>4242424242424242</litleToken><tokenResponseCode>111</tokenResponseCode><bin>bin</bin></tokenResponse></authorizationResponse></litleOnlineResponse>"
        litleXml = litleOnlineRequest(config)
        xml_object = litleXml._processResponse(outputString)
        self.assertEquals("bin", xml_object.tokenResponse.bin)
        
    def test_minOccurs_availableBalance(self):
        outputString = "<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><authorizationResponse id='' reportGroup='DefaultReportGroup' customerId=''><litleTxnId>057484783403434000</litleTxnId><orderId>12344</orderId><response>000</response><responseTime>2012-06-05T16:36:39</responseTime><message>Approved</message><enhancedAuthResponse></enhancedAuthResponse></authorizationResponse></litleOnlineResponse>"
        litleXml = litleOnlineRequest(config)
        xml_object = litleXml._processResponse(outputString)
        self.assertEquals("DefaultReportGroup", xml_object.reportGroup)
        
    def test_minOccurs_bmlMerhcantId(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        bml = litleXmlFields.billMeLaterRequest()
        authorization.billMeLatertRequest = bml

        comm = Communications(config)
        comm.http_post = MagicMock()
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(authorization)
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def test_minOccurs_paypageRegistrationId(self):
        sale = litleXmlFields.sale()
        sale.orderId = '12344'
        sale.amount = 106
        sale.orderSource = 'ecommerce'
        paypage = litleXmlFields.cardPaypageType()
        sale.paypage = paypage
        comm = Communications(config)
        comm.http_post = MagicMock()
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(sale)
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPostGenerationScript)
    return suite

if __name__ =='__main__':
    unittest.main()