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

class TestConfigOverride(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def testUserOverride(self):
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
        litle.sendRequest(authorization, user='Dan')
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<user>Dan</user>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testPasswordOverride(self):
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
        litle.sendRequest(authorization, password = 'customPassword')
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<password>customPassword</password>.*?")
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testVersionOverride(self):
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
        litle.sendRequest(authorization, version="3.14")
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher('.*?version="8.13".*?')
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testMerchantIdOverride(self):
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
        litle.sendRequest(authorization, merchantId="98765")
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher('.*?merchantId="98765".*?')
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testReportGroupOverride(self):
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
        litle.sendRequest(authorization, reportGroup="testReports")
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher('.*?reportGroup="testReports".*?')
        comm.http_post.assert_called_with(match_re, url=ANY, proxy=ANY, timeout=ANY)
        
    def testTimeoutOverride(self):
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
        litle.sendRequest(authorization, timeout=42)
        
        comm.http_post.assert_called_once()
        comm.http_post.assert_called_with(ANY, url=ANY, proxy=ANY, timeout=42)
        
    def testUrlOverride(self):
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
        litle.sendRequest(authorization, url="www.customurl.com")
        
        comm.http_post.assert_called_once()
        comm.http_post.assert_called_with(ANY, url="www.customurl.com", proxy=ANY, timeout=ANY)
        
    def testProxyOverride(self):
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
        litle.sendRequest(authorization, proxy="bumpyproxy:1776")
        
        comm.http_post.assert_called_once()
        comm.http_post.assert_called_with(ANY, url=ANY, 
                                          proxy="bumpyproxy:1776", 
                                          timeout=ANY)
        
    def testMissingUser(self):
        config2 = Configuration()
        config2.setPassword("Pass")
        config2.setMerchantId("12345")
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'
        authorization.card = card

        comm = Communications(config2)
        comm.http_post = MagicMock()        

        with self.assertRaises(AttributeError):
            litleOnlineRequest(config2)
            
    def testMissingPassword(self):
        config3 = Configuration()
        config3.setUser("User")
        config3.setMerchantId("12345")
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'
        authorization.card = card

        comm = Communications(config3)
        comm.http_post = MagicMock()        

        with self.assertRaises(AttributeError):
            litleOnlineRequest(config3)
            
    def testMissingId(self):
        config4 = Configuration()
        config4.setUser("User")
        config4.setPassword("Pass")
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'
        authorization.card = card

        comm = Communications(config4)
        comm.http_post = MagicMock()        

        with self.assertRaises(AttributeError):
            litleOnlineRequest(config4)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestConfigOverride)
    return suite

if __name__ =='__main__':
    unittest.main()