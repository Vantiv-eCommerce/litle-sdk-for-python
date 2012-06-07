from litleSdkPythonTest.all.SetupTest import *
import unittest

class TestEcheckVoid(unittest.TestCase):
    
    def test_TestEcheckVoid(self):
        echeckvoid = litleXmlFields.echeckVoid()
        echeckvoid.litleTxnId = 123456789101112L
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckvoid)
        self.assertEquals(response.message, "Valid Format")
        self.assertEquals("Approved",response.transactionResponse.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEcheckVoid)
    return suite