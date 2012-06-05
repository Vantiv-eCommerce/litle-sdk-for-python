from SetupTest import *
import unittest

class TestHandleExtraField(unittest.TestCase):
    
    def test_simpleExtraField(self):
        xml_text="<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><captureGivenAuthResponse id='' reportGroup='DefaultReportGroup' customerId=''><litleTxnId>057484783403434000</litleTxnId><orderId>12344</orderId><response>000</response><responseTime>2012-06-05T16:36:39</responseTime><message>Approved</message><authCode>83307</authCode></captureGivenAuthResponse></litleOnlineResponse>"

        xml_compare="<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'><captureGivenAuthResponse id='' reportGroup='DefaultReportGroup' customerId=''><litleTxnId>057484783403434000</litleTxnId><orderId>12344</orderId><response>000</response><responseTime>2012-06-05T16:36:39</responseTime><message>Approved</message></captureGivenAuthResponse></litleOnlineResponse>"

        new_xml = litleXmlFields.handleExtraField(xml_text)
      #  print new_xml
        self.assertEquals(new_xml,xml_compare)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSale)
    return suite