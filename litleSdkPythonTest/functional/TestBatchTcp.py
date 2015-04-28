# Copyright (c) 2011-2014 Litle & Co.
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE lUSE OR
# OTHER DEALINGS IN THE SOFTWARE.

import os, sys
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest
import tempfile
import shutil
import copy

class TestBatchTcp(unittest.TestCase):
    def setUp(self):
        self.merchantId = '0180'


    def testSendToLitle_WithFileConfig(self):
        requestFileName = "litleSdk-testBatchFile-fileConfig.xml"
        request = litleBatchFileRequest(requestFileName)
        self.assertTrue(os.path.exists(request.requestFile.name))
        configFromFile = request.config
        self.assertEqual('prelive.litle.com', configFromFile.batchHost)
        self.assertEqual('15000', configFromFile.batchPort)
        self.prepareTestRequest(request)
        response = request.sendRequestTCP()
        self.assertPythonApi(request, response)
        requestDir = configFromFile.batchRequestFolder
        responseDir = configFromFile.batchResponseFolder
        self.assertGeneratedFiles(requestDir, responseDir, requestFileName, request)

    def testSendToLitle_WithConfigOverrides(self):
        requestDir = tempfile.gettempdir() + '/' + 'request'
        responseDir = tempfile.gettempdir() + '/' + 'response'

        configOverrides = Configuration()
        configOverrides.batchHost = 'prelive.litle.com'
        configOverrides.batchPort = '15000'
        configOverrides.batchRequestFolder = requestDir
        configOverrides.batchResponseFolder = responseDir

        requestFileName = "litleSdk-testBatchFile-fileConfig.xml"
        request = litleBatchFileRequest(requestFileName, configOverrides)
        self.assertTrue(os.path.exists(request.requestFile.name))
        self.prepareTestRequest(request)
        response = request.sendRequestTCP()
        self.assertPythonApi(request, response)
        self.assertGeneratedFiles(requestDir, responseDir, requestFileName, request)

    def testMechantBatchAndProcess(self):          
        requestFileName = "litleSdk-testBatchFile-MECHA.xml"
        
        for i in range(0, 3):
            request = litleBatchFileRequest(requestFileName)

            configFromFile = request.config
            self.assertEqual('prelive.litle.com', configFromFile.batchHost)
            self.assertEqual('15000', configFromFile.batchPort)     
             
            batch = request.createBatch()
            # card
            card = litleXmlFields.cardType()
            card.number = '4100000000000001'
            card.expDate = '1210'
            card.type = 'VI'
     
            # echeck
            echeck = litleXmlFields.echeck()
            echeck.accNum = '1092969901'
            echeck.accType = 'Corporate'
            echeck.routingNum = '011075150'
     
            # billto address
            contact = litleXmlFields.contact()
            contact.name = 'PreNote Sale Corporate'
            contact.firstName = 'unavailable'
            contact.lastName = 'unavailable'
            contact.companyName = 'PreNote Sale Corporate'
            contact.addressLine1 = '1 Lowell Street'
            contact.addressLine2 = 'Tower 2'
            contact.city = 'lowell'
            contact.state = 'MA'
            contact.zip = '01850'
            contact.phone = '1234567890'
            contact.email = 'Bob@litle.com'
     
            # auth
            auth = litleXmlFields.authorization()
            auth.reportGroup = 'Planets'
            auth.orderId = '12344'
            auth.amount = 106
            auth.orderSource = 'ecommerce'
            auth.card = card
     
            batch.addTransaction(auth)
     
            sale = litleXmlFields.sale()
            sale.reportGroup = 'Planets'
            sale.orderId = '12344'
            sale.amount = 6000
            sale.orderSource = 'ecommerce'
            sale.card = card
     
            batch.addTransaction(sale)
     
            credit = litleXmlFields.credit()
            credit.reportGroup = 'Planets'
            credit.orderId = '12344'
            credit.amount = 106
            credit.orderSource = 'ecommerce'
            credit.card = card
     
            batch.addTransaction(credit)
     
            authReversal = litleXmlFields.authReversal()
            authReversal.reportGroup = 'Planets'
            authReversal.litleTxnId = 12345678000
            authReversal.amount = 106
            authReversal.payPalNotes = 'Notes'
     
            batch.addTransaction(authReversal)
     
            registerTokenRequestType = litleXmlFields.registerTokenRequest()
            registerTokenRequestType.reportGroup = 'Planets'
            registerTokenRequestType.orderId = '12344'
            registerTokenRequestType.accountNumber = '1233456789103801'
     
            batch.addTransaction(registerTokenRequestType)
     
            cardValidationNumOnToken = litleXmlFields.updateCardValidationNumOnToken()
            cardValidationNumOnToken.reportGroup = 'Planets'
            cardValidationNumOnToken.id = '12345'
            cardValidationNumOnToken.customerId = '0987'
            cardValidationNumOnToken.orderId = '12344'
            cardValidationNumOnToken.litleToken = '1233456789103801'
            cardValidationNumOnToken.cardValidationNum = '123'
     
            batch.addTransaction(cardValidationNumOnToken)
     
            forceCapture = litleXmlFields.forceCapture()
            forceCapture.reportGroup = 'Planets'
            forceCapture.id = '123456'
            forceCapture.orderId = '12344'
            forceCapture.amount = 106
            forceCapture.orderSource = 'ecommerce'
            forceCapture.card = card
     
            batch.addTransaction(forceCapture)
     
            capture = litleXmlFields.capture()
            capture.reportGroup = 'Planets'
            capture.litleTxnId = 123456000
            capture.amount = 106
     
            batch.addTransaction(capture)
     
            captureGivenAuth = litleXmlFields.captureGivenAuth()
            captureGivenAuth.reportGroup = 'Planets'
            captureGivenAuth.orderId = '12344'
            captureGivenAuth.amount = 106
            authInformation = litleXmlFields.authInformation()
            authInformation.authDate = pyxb.binding.datatypes.date(2002, 10, 9)
            authInformation.authAmount = 12345
            authInformation.authCode = '543216'
            captureGivenAuth.authInformation = authInformation
            captureGivenAuth.orderSource = 'ecommerce'
            captureGivenAuth.card = card
     
            batch.addTransaction(captureGivenAuth)
     
            echeckVerification = litleXmlFields.echeckVerification()
            echeckVerification.reportGroup = 'Planets'
            echeckVerification.amount = 123456
            echeckVerification.orderId = '12345'
            echeckVerification.orderSource = 'ecommerce'
            echeckVerification.billToAddress = contact
            echeckVerification.echeckOrEcheckToken = echeck
     
            batch.addTransaction(echeckVerification)
     
            echeckCredit = litleXmlFields.echeckCredit()
            echeckCredit.reportGroup = 'Planets'
            echeckCredit.litleTxnId = 1234567890
            echeckCredit.amount = 12
     
            batch.addTransaction(echeckCredit)
     
            echeckRedeposit = litleXmlFields.echeckRedeposit()
            echeckRedeposit.reportGroup = 'Planets'
            echeckRedeposit.litleTxnId = 124321341412
     
            batch.addTransaction(echeckRedeposit)
     
            echeckSale = litleXmlFields.echeckSale()
            echeckSale.reportGroup = 'Planets'
            echeckSale.amount = 123456
            echeckSale.orderId = '12345'
            echeckSale.orderSource = 'ecommerce'
            echeckSale.billToAddress = contact
            echeckSale.echeckOrEcheckToken = echeck
            echeckSale.verify = True
     
            batch.addTransaction(echeckSale)
            echeckPreNoteSale = litleXmlFields.echeckPreNoteSale();
            echeckPreNoteSale.orderId = "12344"
            echeckPreNoteSale.billToAddress = contact
            echeckPreNoteSale.echeck = echeck
            echeckPreNoteSale.orderSource = 'ecommerce'
    
            transactionCount = batch.numOfTxn
            fileResponse = request.sendRequestTCP()
            batchResponse = fileResponse.getNextBatchResponse()
            
            txns = 0
      
            nextTransaction = True
            while nextTransaction:
                try:
                    batchResponse.getNextTransaction()
                    txns += 1
                except:
                    nextTransaction = False
            if txns == transactionCount:
                break
        self.assertEqual(transactionCount, txns)

    def testGiftCardTransactions(self):
        requestFileName = "litleSdk-testBatchFile-GIFTCARD.xml"
        request = litleBatchFileRequest(requestFileName)
        configFromFile = request.config
        self.assertEqual('prelive.litle.com', configFromFile.batchHost)
        self.assertEqual('15000', configFromFile.batchPort)
        batch = request.createBatch()

        giftCard = litleXmlFields.cardType()
        giftCard.type = 'GC'
        giftCard.expDate = '1218'
        giftCard.number = '4100000000000001'

        activate = litleXmlFields.activate()
        activate.reportGroup = 'Planets'
        activate.orderSource = 'ecommerce'
        activate.amount = 100
        activate.orderId = 'abc'
        activate.card = giftCard

        batch.addTransaction(activate)

        deactivate = litleXmlFields.deactivate()
        deactivate.reportGroup = 'Planets'
        deactivate.orderId = 'def'
        deactivate.orderSource = 'ecommerce'
        deactivate.card = giftCard

        batch.addTransaction(deactivate)

        load = litleXmlFields.load()
        load.reportGroup = 'Planets'
        load.orderId = 'ghi'
        load.amount = 100
        load.orderSource = 'ecommerce'
        load.card = giftCard

        batch.addTransaction(load)

        unload = litleXmlFields.unload()
        unload.reportGroup = 'Planets'
        unload.orderId = 'jkl'
        unload.amount = 100
        unload.orderSource = 'ecommerce'
        unload.card = giftCard

        batch.addTransaction(unload)

        balanceInquiry = litleXmlFields.balanceInquiry()
        balanceInquiry.reportGroup = 'Planets'
        balanceInquiry.orderId = 'mno'
        balanceInquiry.orderSource = 'ecommerce'
        balanceInquiry.card = giftCard

        batch.addTransaction(balanceInquiry)

        fileResponse = request.sendRequestTCP()
        batchResponse = fileResponse.getNextBatchResponse()

        txns = 0

        nextTransaction = True
        while nextTransaction:
            try:
                txn = batchResponse.getNextTransaction()
                self.assertNotEqual(None, txn.litleTxnId)
                txns += 1
            except NoTransactionException:
                nextTransaction = False

        self.assertEqual(5, txns)

    def testMechaBatchAndProcess_Recurring(self):
        requestFileName = "litleSdk-testBatchFile-RECURRING.xml"
        request = litleBatchFileRequest(requestFileName)
        configFromFile = request.config
        self.assertEqual('prelive.litle.com', configFromFile.batchHost)
        self.assertEqual('15000', configFromFile.batchPort)

        batch = request.createBatch()
        cancelSubscription = litleXmlFields.cancelSubscription()
        cancelSubscription.subscriptionId = 12345
        batch.addTransaction(cancelSubscription)

        updateSubscription = litleXmlFields.updateSubscription()
        updateSubscription.subscriptionId = 12345
        batch.addTransaction(updateSubscription)

        createPlan = litleXmlFields.createPlan()
        createPlan.planCode = 'abc'
        createPlan.name = 'name'
        createPlan.intervalType = 'ANNUAL'
        createPlan.amount = 100
        batch.addTransaction(createPlan)

        updatePlan = litleXmlFields.updatePlan()
        updatePlan.planCode = 'def'
        updatePlan.active = True
        batch.addTransaction(updatePlan)

        fileResponse = request.sendRequestTCP()
        batchResponse = fileResponse.getNextBatchResponse()

        txns = 0

        nextTransaction = True
        while nextTransaction:
            try:
                txn = batchResponse.getNextTransaction()
                if isinstance(txn, litleXmlFields.updateSubscriptionResponse.typeDefinition()):
                    self.assertEqual(12345, txn.subscriptionId)
                elif isinstance(txn, litleXmlFields.cancelSubscriptionResponse.typeDefinition()):
                    self.assertEqual(12345, txn.subscriptionId)
                elif isinstance(txn, litleXmlFields.createPlanResponse.typeDefinition()):
                    self.assertEqual('abc', txn.planCode)
                elif isinstance(txn, litleXmlFields.createPlanResponse.typeDefinition()):
                    self.assertEqual('def', txn.planCode)

                txns += 1
            except NoTransactionException:
                nextTransaction = False

        self.assertEqual(4, txns)

    def testBatch_AU(self):
        requestFileName = "litleSdk-testBatchFile-AU.xml"
        request = litleBatchFileRequest(requestFileName)
        configFromFile = request.config
        self.assertEqual('prelive.litle.com', configFromFile.batchHost)
        self.assertEqual('15000', configFromFile.batchPort)
        batch = request.createBatch()

        # card
        card = litleXmlFields.card()
        card.number = '4100000000000001'
        card.expDate = '1210'
        card.type = 'VI'

        accountUpdate = litleXmlFields.accountUpdate()
        accountUpdate.reportGroup = 'Planets'
        accountUpdate.id = '12345'
        accountUpdate.customerId = '0987'
        accountUpdate.orderId = '1234'
        accountUpdate.cardOrToken = card

        batch.addTransaction(accountUpdate)

        fileResponse = request.sendRequestTCP()
        batchResponse = fileResponse.getNextBatchResponse()

        txns = 0

        nextTransaction = True

        while nextTransaction:
            try:
                txn = batchResponse.getNextTransaction()
                self.assertEqual('Planets', txn.reportGroup)
                self.assertEqual('12345', txn.id)
                self.assertEqual('0987', txn.customerId)
                self.assertEqual('1234', txn.orderId)
                txns += 1
            except NoTransactionException:
                nextTransaction = False

        self.assertEqual(1, txns)
        
    def testEcheckPreNoteAll(self):
        requestFileName = "litleSdk-testBatchFile-EchecPreNoteAll.xml"
        request = litleBatchFileRequest(requestFileName)

        configFromFile = request.config
        self.assertEqual('prelive.litle.com', configFromFile.batchHost)
        self.assertEqual('15000', configFromFile.batchPort)

        batch = request.createBatch()
 
        # echeckSuccess
        echeckSuccess = litleXmlFields.echeck()
        echeckSuccess.accNum = '1092969901'
        echeckSuccess.accType = 'Corporate'
        echeckSuccess.routingNum = '011075150'
        
        # echeckErr1
        echeckRoutErr = litleXmlFields.echeck()
        echeckRoutErr.accNum = '6099999992'
        echeckRoutErr.accType = 'Checking'
        echeckRoutErr.routingNum = '053133052'
        
        # echeckErr2l
        echeckAccErr = litleXmlFields.echeck()
        echeckAccErr.accNum = '10@2969901'
        echeckAccErr.accType = 'Savings'
        echeckAccErr.routingNum = '011100012'
 
        # billto address
        contact = litleXmlFields.contact()
        contact.name = 'PreNote Sale Corporate'
        contact.firstName = 'unavailable'
        contact.lastName = 'unavailable'
        contact.companyName = 'PreNote Sale Corporate'
        contact.addressLine1 = '1 Lowell Street'
        contact.addressLine2 = 'Tower 2'
        contact.city = 'lowell'
        contact.state = 'MA'
        contact.zip = '01850'
        contact.phone = '1234567890'
        contact.email = 'Bob@litle.com'

        echeckPreNoteSale = litleXmlFields.echeckPreNoteSale();
        echeckPreNoteSale.orderId = "000"
        echeckPreNoteSale.billToAddress = contact
        echeckPreNoteSale.echeck = echeckSuccess
        echeckPreNoteSale.orderSource = 'ecommerce'           
        batch.addTransaction(echeckPreNoteSale)
        
        echeckPreNoteCredit = litleXmlFields.echeckPreNoteCredit();
        echeckPreNoteCredit.orderId = "000"
        echeckPreNoteCredit.billToAddress = contact
        echeckPreNoteCredit.echeck = echeckSuccess
        echeckPreNoteCredit.orderSource = 'ecommerce'         
        batch.addTransaction(echeckPreNoteCredit)
        
        echeckPreNoteSale = litleXmlFields.echeckPreNoteSale();
        echeckPreNoteSale.orderId = "900"
        echeckPreNoteSale.billToAddress = contact
        echeckPreNoteSale.echeck = echeckRoutErr
        echeckPreNoteSale.orderSource = 'ecommerce'           
        batch.addTransaction(echeckPreNoteSale)
        
        echeckPreNoteCredit = litleXmlFields.echeckPreNoteCredit();
        echeckPreNoteCredit.orderId = "900"
        echeckPreNoteCredit.billToAddress = contact
        echeckPreNoteCredit.echeck = echeckRoutErr
        echeckPreNoteCredit.orderSource = 'ecommerce'         
        batch.addTransaction(echeckPreNoteCredit)
        
        echeckPreNoteSale = litleXmlFields.echeckPreNoteSale();
        echeckPreNoteSale.orderId = "301"
        echeckPreNoteSale.billToAddress = contact
        echeckPreNoteSale.echeck = echeckAccErr
        echeckPreNoteSale.orderSource = 'ecommerce'           
        batch.addTransaction(echeckPreNoteSale)
        
        echeckPreNoteCredit = litleXmlFields.echeckPreNoteCredit();
        echeckPreNoteCredit.orderId = "301"
        echeckPreNoteCredit.billToAddress = contact
        echeckPreNoteCredit.echeck = echeckAccErr
        echeckPreNoteCredit.orderSource = 'ecommerce'         
        batch.addTransaction(echeckPreNoteCredit)
 
        transactionCount = batch.numOfTxn
 
        fileResponse = request.sendRequestTCP()
        batchResponse = fileResponse.getNextBatchResponse()
 
        txns = 0

        nextTransaction = True
        
        while nextTransaction:
            try:
                responseTxn = batchResponse.getNextTransaction()
                self.assertEqual(responseTxn.response, responseTxn.orderId)
                txns += 1;
            except NoTransactionException:
                nextTransaction = False

        self.assertEqual(transactionCount, txns)
        
    def testPFIFInstructionTxn(self):
        requestFileName = "litleSdk-testBatchFile-PFIF.xml"
        request = litleBatchFileRequest(requestFileName)

        configFromFile = request.config
        self.assertEqual('prelive.litle.com', configFromFile.batchHost)
        self.assertEqual('15000', configFromFile.batchPort)

        batch = request.createBatch()

        # echeck
        echeck = litleXmlFields.echeck()
        echeck.accNum = '1092969901'
        echeck.accType = 'Corporate'
        echeck.routingNum = '011075150'

        submerchantCredit = litleXmlFields.submerchantCredit();        
        submerchantCredit.fundingSubmerchantId = "12347"
        submerchantCredit.submerchantName = "001"
        submerchantCredit.fundsTransferId = "123456"
        submerchantCredit.amount = "100"
        submerchantCredit.accountInfo = echeck             
        batch.addTransaction(submerchantCredit)

        submerchantDebit = litleXmlFields.submerchantDebit();        
        submerchantDebit.fundingSubmerchantId = "12347"
        submerchantDebit.submerchantName = "001"
        submerchantDebit.fundsTransferId = "123456"
        submerchantDebit.amount = "100"
        submerchantDebit.accountInfo = echeck          
        batch.addTransaction(submerchantDebit)
           
        payFacCredit = litleXmlFields.payFacCredit();        
        payFacCredit.fundingSubmerchantId = "12347"
        payFacCredit.fundsTransferId = "123456"
        payFacCredit.amount = "100"           
        batch.addTransaction(payFacCredit)
           
        payFacDebit = litleXmlFields.payFacDebit();        
        payFacDebit.fundingSubmerchantId = "12347"
        payFacDebit.fundsTransferId = "123456"
        payFacDebit.amount = "100"           
        batch.addTransaction(payFacDebit)
           
        reserveCredit = litleXmlFields.reserveCredit();        
        reserveCredit.fundingSubmerchantId = "12347"
        reserveCredit.fundsTransferId = "123456"
        reserveCredit.amount = "100"           
        batch.addTransaction(reserveCredit)
           
        reserveDebit = litleXmlFields.reserveDebit();        
        reserveDebit.fundingSubmerchantId = "12347"
        reserveDebit.fundsTransferId = "123456"
        reserveDebit.amount = "100"           
        batch.addTransaction(reserveDebit)        

        vendorCredit = litleXmlFields.vendorCredit();        
        vendorCredit.fundingSubmerchantId = "12347"
        vendorCredit.vendorName = "001"
        vendorCredit.fundsTransferId = "123456"
        vendorCredit.amount = "100"
        vendorCredit.accountInfo = echeck           
        batch.addTransaction(vendorCredit)

        vendorDebit = litleXmlFields.vendorDebit();        
        vendorDebit.fundingSubmerchantId = "12347"
        vendorDebit.vendorName = "001"
        vendorDebit.fundsTransferId = "123456"
        vendorDebit.amount = "100"
        vendorDebit.accountInfo = echeck           
        batch.addTransaction(vendorDebit)
           
        physicalCheckCredit = litleXmlFields.physicalCheckCredit();        
        physicalCheckCredit.fundingSubmerchantId = "12347"
        physicalCheckCredit.fundsTransferId = "123456"
        physicalCheckCredit.amount = "100"           
        batch.addTransaction(physicalCheckCredit)
           
        physicalCheckDebit = litleXmlFields.physicalCheckDebit();        
        physicalCheckDebit.fundingSubmerchantId = "12347"
        physicalCheckDebit.fundsTransferId = "123456"
        physicalCheckDebit.amount = "100"           
        batch.addTransaction(physicalCheckDebit)

        transactionCount = batch.numOfTxn

        fileResponse = request.sendRequestTCP()
        batchResponse = fileResponse.getNextBatchResponse()

        txns = 0

        nextTransaction = True
        while nextTransaction:
            try:
                batchResponse.getNextTransaction()
                txns += 1
            except:
                nextTransaction = False

        self.assertEqual(transactionCount, txns)   
        

    def assertPythonApi(self, request, response):
        self.assertNotEqual(None, response)
        self.assertNotEqual(None, response.litleResponse.litleSessionId)
        self.assertEqual('0', response.litleResponse.response)
        self.assertEqual('Valid Format', response.litleResponse.message)
        self.assertEqual('9.3', response.litleResponse.version)

        batchResponse = response.getNextBatchResponse()
        self.assertNotEqual(None, response)
        self.assertNotEqual(None, batchResponse.batchResponse.litleBatchId)
        self.assertEqual(self.merchantId, batchResponse.batchResponse.merchantId)

        saleResponse = batchResponse.getNextTransaction()
        self.assertEqual('000', saleResponse.response)
        self.assertEqual('Approved', saleResponse.message)
        self.assertNotEqual(None, saleResponse.litleTxnId)
        self.assertEqual('orderId11', saleResponse.orderId)
        self.assertEqual('reportGroup11', saleResponse.reportGroup)

    def prepareTestRequest(self, request):
        batchRequest = request.createBatch()
        sale = litleXmlFields.sale()
        sale.reportGroup = 'reportGroup11'
        sale.orderId = 'orderId11'
        sale.amount = 1099
        sale.orderSource = 'ecommerce'

        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4457010000000009"
        card.expDate = "0114"
        sale.card = card

        batchRequest.addTransaction(sale)

    def assertGeneratedFiles(self, requestDir, responseDir, requestFileName, request):
        requestPath = requestDir + '/' + requestFileName
        responsePath = responseDir + '/' + requestFileName
        fRequest = os.path.abspath(request.requestFile.name)
        fResponse = os.path.abspath(request.responseFile.name)

        self.assertEqual(requestPath, fRequest)
        self.assertEqual(responsePath, fResponse)
        self.assertTrue(os.path.exists(fRequest))
        self.assertTrue(os.path.exists(fResponse))
        self.assertTrue(os.path.getsize(fRequest) > 0)
        self.assertTrue(os.path.getsize(fResponse) > 0)

        responseFromFile = litleBatchFileResponse(fResponse)
        self.assertPythonApi(request, responseFromFile)


def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBatchTcp)
    return suite

if __name__ == '__main__':
    unittest.main()
