from litleSdkPythonTest.all.SetupTest import *
import unittest

class TestSale(unittest.TestCase):
    
    def test_simpleSaleWithCard(self):
        sale = litleXmlFields.sale()
        sale.litleTxnId = 123456L
        sale.amount = 106L
        sale.orderId = '12344'
        sale.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals(response.message, "Valid Format")
        self.assertEquals("Approved",response.transactionResponse.message)
        
    def test_simpleSaleWithPayPal(self):
        sale = litleXmlFields.sale()
        sale.litleTxnId = 123456L
        sale.amount = 106L
        sale.orderId = '12344'
        sale.orderSource = 'ecommerce'
        
        paypal = litleXmlFields.payPal()
        paypal.payerId = "1234"
        paypal.token = "1234"
        paypal.transactionId = "123456"
        sale.paypal = paypal
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals(response.message, "Valid Format")
        self.assertEquals("Approved",response.transactionResponse.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSale)
    return suite