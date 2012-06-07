from litleSdkPythonTest.all.SetupTest import *
import unittest

class certTest2(unittest.TestCase):
    
    def test14(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '14'
        authorization.amount = 3000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "4457010200000247"
        card.expDate = "0812"
        card.type = 'VI'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("PREPAID",response.transactionResponse.enhancedAuthResponse.fundingSource.type)
        self.assertEquals("2000", response.transactionResponse.enhancedAuthResponse.fundingSource.availableBalance)
        self.assertEquals("NO", response.transactionResponse.enhancedAuthResponse.fundingSource.reloadable)
        self.assertEquals("GIFT", response.transactionResponse.enhancedAuthResponse.fundingSource.prepaidCardType)
        
    def test15(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '15'
        authorization.amount = 3000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5500000254444445"
        card.expDate = "0312"
        card.type = 'MC'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("PREPAID",response.transactionResponse.enhancedAuthResponse.fundingSource.type)
        self.assertEquals("2000", response.transactionResponse.enhancedAuthResponse.fundingSource.availableBalance)
        self.assertEquals("YES", response.transactionResponse.enhancedAuthResponse.fundingSource.reloadable)
        self.assertEquals("PAYROLL", response.transactionResponse.enhancedAuthResponse.fundingSource.prepaidCardType)
        
    def test16(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '16'
        authorization.amount = 3000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5592106621450897"
        card.expDate = "0312"
        card.type = 'MC'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("PREPAID",response.transactionResponse.enhancedAuthResponse.fundingSource.type)
        self.assertEquals("0", response.transactionResponse.enhancedAuthResponse.fundingSource.availableBalance)
        self.assertEquals("YES", response.transactionResponse.enhancedAuthResponse.fundingSource.reloadable)
        self.assertEquals("PAYROLL", response.transactionResponse.enhancedAuthResponse.fundingSource.prepaidCardType)
        
    def test17(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '17'
        authorization.amount = 3000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5590409551104142"
        card.expDate = "0312"
        card.type = 'MC'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("PREPAID",response.transactionResponse.enhancedAuthResponse.fundingSource.type)
        self.assertEquals("6500", response.transactionResponse.enhancedAuthResponse.fundingSource.availableBalance)
        self.assertEquals("YES", response.transactionResponse.enhancedAuthResponse.fundingSource.reloadable)
        self.assertEquals("PAYROLL", response.transactionResponse.enhancedAuthResponse.fundingSource.prepaidCardType)
        
    def test18(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '18'
        authorization.amount = 3000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5587755665222179"
        card.expDate = "0312"
        card.type = 'MC'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("PREPAID",response.transactionResponse.enhancedAuthResponse.fundingSource.type)
        self.assertEquals("12200", response.transactionResponse.enhancedAuthResponse.fundingSource.availableBalance)
        self.assertEquals("YES", response.transactionResponse.enhancedAuthResponse.fundingSource.reloadable)
        self.assertEquals("PAYROLL", response.transactionResponse.enhancedAuthResponse.fundingSource.prepaidCardType)
        
    def test19(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '19'
        authorization.amount = 3000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5445840176552850"
        card.expDate = "0312"
        card.type = 'MC'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("PREPAID",response.transactionResponse.enhancedAuthResponse.fundingSource.type)
        self.assertEquals("20000", response.transactionResponse.enhancedAuthResponse.fundingSource.availableBalance)
        self.assertEquals("YES", response.transactionResponse.enhancedAuthResponse.fundingSource.reloadable)
        self.assertEquals("PAYROLL", response.transactionResponse.enhancedAuthResponse.fundingSource.prepaidCardType)
        
    def test20(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '20'
        authorization.amount = 3000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5390016478904678"
        card.expDate = "0312"
        card.type = 'MC'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("PREPAID",response.transactionResponse.enhancedAuthResponse.fundingSource.type)
        self.assertEquals("10050", response.transactionResponse.enhancedAuthResponse.fundingSource.availableBalance)
        self.assertEquals("YES", response.transactionResponse.enhancedAuthResponse.fundingSource.reloadable)
        self.assertEquals("PAYROLL", response.transactionResponse.enhancedAuthResponse.fundingSource.prepaidCardType)

    def test21(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '21'
        authorization.amount = 5000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "4457010201000246"
        card.expDate = "0912"
        card.type = 'VI'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("AFFLUENT",response.transactionResponse.enhancedAuthResponse.affluence)

    def test22(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '22'
        authorization.amount = 5000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "4457010202000245"
        card.expDate = "1111"
        card.type = 'VI'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("MASS AFFLUENT",response.transactionResponse.enhancedAuthResponse.affluence)

    def test23(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '23'
        authorization.amount = 5000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5112010201000109"
        card.expDate = "0412"
        card.type = 'MC'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("AFFLUENT",response.transactionResponse.enhancedAuthResponse.affluence)

    def test24(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '24'
        authorization.amount = 5000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5112010202000108"
        card.expDate = "0812"
        card.type = 'MC'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals('MASS AFFLUENT',response.transactionResponse.enhancedAuthResponse.affluence)

    def test25(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '25'
        authorization.amount = 5000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "4100204446270000"
        card.expDate = "1112"
        card.type = 'VI'
        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("BRA",response.transactionResponse.enhancedAuthResponse.issuerCountry)

    def test26(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '26'
        authorization.amount = 18698
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5194560012341234"
        card.expDate = "1212"
        card.type = 'MC'
        authorization.card = card
        
        authorization.allowPartialAuth = True
        healthcareiias = litleXmlFields.healthcareIIAS()
        healthcareamounts = litleXmlFields.healthcareAmounts()
        healthcareamounts.totalHealthcareAmount = 20000
        healthcareiias.healthcareAmounts = healthcareamounts
        healthcareiias.IIASFlag = 'Y'
        authorization.healthcareIIAS = healthcareiias
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals("341",response.transactionResponse.response)
        self.assertEquals("Invalid healthcare amounts",response.transactionResponse.message)

    def test27(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '27'
        authorization.amount = 18698
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5194560012341234"
        card.expDate = "1212"
        card.type = 'MC'
        authorization.card = card
        
        authorization.allowPartialAuth = True
        healthcareiias = litleXmlFields.healthcareIIAS()
        healthcareamounts = litleXmlFields.healthcareAmounts()
        healthcareamounts.totalHealthcareAmount = 15000
        healthcareamounts.RxAmount = 16000
        healthcareiias.healthcareAmounts = healthcareamounts
        healthcareiias.IIASFlag = 'Y'
        authorization.healthcareIIAS = healthcareiias
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals("341",response.transactionResponse.response)
        self.assertEquals("Invalid healthcare amounts",response.transactionResponse.message)

    def test28(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '28'
        authorization.amount = 15000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "5194560012341234"
        card.expDate = "1212"
        card.type = 'MC'
        authorization.card = card
        
        authorization.allowPartialAuth = True
        healthcareiias = litleXmlFields.healthcareIIAS()
        healthcareamounts = litleXmlFields.healthcareAmounts()
        healthcareamounts.totalHealthcareAmount = 15000
        healthcareamounts.RxAmount = 3698
        healthcareiias.healthcareAmounts = healthcareamounts
        healthcareiias.IIASFlag = 'Y'
        authorization.healthcareIIAS = healthcareiias
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
#       
    def test29(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '29'
        authorization.amount = 18699
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "4024720001231239"
        card.expDate = "1212"
        card.type = 'VI'
        authorization.card = card
        
        authorization.allowPartialAuth = True
        healthcareiias = litleXmlFields.healthcareIIAS()
        healthcareamounts = litleXmlFields.healthcareAmounts()
        healthcareamounts.totalHealthcareAmount = 31000
        healthcareamounts.RxAmount = 1000
        healthcareamounts.visionAmount = 19901
        healthcareamounts.clinicOtherAmount = 9050
        healthcareamounts.dentalAmount = 1049
        healthcareiias.healthcareAmounts = healthcareamounts
        healthcareiias.IIASFlag = 'Y'
        authorization.healthcareIIAS = healthcareiias
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals("341",response.transactionResponse.response)
        self.assertEquals("Invalid healthcare amounts",response.transactionResponse.message)

    def test30(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '30'
        authorization.amount = 20000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "4024720001231239"
        card.expDate = "1212"
        card.type = 'VI'
        authorization.card = card
        
        authorization.allowPartialAuth = True
        healthcareiias = litleXmlFields.healthcareIIAS()
        healthcareamounts = litleXmlFields.healthcareAmounts()
        healthcareamounts.totalHealthcareAmount = 20000
        healthcareamounts.RxAmount = 1000
        healthcareamounts.visionAmount = 19901
        healthcareamounts.clinicOtherAmount = 9050
        healthcareamounts.dentalAmount = 1049
        healthcareiias.healthcareAmounts = healthcareamounts
        healthcareiias.IIASFlag = 'Y'
        authorization.healthcareIIAS = healthcareiias
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals("341",response.transactionResponse.response)
        self.assertEquals("Invalid healthcare amounts",response.transactionResponse.message)

    def test31(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '31'
        authorization.amount = 25000
        authorization.orderSource = 'ecommerce'
        card = litleXmlFields.cardType()
        card.number = "4024720001231239"
        card.expDate = "1212"
        card.type = 'VI'
        authorization.card = card
        
        authorization.allowPartialAuth = True
        healthcareiias = litleXmlFields.healthcareIIAS()
        healthcareamounts = litleXmlFields.healthcareAmounts()
        healthcareamounts.totalHealthcareAmount = 18699
        healthcareamounts.RxAmount = 1000
        healthcareamounts.visionAmount = 15099
        healthcareiias.healthcareAmounts = healthcareamounts
        healthcareiias.IIASFlag = 'Y'
        authorization.healthcareIIAS = healthcareiias
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals("010",response.transactionResponse.response)
        self.assertEquals("Partially Approved",response.transactionResponse.message)
        self.assertEquals(18699, response.transactionResponse.approvedAmount)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(certTest2)
    return suite