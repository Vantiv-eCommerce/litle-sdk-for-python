from SetupTest import *
import unittest

class certTest1(unittest.TestCase):
    
    def test1_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1'
        authorization.amount = 10010
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="John Smith"
        contact.addressLine1="1 Main St."
        contact.city="Burlington"
        contact.state="MA"
        contact.zip="01803-3747"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "4457010000000009"
        card.expDate = "0112"
        card.cardValidationNum = "349"
        card.type = 'VI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("11111 ",response.transactionResponse.authCode)
        self.assertEquals( "01",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M",response.transactionResponse.fraudResult.cardValidationResult);
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.transactionResponse.response)
        self.assertEquals("Approved",captureresponse.transactionResponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)
        
    def test1_AVS(self):
            
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1'
        authorization.amount = 000
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="John Smith"
        contact.addressLine1="1 Main St."
        contact.city="Burlington"
        contact.state="MA"
        contact.zip="01803-3747"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "4457010000000009"
        card.expDate = "0112"
        card.cardValidationNum = "349"
        card.type = 'VI'

        authorization.card = card
            
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("11111 ",response.transactionResponse.authCode)
        self.assertEquals( "01",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M",response.transactionResponse.fraudResult.cardValidationResult);
        
    def test1_sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '1'
        sale.amount = 10010
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="John Smith"
        contact.addressLine1="1 Main St."
        contact.city="Burlington"
        contact.state="MA"
        contact.zip="01803-3747"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "4457010000000009"
        card.expDate = "0112"
        card.cardValidationNum = "349"
        card.type = 'VI'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("11111 ",response.transactionResponse.authCode)
        self.assertEquals( "01",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M",response.transactionResponse.fraudResult.cardValidationResult);
       
        credit = litleXmlFields.credit()
        credit.litleTxnId = response.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)
        
    def test2_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '2'
        authorization.amount = 20020
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mike J. Hammer"
        contact.addressLine1="2 Main St."
        contact.addressLine2="Apt. 222"
        contact.city="Riverside"
        contact.state="RI"
        contact.zip="02915"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010000000003"
        card.expDate = "0212"
        card.cardValidationNum = "261"
        card.type = 'MC'

        authorization.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("22222",response.transactionResponse.authCode)
        self.assertEquals( "10",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M",response.transactionResponse.fraudResult.cardValidationResult);
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.transactionResponse.response)
        self.assertEquals("Approved",captureresponse.transactionResponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)
        
        
    def test2_AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '2'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mike J. Hammer"
        contact.addressLine1="2 Main St."
        contact.addressLine2="Apt. 222"
        contact.city="Riverside"
        contact.state="RI"
        contact.zip="02915"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010000000003"
        card.expDate = "0212"
        card.cardValidationNum = "261"
        card.type = 'MC'

        authorization.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("22222",response.transactionResponse.authCode)
        self.assertEquals( "10",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M",response.transactionResponse.fraudResult.cardValidationResult);

        
    def test2_sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '2'
        sale.amount = 20020
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mike J. Hammer"
        contact.addressLine1="2 Main St."
        contact.addressLine2="Apt. 222"
        contact.city="Riverside"
        contact.state="RI"
        contact.zip="02915"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010000000003"
        card.expDate = "0212"
        card.cardValidationNum = "261"
        card.type = 'MC'

        sale.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        sale.fraudCheck = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("22222",response.transactionResponse.authCode)
        self.assertEquals( "10",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M",response.transactionResponse.fraudResult.cardValidationResult);
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = response.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)    
        
        
    def test3_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '3'
        authorization.amount = 30030
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Eileen Jones"
        contact.addressLine1="3 Main St."
        contact.city="Bloomfield"
        contact.state="CT"
        contact.zip="06002"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010000000003"
        card.expDate = "0312"
        card.cardValidationNum = "758"
        card.type = 'DI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("33333",response.transactionResponse.authCode)
        self.assertEquals( "10",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M",response.transactionResponse.fraudResult.cardValidationResult);
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.transactionResponse.response)
        self.assertEquals("Approved",captureresponse.transactionResponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)
        
        
    def test3_AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '3'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Eileen Jones"
        contact.addressLine1="3 Main St."
        contact.city="Bloomfield"
        contact.state="CT"
        contact.zip="06002"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010000000003"
        card.expDate = "0312"
        card.cardValidationNum = "758"
        card.type = 'DI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("33333",response.transactionResponse.authCode)
        self.assertEquals( "10",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M",response.transactionResponse.fraudResult.cardValidationResult);
        
    def test3_sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '3'
        sale.amount = 30030
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Eileen Jones"
        contact.addressLine1="3 Main St."
        contact.city="Bloomfield"
        contact.state="CT"
        contact.zip="06002"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010000000003"
        card.expDate = "0312"
        card.cardValidationNum = "758"
        card.type = 'DI'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("33333",response.transactionResponse.authCode)
        self.assertEquals( "10",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("M",response.transactionResponse.fraudResult.cardValidationResult);
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = response.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)
        
        
    def test4_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '4'
        authorization.amount = 40040
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Bob Black"
        contact.addressLine1="4 Main St."
        contact.city="Laurel"
        contact.state="MD"
        contact.zip="20708"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001000000005"
        card.expDate = "0412"
        card.cardValidationNum = "758"
        card.type = 'AX'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("44444",response.transactionResponse.authCode)
        self.assertEquals( "12",response.transactionResponse.fraudResult.avsResult)
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.transactionResponse.response)
        self.assertEquals("Approved",captureresponse.transactionResponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)
        
        
    def test4_AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '4'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Bob Black"
        contact.addressLine1="4 Main St."
        contact.city="Laurel"
        contact.state="MD"
        contact.zip="20708"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001000000005"
        card.expDate = "0412"
        card.cardValidationNum = "758"
        card.type = 'AX'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("44444",response.transactionResponse.authCode)
        self.assertEquals( "12",response.transactionResponse.fraudResult.avsResult)
        
        
    def test4_sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '4'
        sale.amount = 40040
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Bob Black"
        contact.addressLine1="4 Main St."
        contact.city="Laurel"
        contact.state="MD"
        contact.zip="20708"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001000000005"
        card.expDate = "0412"
        card.cardValidationNum = "758"
        card.type = 'AX'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("44444",response.transactionResponse.authCode)
        self.assertEquals( "12",response.transactionResponse.fraudResult.avsResult)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = response.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)
        
        
    def test5_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '5'
        authorization.amount = 50050
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4457010200000007"
        card.expDate = "0512"
        card.cardValidationNum = "463"
        card.type = 'VI'

        authorization.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("55555 ",response.transactionResponse.authCode)
        self.assertEquals( "32",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("N",response.transactionResponse.fraudResult.cardValidationResult);
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.transactionResponse.response)
        self.assertEquals("Approved",captureresponse.transactionResponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)
        
        
    def test5_AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '5'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4457010200000007"
        card.expDate = "0512"
        card.cardValidationNum = "463"
        card.type = 'VI'

        authorization.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("55555 ",response.transactionResponse.authCode)
        self.assertEquals( "32",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("N",response.transactionResponse.fraudResult.cardValidationResult);
        
        
    def test5_sale(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '5'
        authorization.amount = 50050
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4457010200000007"
        card.expDate = "0512"
        card.cardValidationNum = "463"
        card.type = 'VI'

        authorization.card = card
        
        authenticationvalue = litleXmlFields.fraudCheckType()
        authenticationvalue.authenticationValue= "BwABBJQ1AgAAAAAgJDUCAAAAAAA="
        authorization.cardholderAuthentication = authenticationvalue
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "000",response.transactionResponse.response)
        self.assertEquals("Approved",response.transactionResponse.message)
        self.assertEquals("55555 ",response.transactionResponse.authCode)
        self.assertEquals( "32",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("N",response.transactionResponse.fraudResult.cardValidationResult);
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = response.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)
        
        
    def test6_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '6'
        authorization.amount = 60060
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Joe Green"
        contact.addressLine1="6 Main St."
        contact.city="Derry"
        contact.state="NH"
        contact.zip="03038"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "4457010100000008"
        card.expDate = "0612"
        card.cardValidationNum = "992"
        card.type = 'VI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "110",response.transactionResponse.response)
        self.assertEquals("Insufficient Funds",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("P",response.transactionResponse.fraudResult.cardValidationResult);
        
        capture = litleXmlFields.capture()
        capture.litleTxnId = response.transactionResponse.litleTxnId
        captureresponse = litleXml.sendRequest(capture)
        self.assertEquals( "000",captureresponse.transactionResponse.response)
        self.assertEquals("Approved",captureresponse.transactionResponse.message)
        
        credit = litleXmlFields.credit()
        credit.litleTxnId = captureresponse.transactionResponse.litleTxnId
        creditresponse = litleXml.sendRequest(credit)
        self.assertEquals( "000",creditresponse.transactionResponse.response)
        self.assertEquals("Approved",creditresponse.transactionResponse.message)
        
        void = litleXmlFields.void()
        void.litleTxnId = creditresponse.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "000",voidresponse.transactionResponse.response)
        self.assertEquals("Approved",voidresponse.transactionResponse.message)
        
        
    def test6_sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '6'
        sale.amount = 60060
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Joe Green"
        contact.addressLine1="6 Main St."
        contact.city="Derry"
        contact.state="NH"
        contact.zip="03038"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "4457010100000008"
        card.expDate = "0612"
        card.cardValidationNum = "992"
        card.type = 'VI'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "110",response.transactionResponse.response)
        self.assertEquals("Insufficient Funds",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("P",response.transactionResponse.fraudResult.cardValidationResult);
        
        void = litleXmlFields.void()
        void.litleTxnId = response.transactionResponse.litleTxnId
        voidresponse = litleXml.sendRequest(void)
        self.assertEquals( "360",voidresponse.transactionResponse.response)
        self.assertEquals("No transaction found with specified litleTxnId",voidresponse.transactionResponse.message)
        
        
    def test7_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '7'
        authorization.amount = 70070
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Jane Murray"
        contact.addressLine1="7 Main St."
        contact.city="Amesbury"
        contact.state="MA"
        contact.zip="01913"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010100000002"
        card.expDate = "0712"
        card.cardValidationNum = "251"
        card.type = 'MC'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "301",response.transactionResponse.response)
        self.assertEquals("Invalid Account Number",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("N",response.transactionResponse.fraudResult.cardValidationResult);
        
        
    def test7_AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '7'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Jane Murray"
        contact.addressLine1="7 Main St."
        contact.city="Amesbury"
        contact.state="MA"
        contact.zip="01913"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010100000002"
        card.expDate = "0712"
        card.cardValidationNum = "251"
        card.type = 'MC'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "301",response.transactionResponse.response)
        self.assertEquals("Invalid Account Number",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("N",response.transactionResponse.fraudResult.cardValidationResult);
        
        
    def test7_sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '7'
        sale.amount = 70070
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Jane Murray"
        contact.addressLine1="7 Main St."
        contact.city="Amesbury"
        contact.state="MA"
        contact.zip="01913"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "5112010100000002"
        card.expDate = "0712"
        card.cardValidationNum = "251"
        card.type = 'MC'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "301",response.transactionResponse.response)
        self.assertEquals("Invalid Account Number",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("N",response.transactionResponse.fraudResult.cardValidationResult);
        
        
    def test8_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '8'
        authorization.amount = 80080
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mark Johnson"
        contact.addressLine1="8 Main St."
        contact.city="Manchester"
        contact.state="NH"
        contact.zip="03101"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010100000002"
        card.expDate = "0812"
        card.cardValidationNum = "184"
        card.type = 'DI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "123",response.transactionResponse.response)
        self.assertEquals("Call Discover",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("P",response.transactionResponse.fraudResult.cardValidationResult);
        
        
    def test8_AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '8'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mark Johnson"
        contact.addressLine1="8 Main St."
        contact.city="Manchester"
        contact.state="NH"
        contact.zip="03101"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010100000002"
        card.expDate = "0812"
        card.cardValidationNum = "184"
        card.type = 'DI'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "123",response.transactionResponse.response)
        self.assertEquals("Call Discover",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("P",response.transactionResponse.fraudResult.cardValidationResult);
        
        
    def test8_sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '8'
        sale.amount = 80080
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="Mark Johnson"
        contact.addressLine1="8 Main St."
        contact.city="Manchester"
        contact.state="NH"
        contact.zip="03101"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "6011010100000002"
        card.expDate = "0812"
        card.cardValidationNum = "184"
        card.type = 'DI'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "123",response.transactionResponse.response)
        self.assertEquals("Call Discover",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        self.assertEquals("P",response.transactionResponse.fraudResult.cardValidationResult);
        
        
    def test9_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '9'
        authorization.amount = 90090
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="James Miller"
        contact.addressLine1="9 Main St."
        contact.city="Boston"
        contact.state="MA"
        contact.zip="02134"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001010000003"
        card.expDate = "0912"
        card.cardValidationNum = "0421"
        card.type = 'AX'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "303",response.transactionResponse.response)
        self.assertEquals("Pick Up Card",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        
        
    def test9_AVS(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '9'
        authorization.amount = 0
        authorization.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="James Miller"
        contact.addressLine1="9 Main St."
        contact.city="Boston"
        contact.state="MA"
        contact.zip="02134"
        contact.country="USA"
        authorization.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001010000003"
        card.expDate = "0912"
        card.cardValidationNum = "0421"
        card.type = 'AX'

        authorization.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "303",response.transactionResponse.response)
        self.assertEquals("Pick Up Card",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        
        
    def test9_sale(self):
        
        sale = litleXmlFields.sale()
        sale.orderId = '9'
        sale.amount = 90090
        sale.orderSource = 'ecommerce'
        
        contact = litleXmlFields.contact();
        contact.name="James Miller"
        contact.addressLine1="9 Main St."
        contact.city="Boston"
        contact.state="MA"
        contact.zip="02134"
        contact.country="USA"
        sale.billToAddress = contact
        
        card = litleXmlFields.cardType()
        card.number = "375001010000003"
        card.expDate = "0912"
        card.cardValidationNum = "0421"
        card.type = 'AX'

        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEquals( "303",response.transactionResponse.response)
        self.assertEquals("Pick Up Card",response.transactionResponse.message)
        self.assertEquals( "34",response.transactionResponse.fraudResult.avsResult)
        
        
    def test10_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '10'
        authorization.amount = 40000
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4457010140000141"
        card.expDate = "0912"
        card.type = 'VI'

        authorization.card = card
        
        authorization.allowPartialAuth = True
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "010",response.transactionResponse.response)
        self.assertEquals("Partially Approved",response.transactionResponse.message)
        self.assertEquals( 32000L,response.transactionResponse.approvedAmount)
        
        
    def test11_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '11'
        authorization.amount = 60000
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "5112010140000004"
        card.expDate = "1111"
        card.type = 'MC'

        authorization.card = card
        
        authorization.allowPartialAuth = True
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "010",response.transactionResponse.response)
        self.assertEquals("Partially Approved",response.transactionResponse.message)
        self.assertEquals( 48000L,response.transactionResponse.approvedAmount)
        
        
    def test12_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '12'
        authorization.amount = 50000
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "375001014000009"
        card.expDate = "0412"
        card.type = 'AX'

        authorization.card = card
        
        authorization.allowPartialAuth = True
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "010",response.transactionResponse.response)
        self.assertEquals("Partially Approved",response.transactionResponse.message)
        self.assertEquals( 40000L,response.transactionResponse.approvedAmount)
        
    
    def test13_auth(self):
        
        authorization = litleXmlFields.authorization()
        authorization.orderId = '13'
        authorization.amount = 15000
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "6011010140000004"
        card.expDate = "0812"
        card.type = 'DI'

        authorization.card = card
        
        authorization.allowPartialAuth = True
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(authorization)
        self.assertEquals( "010",response.transactionResponse.response)
        self.assertEquals("Partially Approved",response.transactionResponse.message)
        self.assertEquals( 12000L,response.transactionResponse.approvedAmount)
        
def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(certTest1)
    return suite