from test.all.SetupTest import *
import unittest
from mock import *

class TestConfigOverride(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_userOverride(self):
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
        litle.sendRequest(authorization, user = 'Dan')
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<user>Dan</user>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)
        
    def test_passwordOverride(self):
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
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)
        
    def test_versionOverride(self):
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
        litle.sendRequest(authorization, version = "3.14")
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher('.*?version="3.14".*?')
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)
        
    def test_merchantIdOverride(self):
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
        litle.sendRequest(authorization, merchantId = "98765")
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher('.*?merchantId="98765".*?')
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)
        
    def test_reportGroupOverride(self):
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
        litle.sendRequest(authorization, reportGroup = "testReports")
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher('.*?reportGroup="testReports".*?')
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)
        
    def test_timeoutOverride(self):
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
        litle.sendRequest(authorization, timeout = 42)
        
        comm.http_post.assert_called_once()
        comm.http_post.assert_called_with(ANY,url=ANY,proxy=ANY,timeout=42)
        
    def test_urlOverride(self):
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
        litle.sendRequest(authorization, url = "www.customurl.com")
        
        comm.http_post.assert_called_once()
        comm.http_post.assert_called_with(ANY,url="www.customurl.com",proxy=ANY,timeout=ANY)
        
    def test_proxyOverride(self):
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
        litle.sendRequest(authorization, proxy = "bumpyproxy:1776")
        
        comm.http_post.assert_called_once()
        comm.http_post.assert_called_with(ANY,url=ANY,proxy="bumpyproxy:1776",timeout=ANY)
        
    def test_missingUser(self):
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
            
    def test_missingPassword(self):
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
            
    def test_missingId(self):
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