from SetupTest import *
import unittest

class TestCapture(unittest.TestCase):
    
    def test_simple_capture(self):
        Capture = litleXmlFields.capture()
        Capture.litleTxnId = 123456000
        Capture.amount = 106
        Capture.payPalNotes = "Notes"
    
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(Capture)
            
        self.assertEquals("Approved",response.transactionResponse.message)
        
    def test_simple_capture_with_partial(self):
        Capture = litleXmlFields.capture()
        Capture.litleTxnId = 123456000
        Capture.amount = 106
        Capture.partial = True
        Capture.payPalNotes = "Notes"
    
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(Capture)
            
        self.assertEquals("Approved",response.transactionResponse.message)
        
    def test_complex_capture(self):
        Capture = litleXmlFields.capture()
        Capture.litleTxnId = 123456000
        Capture.amount = 106
        Capture.payPalNotes = "Notes"
        
        enhanced = litleXmlFields.enhancedData()
        enhanced.customerReference = "Litle"
        enhanced.salesTax = 50
        enhanced.deliveryType = "TBD"
        Capture.enhancedData = enhanced
        
        Capture.payPalOrderComplete = True
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(Capture)
            
        self.assertEquals("Approved",response.transactionResponse.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCapture)
    return suite