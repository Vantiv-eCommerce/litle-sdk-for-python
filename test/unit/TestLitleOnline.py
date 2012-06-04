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
        m = MagicMock(return_value = "<litleOnlineResponse version='8.10' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><authorizationResponse><litleTxnId>123</litleTxnId></authorizationResponse></litleOnlineResponse>")
        print m.http_post()
        print m.property.http_post.attribute()
        
        litle = litleOnlineRequest(config)
        litle.sendRequest(authorization)
        print m.method_calls
        #'<?xml version="1.0" ?><litleOnlineRequest merchantId="101" version="8.1" xmlns="http://www.litle.com/schema"><authentication><user>PHXMLTEST</user><password>certpass</password></authentication><authorization reportGroup="Planets"><orderId>1234</orderId><amount>106</amount><orderSource>ecommerce</orderSource><card><type>VI</type><number>4100000000000000</number><expDate>1210</expDate></card></authorization></litleOnlineRequest>',url=None,proxy=None,timeout=None
       # matcher = Matcher(".*?<litleOnlineRequest.*?<authorization.*?<card>.*?<number>4100000000000002</number>.*?</card>.*?</authorization>.*?",Comm)
        m.assert_called_once()
        m.http_post.assert_called_with(False)
       # m.assert_called_with("hi")
#        litle = litleOnlineRequest(config)
#        litle.sendRequest = MagicMock(return_value = 1)
#        litle.sendRequest(authorization)        
#        litle.sendRequest.assert_called_once_with(authorization)
#        
#class Matcher(object):
#     def __init__(self, compare, some_obj):
#         self.compare = compare
#         self.some_obj = some_obj
#     def __eq__(self, other):
#         return self.compare(self.some_obj, other)