from SetupTest import *
import unittest

class certTest4(unittest.TestCase):
    
    def test37(self):
        verification = litleXmlFields.echeckVerification()
        verification.orderId = "37"
        verification.amount = 3001
        verification.orderSource = 'telephone'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.firstName = "Tom"
        billtoaddress.lastName = "Black"
        verification.billToAddress = billtoaddress
        
        echeck = litleXmlFields.echeck()
        echeck.accNum = "10@BC99999"
        echeck.accType = 'Checking'
        echeck.routingNum = "053100300"
        verification.echeckOrEcheckToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(verification)
        self.assertEquals("301", response.transactionResponse.response)
        self.assertEquals("Invalid Account Number", response.transactionResponse.message)
    
    def test38(self):
        verification = litleXmlFields.echeckVerification()
        verification.orderId = "38"
        verification.amount = 3002
        verification.orderSource = 'telephone'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.firstName = "John"
        billtoaddress.lastName = "Smith"
        billtoaddress.phone = "999-999-999"
        verification.billToAddress = billtoaddress
        
        echeck = litleXmlFields.echeck()
        echeck.accNum = "1099999999"
        echeck.accType = 'Checking'
        echeck.routingNum = "053000219"
        verification.echeckOrEcheckToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(verification)
        self.assertEquals("000", response.transactionResponse.response)
        self.assertEquals("Approved", response.transactionResponse.message)
        
    def test39(self):
        verification = litleXmlFields.echeckVerification()
        verification.orderId = "39"
        verification.amount = 3003
        verification.orderSource = 'telephone'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.firstName = "Robert"
        billtoaddress.lastName = "Jones"
        billtoaddress.companyName = "Good Goods Inc"
        billtoaddress.phone = "9999999999"
        verification.billToAddress = billtoaddress
        
        echeck = litleXmlFields.echeck()
        echeck.accNum = "3099999999"
        echeck.accType = 'Corporate'
        echeck.routingNum = "053100300"
        verification.echeckOrEcheckToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(verification)
        self.assertEquals("950", response.transactionResponse.response)
        self.assertEquals("Declined - Negative Information on File", response.transactionResponse.message)
        
    def test40(self):
        verification = litleXmlFields.echeckVerification()
        verification.orderId = "40"
        verification.amount = 3004
        verification.orderSource = 'telephone'
        
        billtoaddress = litleXmlFields.contact()
        billtoaddress.firstName = "Peter"
        billtoaddress.lastName = "Green"
        billtoaddress.companyName = "Green Co"
        billtoaddress.phone = "9999999999"
        verification.billToAddress = billtoaddress
        
        echeck = litleXmlFields.echeck()
        echeck.accNum = "8099999999"
        echeck.accType = 'Corporate'
        echeck.routingNum = "063102152"
        verification.echeckOrEcheckToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(verification)
        self.assertEquals("951", response.transactionResponse.response)
        self.assertEquals("Absolute Decline", response.transactionResponse.message)
        
#    def test41(self):
#        sale = litleXmlFields.echeckSale()
#        sale.orderId = "41"
#        sale.amount = 2008
#        sale.orderSource = 'telephone'
#        
#        billtoaddress = litleXmlFields.contact()
#        billtoaddress.firstName = "Mike"
#        billtoaddress.middleInitial = "J"
#        billtoaddress.lastName = "Hammer"
#        sale.billToAddress = billtoaddress
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accNum = "10@BC99999"
#        echeck.accType = 'Checking'
#        echeck.routingNum = "053100300"
#        sale.echeckOrEcheckToken = echeck
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(sale)
#        self.assertEquals("301", response.transactionResponse.response)
#        self.assertEquals("Invalid Account Number", response.transactionResponse.message)
#        
#    def test42(self):
#        sale = litleXmlFields.echeckSale()
#        sale.orderId = "42"
#        sale.amount = 2004
#        sale.orderSource = 'telephone'
#        
#        billtoaddress = litleXmlFields.contact()
#        billtoaddress.firstName = "Tom"
#        billtoaddress.lastName = "Black"
#        sale.billToAddress = billtoaddress
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accNum = "4099999992"
#        echeck.accType = 'Checking'
#        echeck.routingNum = "211370545"
#        sale.echeckOrEcheckToken = echeck
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(sale)
#        self.assertEquals("000", response.transactionResponse.response)
#        self.assertEquals("Approved", response.transactionResponse.message)
#        
#    def test43(self):
#        sale = litleXmlFields.echeckSale()
#        sale.orderId = "43"
#        sale.amount = 2007
#        sale.orderSource = 'telephone'
#        
#        billtoaddress = litleXmlFields.contact()
#        billtoaddress.firstName = "Peter"
#        billtoaddress.lastName = "Green"
#        billtoaddress.companyName = "Green Co"
#        sale.billToAddress = billtoaddress
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accNum = "6099999992"
#        echeck.accType = 'Corporate'
#        echeck.routingNum = "211370545"
#        sale.echeckOrEcheckToken = echeck
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(sale)
#        self.assertEquals("000", response.transactionResponse.response)
#        self.assertEquals("Approved", response.transactionResponse.message)
#        
#    def test44(self):
#        sale = litleXmlFields.echeckSale()
#        sale.orderId = "44"
#        sale.amount = 2009
#        sale.orderSource = 'telephone'
#        
#        billtoaddress = litleXmlFields.contact()
#        billtoaddress.firstName = "Peter"
#        billtoaddress.lastName = "Green"
#        billtoaddress.companyName = "Green Co"
#        sale.billToAddress = billtoaddress
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accNum = "9099999992"
#        echeck.accType = 'Corporate'
#        echeck.routingNum = "053133052"
#        sale.echeckOrEcheckToken = echeck
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(sale)
#        self.assertEquals("900", response.transactionResponse.response)
#        self.assertEquals("Invalid Bank Routing Number", response.transactionResponse.message)
#        
#    def test45(self):
#        credit = litleXmlFields.echeckCredit()
#        credit.orderId = "45"
#        credit.amount = 1001
#        credit.orderSource = 'telephone'
#        
#        billtoaddress = litleXmlFields.contact()
#        billtoaddress.firstName = "John"
#        billtoaddress.lastName = "Smith"
#        credit.billToAddress = billtoaddress
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accNum = "10@BC99999"
#        echeck.accType = 'Checking'
#        echeck.routingNum = "053100300"
#        credit.echeckOrEcheckToken = echeck
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(credit)
#        self.assertEquals("301", response.transactionResponse.response)
#        self.assertEquals("Invalid Account Number", response.transactionResponse.message)
#        
#    def test46(self):
#        credit = litleXmlFields.echeckCredit()
#        credit.orderId = "46"
#        credit.amount = 1003
#        credit.orderSource = 'telephone'
#        
#        billtoaddress = litleXmlFields.contact()
#        billtoaddress.firstName = "Robert"
#        billtoaddress.lastName = "Jones"
#        billtoaddress.companyName = "Widget Inc"
#        credit.billToAddress = billtoaddress
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accNum = "3099999999"
#        echeck.accType = 'Corporate'
#        echeck.routingNum = "063102152"
#        credit.echeckOrEcheckToken = echeck
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(credit)
#        self.assertEquals("000", response.transactionResponse.response)
#        self.assertEquals("Approved", response.transactionResponse.message)
#        
#    def test47(self):
#        credit = litleXmlFields.echeckCredit()
#        credit.orderId = "47"
#        credit.amount = 1007
#        credit.orderSource = 'telephone'
#        
#        billtoaddress = litleXmlFields.contact()
#        billtoaddress.firstName = "Peter"
#        billtoaddress.lastName = "Green"
#        billtoaddress.companyName = "Green Co"
#        credit.billToAddress = billtoaddress
#        
#        echeck = litleXmlFields.echeck()
#        echeck.accNum = "6099999993"
#        echeck.accType = 'Corporate'
#        echeck.routingNum = "211370545"
#        credit.echeckOrEcheckToken = echeck
#        
#        litleXml =  litleOnlineRequest(config)
#        response = litleXml.litleXmlMapper(credit)
#        self.assertEquals("301", response.transactionResponse.response)
#        self.assertEquals("Invalid Account Number", response.transactionResponse.message)
#        
    def test48(self):
        credit = litleXmlFields.echeckCredit()
        credit.litleTxnId = 430000000000000001
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(credit)
        self.assertEquals("000", response.transactionResponse.response)
        self.assertEquals("Approved", response.transactionResponse.message)
        
    def test49(self):
        credit = litleXmlFields.echeckCredit()
        credit.litleTxnId = 2
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(credit)
        self.assertEquals("360", response.transactionResponse.response)
        self.assertEquals("No transaction found with specified litleTxnId", response.transactionResponse.message)
