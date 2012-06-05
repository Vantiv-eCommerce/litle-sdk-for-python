from SetupTest import *
import unittest

class TestAuthReversal(unittest.TestCase):
    
    def test_simple_authReversal(self):
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = 12345678000
        reversal.amount = 106
        reversal.payPalNotes = "Notes"

    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(reversal)
            
        self.assertEquals("Approved",response.transactionResponse.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuthReversal)
    return suite