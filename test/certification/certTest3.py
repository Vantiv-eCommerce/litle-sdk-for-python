from SetupTest import *
import unittest

class certTest3(unittest.TestCase):
#    
    def test32(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '32'
        authorization.amount = 10010
        authorization.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.name = "John Smith"
        billtoaddress.addressLine1 = "1 Main St."
        billtoaddress.city = "Burlington"
        billtoaddress.state = "MA"
        billtoaddress.zip = "01803-3747"
        billtoaddress.country = 'US'
        authorization.billToAddress = billtoaddress
        
        card = litleXmlFields.cardType()
        card.number = "4457010000000009"
        card.expDate = "0112"
        card.type = 'VI'
        card.cardValidationNum = "349"
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("11111 ", response.transactionResponse.authCode)
        self.assertEquals("01", response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M", response.transactionResponse.fraudResult.cardValidationResult)
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.transactionResponse.litleTxnId
        capture.amount = 5005
        captureResponse = litleXml.litleXmlMapper(capture)
        self.assertEquals("000", captureResponse.transactionResponse.response)
        self.assertEquals("Approved", captureResponse.transactionResponse.message)
        
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = response.transactionResponse.litleTxnId
        reversalResponse = litleXml.litleXmlMapper(reversal)
        self.assertEquals("111", reversalResponse.transactionResponse.response)
        self.assertEquals("Authorization amount has already been depleted", reversalResponse.transactionResponse.message)

    def test33(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '33'
        authorization.amount = 20020
        authorization.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.name = "Mike J. Hammer"
        billtoaddress.addressLine1 = "2 Main St."
        billtoaddress.addressLine2 = "Apt. 222"
        billtoaddress.city = "Riverside"
        billtoaddress.state = "RI"
        billtoaddress.zip = "02915"
        billtoaddress.country = 'US'
        authorization.billToAddress = billtoaddress
        
        card = litleXmlFields.cardType()
        card.number = "5112010000000003"
        card.expDate = "0212"
        card.type = 'MC'
        card.cardValidationNum = "261"
        authorization.card = card
        
        fraud = litleXmlFields.fraudCheckType()
        fraud.authenticationValue = "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = fraud
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(authorization)
        self.assertEquals("000", response.transactionResponse.response)
        self.assertEquals("Approved", response.transactionResponse.message)
        self.assertEquals("22222", response.transactionResponse.authCode)
        self.assertEquals("10", response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M", response.transactionResponse.fraudResult.cardValidationResult)
        
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = response.transactionResponse.litleTxnId
        reversalResponse = litleXml.litleXmlMapper(reversal)
        self.assertEquals("000", reversalResponse.transactionResponse.response)
        self.assertEquals("Approved", reversalResponse.transactionResponse.message)

    def test34(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '34'
        authorization.amount = 30030
        authorization.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.name = "Eileen Jones"
        billtoaddress.addressLine1 = "3 Main St."
        billtoaddress.city = "Bloomfield"
        billtoaddress.state = "CT"
        billtoaddress.zip = "06002"
        billtoaddress.country = 'US'
        authorization.billToAddress = billtoaddress
        
        card = litleXmlFields.cardType()
        card.number = "6011010000000003"
        card.expDate = "0312"
        card.type = 'DI'
        card.cardValidationNum = "758"
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("33333", response.transactionResponse.authCode)
        self.assertEquals("10", response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M", response.transactionResponse.fraudResult.cardValidationResult)
        
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = response.transactionResponse.litleTxnId
        reversalResponse = litleXml.litleXmlMapper(reversal)
        self.assertEquals("000", reversalResponse.transactionResponse.response)
        self.assertEquals("Approved", reversalResponse.transactionResponse.message)
        
    def test35(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '35'
        authorization.amount = 40040
        authorization.orderSource = 'ecommerce'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.name = "Bob Black"
        billtoaddress.addressLine1 = "4 Main St."
        billtoaddress.city = "Laurel"
        billtoaddress.state = "MD"
        billtoaddress.zip = "20708"
        billtoaddress.country = 'US'
        authorization.billToAddress = billtoaddress
        
        card = litleXmlFields.cardType()
        card.number = "375001000000005"
        card.expDate = "0412"
        card.type = 'AX'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("44444", response.transactionResponse.authCode)
        self.assertEquals("12", response.transactionResponse.fraudResult.avsResult)
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.transactionResponse.litleTxnId
        capture.amount = 20020
        captureResponse = litleXml.litleXmlMapper(capture)
        self.assertEquals("000", captureResponse.transactionResponse.response)
        self.assertEquals("Approved", captureResponse.transactionResponse.message)
        
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = response.transactionResponse.litleTxnId
        reversalResponse = litleXml.litleXmlMapper(reversal)
        self.assertEquals("000", reversalResponse.transactionResponse.response)
        self.assertEquals("Approved", reversalResponse.transactionResponse.message)
        
    def test36(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '36'
        authorization.amount = 20500
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "375000026600004"
        card.expDate = "0512"
        card.type = 'AX'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = response.transactionResponse.litleTxnId
        reversal.amount = 10000
        reversalResponse = litleXml.litleXmlMapper(reversal)
        self.assertEquals("336", reversalResponse.transactionResponse.response)
        self.assertEquals("Reversal Amount does not match Authorization amount", reversalResponse.transactionResponse.message)

if __name__ == '__main__':
    unittest.main()      