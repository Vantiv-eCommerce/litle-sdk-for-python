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
import base64
from litleSdkPython import litleXmlFields
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
        #Jan 31,2015 checked secondaryAmount
        
        
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type='VI'
        
        authorization.card = card
        
        comm = Communications(config) #create an communication using config
        comm.http_post = MagicMock() #go deep into mock, some magic happened and http_post was set for com

        litle = litleOnlineRequest(config) #initial litleonlinerequest
        litle.setCommunications(comm) #use previous settled comm
        litle._processResponse = MagicMock(return_value=None) 
        litle.sendRequest(authorization) #trick happend here, in inner self.communications.http_post method sent the request xml to mock
        
        expected = RegexMatcher("[\s\S]*?<litleOnlineRequest[\s\S]*?<authorization[\s\S]*?<card>[\s\S]*?<number>4100000000000000</number>[\s\S]*?</card>[\s\S]*?</authorization>[\s\S]*?")
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
    
    #new features for 8.29
    def testAuthWithSecondaryAmountAndApplepay(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.secondaryAmount = '10'
        
        
        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "yoyo"
        applepay.version = '8.29'
        header=litleXmlFields.applepayHeaderType()
        header.applicationData='applicationData'
        header.ephemeralPublicKey ='UWIRNRSKSXMXEYEINR'
        header.publicKeyHash='UYTGHJKMNBVFYWUWI'
        header.transactionId='1024'
        applepay.header=header
        authorization.applepay = applepay
        
        comm = Communications(config) #create an communication using config
        comm.http_post = MagicMock() #go deep into mock, some magic happened and http_post was set for com

        litle = litleOnlineRequest(config) #initial litleonlinerequest
        litle.setCommunications(comm) #use previous settled comm
        litle._processResponse = MagicMock(return_value=None) 
        litle.sendRequest(authorization) #trick happend here, in inner self.communications.http_post method sent the request xml to mock
        
        expected=RegexMatcher("[\s\S]*?<litleOnlineRequest[\s\S]*?<authorization[\s\S]*?<secondaryAmount>10</secondaryAmount>[\s\S]*?<applepay>[\s\S]*?<header>[\s\S]*?<applicationData>applicationData</applicationData>[\s\S]*?</header>[\s\S]*?</applepay>[\s\S]*?</authorization>[\s\S]*?")
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
    
    #new for 8.29
    def testAuthenticationValueMaxlength(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.secondaryAmount = '10'
        
        
        fraudCheck=litleXmlFields.fraudCheckType()
        encoded = base64.b64encode('data to be encodedaaaaaaaaaabbbbbbbbbbcc') #generating a base64 encoded data of length 56, expect no exception
        print len(encoded)
        fraudCheck.authenticationValue=encoded
        authorization.cardholderAuthentication=fraudCheck
        
        comm = Communications(config) #create an communication using config
        comm.http_post = MagicMock() #go deep into mock, some magic happened and http_post was set for com

        litle = litleOnlineRequest(config) #initial litleonlinerequest
        litle.setCommunications(comm) #use previous settled comm
        litle._processResponse = MagicMock(return_value=None) 
        litle.sendRequest(authorization) #trick happend here, in inner self.communications.http_post method sent the request xml to mock
        
        #expected=RegexMatcher("[\s\S]*?<litleOnlineRequest[\s\S]*?<authorization[\s\S]*?<secondaryAmount>10</secondaryAmount>[\s\S]*?<applepay>[\s\S]*?<header>[\s\S]*?<applicationData>applicationData</applicationData>[\s\S]*?</header>[\s\S]*?</applepay>[\s\S]*?</authorization>[\s\S]*?")
        #comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
    #new for 8.29
    def testOrderSourceTypeWithApplePay(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'applepay'
         
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type='VI'
        
        authorization.card = card
        
        comm = Communications(config) #create an communication using config
        comm.http_post = MagicMock() #go deep into mock, some magic happened and http_post was set for com

        litle = litleOnlineRequest(config) #initial litleonlinerequest
        litle.setCommunications(comm) #use previous settled comm
        litle._processResponse = MagicMock(return_value=None) 
        litle.sendRequest(authorization) #trick happend here, in inner self.communications.http_post method sent the request xml to mock
        
        expected = RegexMatcher("[\s\S]*?<litleOnlineRequest[\s\S]*?<authorization[\s\S]*?<orderSource>applepay</orderSource>[\s\S]*?<card>[\s\S]*?<number>4100000000000000</number>[\s\S]*?</card>[\s\S]*?</authorization>[\s\S]*?")
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
    def testAuthReversal(self):
        authreversal = litleXmlFields.authReversal()
        authreversal.litleTxnId = 12345678000
        authreversal.amount = 106
        authreversal.payPalNotes = "Notes"
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(authreversal)
        
        comm.http_post.assert_called_once()
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <authReversal reportGroup="DefaultReportGroup">
    <litleTxnId>12345678000</litleTxnId>
    <amount>106</amount>
    <payPalNotes>Notes</payPalNotes>
  </authReversal>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)

    def testCapture(self):
        capture = litleXmlFields.capture()
        capture.litleTxnId = 123456000
        capture.amount = 106
        capture.payPalNotes = "Notes"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(capture)
        
        comm.http_post.assert_called_once()
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <capture reportGroup="DefaultReportGroup">
    <litleTxnId>123456000</litleTxnId>
    <amount>106</amount>
    <payPalNotes>Notes</payPalNotes>
  </capture>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)

    def testCaptureGivenAuth(self):
        capturegivenauth = litleXmlFields.captureGivenAuth()
        capturegivenauth.amount = 106
        capturegivenauth.orderId = "12344"
        
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
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <captureGivenAuth reportGroup="DefaultReportGroup">
    <orderId>12344</orderId>
    <authInformation>
      <authDate>2002-10-09</authDate>
      <authCode>543216</authCode>
      <authAmount>12345</authAmount>
    </authInformation>
    <amount>106</amount>
    <orderSource>ecommerce</orderSource>
    <card>
      <type>VI</type>
      <number>4100000000000001</number>
      <expDate>1210</expDate>
    </card>
  </captureGivenAuth>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
    
    #new for 8.29    
    def testCaptureGivenAuthWithSecondaryAmount(self):
        capturegivenauth = litleXmlFields.captureGivenAuth()
        capturegivenauth.amount = 106
        capturegivenauth.orderId = "12344"
        capturegivenauth.secondaryAmount=100
        
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
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <captureGivenAuth reportGroup="DefaultReportGroup">
    <orderId>12344</orderId>
    <authInformation>
      <authDate>2002-10-09</authDate>
      <authCode>543216</authCode>
      <authAmount>12345</authAmount>
    </authInformation>
    <amount>106</amount>
    <secondaryAmount>100</secondaryAmount>
    <orderSource>ecommerce</orderSource>
    <card>
      <type>VI</type>
      <number>4100000000000001</number>
      <expDate>1210</expDate>
    </card>
  </captureGivenAuth>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
        
        
    def testCredit(self):
        credit = litleXmlFields.credit()
        credit.orderId = "12344"
        credit.orderSource = 'ecommerce'
        
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
        reponse=litle.sendRequest(credit)
        
        comm.http_post.assert_called_once()
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <credit reportGroup="DefaultReportGroup">
    <orderId>12344</orderId>
    <orderSource>ecommerce</orderSource>
    <card>
      <type>VI</type>
      <number>4100000000000001</number>
      <expDate>1210</expDate>
    </card>
  </credit>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
    
    #new for 8.29
    def testCreditWithSecondaryAmount(self):
        credit = litleXmlFields.credit()
        credit.orderId = "12344"
        credit.orderSource = 'ecommerce'
        credit.secondaryAmount =100
        
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
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <credit reportGroup="DefaultReportGroup">
    <orderId>12344</orderId>
    <secondaryAmount>100</secondaryAmount>
    <orderSource>ecommerce</orderSource>
    <card>
      <type>VI</type>
      <number>4100000000000001</number>
      <expDate>1210</expDate>
    </card>
  </credit>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
    
    def testEcheckCredit(self):
        echeckcredit = litleXmlFields.echeckCredit()
        echeckcredit.amount = 12
        echeckcredit.litleTxnId = 123456789101112
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckcredit)
        
        comm.http_post.assert_called_once()
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <echeckCredit reportGroup="DefaultReportGroup">
    <litleTxnId>123456789101112</litleTxnId>
    <amount>12</amount>
  </echeckCredit>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
    
    #new for 8.29
    def testEcheckCreditWithSecondaryAmount(self):
        echeckcredit = litleXmlFields.echeckCredit()
        echeckcredit.orderId = "12344"
        echeckcredit.secondaryAmount =100
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckcredit)
        
        comm.http_post.assert_called_once()
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <echeckCredit reportGroup="DefaultReportGroup">
    <orderId>12344</orderId>
    <secondaryAmount>100</secondaryAmount>
  </echeckCredit>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testEcheckRedeposit(self):
#         echeckredeposit = litleXmlFields.echeckRedeposit()
#         echeckredeposit.litleTxnId = 123456
#         
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(echeckredeposit)
#         
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <echeckRedeposit reportGroup="DefaultReportGroup">
#     <litleTxnId>123456</litleTxnId>
#   </echeckRedeposit>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)

    def testEcheckSale(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
         
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
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <echeckSale reportGroup="DefaultReportGroup">
    <orderId>12345</orderId>
    <amount>123456</amount>
    <orderSource>ecommerce</orderSource>
    <billToAddress>
      <name>Bob</name>
      <city>lowell</city>
      <state>MA</state>
      <email>litle.com</email>
    </billToAddress>
    <echeck>
      <accType>Checking</accType>
      <accNum>12345657890</accNum>
      <routingNum>123456789</routingNum>
      <checkNum>123455</checkNum>
    </echeck>
  </echeckSale>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)

    #new for 8.29
    def testEcheckSaleWithSecondaryAmount(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        echecksale.secondaryAmount= 100
         
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
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <echeckSale reportGroup="DefaultReportGroup">
    <orderId>12345</orderId>
    <amount>123456</amount>
    <secondaryAmount>100</secondaryAmount>
    <orderSource>ecommerce</orderSource>
    <billToAddress>
      <name>Bob</name>
      <city>lowell</city>
      <state>MA</state>
      <email>litle.com</email>
    </billToAddress>
    <echeck>
      <accType>Checking</accType>
      <accNum>12345657890</accNum>
      <routingNum>123456789</routingNum>
      <checkNum>123455</checkNum>
    </echeck>
  </echeckSale>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
#     def testEcheckVoid(self):
#         echeckvoid = litleXmlFields.echeckVoid()
#         echeckvoid.litleTxnId = 12345
#         
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(echeckvoid)
#         
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <echeckVoid reportGroup="DefaultReportGroup">
#     <litleTxnId>12345</litleTxnId>
#   </echeckVoid>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testEcheckVerification(self):
#         echeckverification = litleXmlFields.echeckVerification()
#         echeckverification.amount = 123456
#         echeckverification.orderId = "12345"
#         echeckverification.orderSource = 'ecommerce'
#         
#         echeck = litleXmlFields.echeck()
#         echeck.accType = 'Checking'
#         echeck.accNum = '12345657890'
#         echeck.routingNum = '123456789'
#         echeck.checkNum = '123455'
#         echeckverification.echeckOrEcheckToken = echeck
#         
#         contact = litleXmlFields.contact()
#         contact.name = "Bob"
#         contact.city = "lowell"
#         contact.state = "MA"
#         contact.email = "litle.com"
#         echeckverification.billToAddress = contact
#         
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(echeckverification)
#         
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <echeckVerification reportGroup="DefaultReportGroup">
#     <orderId>12345</orderId>
#     <amount>123456</amount>
#     <orderSource>ecommerce</orderSource>
#     <billToAddress>
#       <name>Bob</name>
#       <city>lowell</city>
#       <state>MA</state>
#       <email>litle.com</email>
#     </billToAddress>
#     <echeck>
#       <accType>Checking</accType>
#       <accNum>12345657890</accNum>
#       <routingNum>123456789</routingNum>
#       <checkNum>123455</checkNum>
#     </echeck>
#   </echeckVerification>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
    def testForceCapture(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106
        forcecapture.orderId = "12344"
        forcecapture.orderSource = 'ecommerce'
         
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
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <forceCapture reportGroup="DefaultReportGroup">
    <orderId>12344</orderId>
    <amount>106</amount>
    <orderSource>ecommerce</orderSource>
    <card>
      <type>VI</type>
      <number>4100000000000001</number>
      <expDate>1210</expDate>
    </card>
  </forceCapture>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
        
    #new for 8.29
    def testforceCaptureWithSecondaryAmount(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106
        forcecapture.orderId = "12344"
        forcecapture.orderSource = 'ecommerce'
        forcecapture.secondaryAmount = 100
        
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
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <forceCapture reportGroup="DefaultReportGroup">
    <orderId>12344</orderId>
    <amount>106</amount>
    <secondaryAmount>100</secondaryAmount>
    <orderSource>ecommerce</orderSource>
    <card>
      <type>VI</type>
      <number>4100000000000001</number>
      <expDate>1210</expDate>
    </card>
  </forceCapture>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)

    def testSale(self):
        sale = litleXmlFields.sale()
        sale.amount = 106
        sale.litleTxnId = 123456
        sale.orderId = "12344"
        sale.orderSource = 'ecommerce'
         
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
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <sale reportGroup="DefaultReportGroup">
    <litleTxnId>123456</litleTxnId>
    <orderId>12344</orderId>
    <amount>106</amount>
    <orderSource>ecommerce</orderSource>
    <card>
      <type>VI</type>
      <number>4100000000000002</number>
      <expDate>1210</expDate>
    </card>
  </sale>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
    
    #new for 8.29  
    def testSaleWithSecondaryAmountAndApplepay(self):
        sale = litleXmlFields.sale()
        sale.amount = 106
        sale.litleTxnId = 123456
        sale.orderId = "12344"
        sale.orderSource = 'ecommerce'
        sale.secondaryAmount=100
         
        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "yoyo"
        applepay.version = '8.29'
        header=litleXmlFields.applepayHeaderType()
        header.applicationData='applicationData'
        header.ephemeralPublicKey ='UWIRNRSKSXMXEYEINR'
        header.publicKeyHash='UYTGHJKMNBVFYWUWI'
        header.transactionId='1024'
        applepay.header=header
        sale.applepay = applepay
         
        comm = Communications(config)
        comm.http_post = MagicMock()
 
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(sale)
         
        comm.http_post.assert_called_once()
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <sale reportGroup="DefaultReportGroup">
    <litleTxnId>123456</litleTxnId>
    <orderId>12344</orderId>
    <amount>106</amount>
    <secondaryAmount>100</secondaryAmount>
    <orderSource>ecommerce</orderSource>
    <applepay>
      <data>4100000000000000</data>
      <header>
        <applicationData>applicationData</applicationData>
        <ephemeralPublicKey>UWIRNRSKSXMXEYEINR</ephemeralPublicKey>
        <publicKeyHash>UYTGHJKMNBVFYWUWI</publicKeyHash>
        <transactionId>1024</transactionId>
      </header>
      <signature>yoyo</signature>
      <version>8.29</version>
    </applepay>
  </sale>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
 
    #new for 8.29
    def testTokenWithApplepay(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = "12344"
        
        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "yoyo"
        applepay.version = '8.29'
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
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <registerTokenRequest reportGroup="DefaultReportGroup">
    <orderId>12344</orderId>
    <applepay>
      <data>4100000000000000</data>
      <header>
        <applicationData>applicationData</applicationData>
        <ephemeralPublicKey>UWIRNRSKSXMXEYEINR</ephemeralPublicKey>
        <publicKeyHash>UYTGHJKMNBVFYWUWI</publicKeyHash>
        <transactionId>1024</transactionId>
      </header>
      <signature>yoyo</signature>
      <version>8.29</version>
    </applepay>
  </registerTokenRequest>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
        
    def testToken(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = "12344"
        token.accountNumber = "1233456789103801"
         
        comm = Communications(config)
        comm.http_post = MagicMock()
 
        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(token)
         
        comm.http_post.assert_called_once()
        expected = """<?xml version="1.0" encoding="utf-8"?>
<litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
  <authentication>
    <user>jenkins</user>
    <password>PYTHON</password>
  </authentication>
  <registerTokenRequest reportGroup="DefaultReportGroup">
    <orderId>12344</orderId>
    <accountNumber>1233456789103801</accountNumber>
  </registerTokenRequest>
</litleOnlineRequest>
"""
        comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
#         
#     def testExtraField(self):
#         auth = litleXmlFields.authorization()
#         auth.orderId = '1234'
#         auth.amount = 106
#         auth.orderSource = 'ecommerce'
#         auth.extraField = "extra"
#         
#         card = litleXmlFields.cardType()
#         card.number = "4100000000000000"
#         card.expDate = "1210"
#         card.type = 'VI'
#         auth.card = card
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(auth)
#         
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <authorization reportGroup="DefaultReportGroup">
#     <orderId>1234</orderId>
#     <amount>106</amount>
#     <orderSource>ecommerce</orderSource>
#     <card>
#       <type>VI</type>
#       <number>4100000000000000</number>
#       <expDate>1210</expDate>
#     </card>
#   </authorization>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testExtraChoices(self):
#         auth = litleXmlFields.authorization()
#         auth.orderId = '1234'
#         auth.amount = 106
#         auth.orderSource = 'ecommerce'
#         
#         card = litleXmlFields.cardType()
#         card.number = "4100000000000000"
#         card.expDate = "1210"
#         card.type = 'VI'
#         auth.card = card
# 
#         paypal = litleXmlFields.payPal()
#         paypal.payerId = "1234"
#         paypal.token = "1234"
#         paypal.transactionId = '123456'
#         auth.paypal = paypal
# 
#         litle = litleOnlineRequest(config)
#         with self.assertRaises(Exception):
#             litle.sendRequest(auth)
# 
#     def testInvalidEnum(self):
#         auth = litleXmlFields.authorization()
#         auth.orderId = '1234'
#         auth.amount = 106
#         auth.orderSource = 'ecommerce'
#         auth.extraField = "extra"
#         
#         card = litleXmlFields.cardType()
#         card.number = "4100000000000000"
#         card.expDate = "1210"
#         
#         with self.assertRaises(pyxb.BadTypeValueError):
#             card.type = 'VC'
#             auth.card = card
# 
#     def testCustomerInfoDob(self):
#         auth = litleXmlFields.authorization();
#         auth.reportGroup = 'Planets'
#         auth.orderId = '12344'
#         auth.amount = 106
#         auth.orderSource = 'ecommerce'
# 
#         card = litleXmlFields.cardType()
#         card.type = 'VI'
#         card.number = '4100000000000002'
#         card.expDate = '1210'
#         auth.card = card
#         customerInfo = litleXmlFields.customerInfo()
#         customerInfo.dob = '1980-04-14'
#         auth.customerInfo = customerInfo
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(auth)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <authorization reportGroup="DefaultReportGroup">
#     <orderId>12344</orderId>
#     <amount>106</amount>
#     <orderSource>ecommerce</orderSource>
#     <customerInfo>
#       <dob>1980-04-14</dob>
#     </customerInfo>
#     <card>
#       <type>VI</type>
#       <number>4100000000000002</number>
#       <expDate>1210</expDate>
#     </card>
#   </authorization>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testCancelSubscription(self):
#         cancel = litleXmlFields.cancelSubscription()
#         cancel.subscriptionId = '12345'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(cancel)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <cancelSubscription>
#     <subscriptionId>12345</subscriptionId>
#   </cancelSubscription>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testUpdateSubscription(self):
#         update = litleXmlFields.updateSubscription()
#         update.billingDate = '2013-08-07'
#         billToAddress = litleXmlFields.contact()
#         billToAddress.name = 'Greg Dake'
#         billToAddress.city = 'Lowell'
#         billToAddress.state = 'MA'
#         billToAddress.email = "sdksupport@litle.com"
#         update.billToAddress = billToAddress
#         card = litleXmlFields.cardType()
#         card.number = '4100000000000001'
#         card.expDate = '1215'
#         card.type = 'VI'
#         update.card = card
#         update.planCode = 'abcdefg'
#         update.subscriptionId = '12345'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(update)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <updateSubscription>
#     <subscriptionId>12345</subscriptionId>
#     <planCode>abcdefg</planCode>
#     <billToAddress>
#       <name>Greg Dake</name>
#       <city>Lowell</city>
#       <state>MA</state>
#       <email>sdksupport@litle.com</email>
#     </billToAddress>
#     <card>
#       <type>VI</type>
#       <number>4100000000000001</number>
#       <expDate>1215</expDate>
#     </card>
#     <billingDate>2013-08-07</billingDate>
#   </updateSubscription>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
#         
#     def testUpdatePlan(self):
#         update = litleXmlFields.updatePlan()
#         update.active = True
#         update.planCode = 'abc'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(update)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <updatePlan>
#     <planCode>abc</planCode>
#     <active>true</active>
#   </updatePlan>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testCreatePlan(self):
#         create = litleXmlFields.createPlan()
#         create.planCode = 'abc'
#         create.active = True
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(create)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <createPlan>
#     <planCode>abc</planCode>
#     <active>true</active>
#   </createPlan>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testActivate(self):
#         activate = litleXmlFields.activate()
#         activate.amount = 100
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(activate)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <activate reportGroup="DefaultReportGroup">
#     <amount>100</amount>
#   </activate>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testDeactivate(self):
#         deactivate = litleXmlFields.deactivate()
#         deactivate.orderId = '123'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(deactivate)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <deactivate reportGroup="DefaultReportGroup">
#     <orderId>123</orderId>
#   </deactivate>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testLoad(self):
#         load = litleXmlFields.load()
#         load.orderId = '123'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(load)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <load reportGroup="DefaultReportGroup">
#     <orderId>123</orderId>
#   </load>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testUnload(self):
#         unload = litleXmlFields.unload()
#         unload.orderId = '123'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(unload)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <unload reportGroup="DefaultReportGroup">
#     <orderId>123</orderId>
#   </unload>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testBalanceInquiry(self):
#         balanceInquiry = litleXmlFields.balanceInquiry()
#         balanceInquiry.orderId = '123'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(balanceInquiry)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <balanceInquiry reportGroup="DefaultReportGroup">
#     <orderId>123</orderId>
#   </balanceInquiry>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testActivateReversal(self):
#         activateReversal = litleXmlFields.activateReversal()
#         activateReversal.litleTxnId = '123'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(activateReversal)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <activateReversal reportGroup="DefaultReportGroup">
#     <litleTxnId>123</litleTxnId>
#   </activateReversal>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testDeactivateReversal(self):
#         deactivateReversal = litleXmlFields.deactivateReversal()
#         deactivateReversal.litleTxnId = '123'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(deactivateReversal)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <deactivateReversal reportGroup="DefaultReportGroup">
#     <litleTxnId>123</litleTxnId>
#   </deactivateReversal>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testLoadReversal(self):
#         loadReversal = litleXmlFields.loadReversal()
#         loadReversal.litleTxnId = '123'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(loadReversal)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <loadReversal reportGroup="DefaultReportGroup">
#     <litleTxnId>123</litleTxnId>
#   </loadReversal>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testUnloadReversal(self):
#         unloadReversal = litleXmlFields.unloadReversal()
#         unloadReversal.litleTxnId = '123'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(unloadReversal)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <unloadReversal reportGroup="DefaultReportGroup">
#     <litleTxnId>123</litleTxnId>
#   </unloadReversal>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testRefundReversal(self):
#         refundReversal = litleXmlFields.refundReversal()
#         refundReversal.litleTxnId = '123'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(refundReversal)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <refundReversal reportGroup="DefaultReportGroup">
#     <litleTxnId>123</litleTxnId>
#   </refundReversal>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testDepositReversal(self):
#         depositReversal = litleXmlFields.depositReversal()
#         depositReversal.litleTxnId = '123'
# 
#         comm = Communications(config)
#         comm.http_post = MagicMock()
# 
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(depositReversal)
# 
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="8.27.0" version="8.27" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <depositReversal reportGroup="DefaultReportGroup">
#     <litleTxnId>123</litleTxnId>
#   </depositReversal>
# </litleOnlineRequest>
# """
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testAuthorizationIncludesWallet(self):
#         authorization = litleXmlFields.authorization()
#         authorization.wallet = litleXmlFields.wallet()
#         authorization.wallet.walletSourceType = litleXmlFields.walletSourceType.MasterPass
#         authorization.wallet.walletSourceTypeId = '5'
#         
#         comm = Communications(config)
#         comm.http_post = MagicMock()
#         
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(authorization)
#         
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="{0}" version="{1}" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <authorization reportGroup="DefaultReportGroup">
#     <wallet>
#       <walletSourceType>MasterPass</walletSourceType>
#       <walletSourceTypeId>5</walletSourceTypeId>
#     </wallet>
#   </authorization>
# </litleOnlineRequest>
# """.format("8.27.0", "8.27")
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
# 
#     def testSaleIncludesWallet(self):
#         sale = litleXmlFields.sale()
#         sale.wallet = litleXmlFields.wallet()
#         sale.wallet.walletSourceType = litleXmlFields.walletSourceType.MasterPass
#         sale.wallet.walletSourceTypeId = '5'
#         
#         comm = Communications(config)
#         comm.http_post = MagicMock()
#         
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(sale)
#         
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="{0}" version="{1}" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <sale reportGroup="DefaultReportGroup">
#     <wallet>
#       <walletSourceType>MasterPass</walletSourceType>
#       <walletSourceTypeId>5</walletSourceTypeId>
#     </wallet>
#   </sale>
# </litleOnlineRequest>
# """.format("8.27.0", "8.27")
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)
#         
#     def testEcheckTxnsCanHavePpdAsOrderSource(self):
#         echeckSale = litleXmlFields.echeckSale()
#         echeckSale.orderSource = litleXmlFields.orderSourceType.echeckppd
#         
#         comm = Communications(config)
#         comm.http_post = MagicMock()
#         
#         litle = litleOnlineRequest(config)
#         litle.setCommunications(comm)
#         litle._processResponse = MagicMock(return_value=None)
#         litle.sendRequest(echeckSale)
#         
#         comm.http_post.assert_called_once()
#         expected = """<?xml version="1.0" encoding="utf-8"?>
# <litleOnlineRequest merchantId="101" merchantSdk="{0}" version="{1}" xmlns="http://www.litle.com/schema">
#   <authentication>
#     <user>jenkins</user>
#     <password>PYTHON</password>
#   </authentication>
#   <echeckSale reportGroup="DefaultReportGroup">
#     <orderSource>echeckppd</orderSource>
#   </echeckSale>
# </litleOnlineRequest>
# """.format("8.27.0", "8.27")
#         comm.http_post.assert_called_with(expected, url=ANY, proxy=ANY, timeout=ANY)


def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLitleOnline)
    return suite

if __name__ =='__main__':
    unittest.main()