from test.all.SetupTest import *
import unittest

class TestCreateFromDom(unittest.TestCase):
    
    def test_simpleExtraField(self):
        xml_text="<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><captureGivenAuthResponse id='' reportGroup='DefaultReportGroup' customerId=''><litleTxnId>057484783403434000</litleTxnId><orderId>12344</orderId><response>000</response><responseTime>2012-06-05T16:36:39</responseTime><message>Approved</message><authCode>83307</authCode></captureGivenAuthResponse></litleOnlineResponse>"
        xml_object = litleXmlFields.CreateFromDocument(xml_text)
        self.assertEquals("Approved",xml_object.transactionResponse.message)
        
    def test_simpleExtraFieldEmbeddedExtraField(self):
        xml_text="<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><captureGivenAuthResponse id='' reportGroup='DefaultReportGroup' customerId=''><litleTxnId>057484783403434000</litleTxnId><orderId>12344</orderId><response>000</response><responseTime>2012-06-05T16:36:39</responseTime><message>Approved</message><authCode><extraField>extra</extraField></authCode></captureGivenAuthResponse></litleOnlineResponse>"
        xml_object = litleXmlFields.CreateFromDocument(xml_text)
        self.assertEquals("Approved",xml_object.transactionResponse.message)
        
    def test_simple_EmbeddedField(self):
        xml_text="<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><authorizationResponse id='' reportGroup='DefaultReportGroup' customerId=''><litleTxnId>057484783403434000</litleTxnId><orderId>12344</orderId><response>000</response><responseTime>2012-06-05T16:36:39</responseTime><message>Approved</message><tokenResponse><litleToken>4242424242424242</litleToken><tokenResponseCode>111</tokenResponseCode><tokenMessage>Message</tokenMessage><bin>bin</bin></tokenResponse></authorizationResponse></litleOnlineResponse>"
        xml_object = litleXmlFields.CreateFromDocument(xml_text)
        self.assertEquals("bin",xml_object.transactionResponse.tokenResponse.bin)
        self.assertEquals("Message",xml_object.transactionResponse.tokenResponse.tokenMessage)

    def test_simple_ExtraEmbeddedField(self):
        xml_text="<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><authorizationResponse id='' reportGroup='DefaultReportGroup' customerId=''><litleTxnId>057484783403434000</litleTxnId><orderId>12344</orderId><response>000</response><responseTime>2012-06-05T16:36:39</responseTime><message>Approved</message><tokenResponse><litleToken>4242424242424242</litleToken><tokenResponseCode>111</tokenResponseCode><tokenMessage>Message</tokenMessage><bin>bin</bin><extra>extra</extra></tokenResponse></authorizationResponse></litleOnlineResponse>"
        xml_object = litleXmlFields.CreateFromDocument(xml_text)
        self.assertEquals("bin",xml_object.transactionResponse.tokenResponse.bin)
        self.assertEquals("Message",xml_object.transactionResponse.tokenResponse.tokenMessage)
        
def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateFromDom)
    return suite