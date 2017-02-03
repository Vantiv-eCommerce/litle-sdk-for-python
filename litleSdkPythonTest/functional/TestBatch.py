#Copyright (c) 2017 Vantiv eCommerce
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

import os, sys
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest
import tempfile
import shutil
import copy

class TestBatch(unittest.TestCase):
    def setUp(self):
        self.merchantId = '0180'


    def testSendToLitleSFTP_WithPreviouslyCreatedFile(self):
        requestFileName = "litleSdk-testBatchFile-testSendToLitleSFTP_WithPreviouslyCreatedFile.xml"
        request = litleBatchFileRequest(requestFileName)
        requestFile = request.requestFile.name
        self.assertTrue(os.path.exists(requestFile))
        configFromFile = request.config
        self.assertEqual('prelive.litle.com', configFromFile.batchHost)
        self.assertEqual('15000', configFromFile.batchPort)
        requestDir = configFromFile.batchRequestFolder
        responseDir = configFromFile.batchResponseFolder
        self.prepareTestRequest(request)
        request.prepareForDelivery()
        self.assertTrue(os.path.exists(requestFile))
        self.assertTrue(os.path.getsize(requestFile) > 0)
        request2 = litleBatchFileRequest(requestFileName)
        response = request2.sendRequestSFTP(True)
        self.assertPythonApi(request2, response)
        self.assertGeneratedFiles(requestDir, responseDir, requestFileName, request2)

    def testSendOnlyToLitleSFTP_WithPreviouslyCreatedFile(self):
        requestFileName = "litleSdk-testBatchFile-testSendOnlyToLitleSFTP_WithPreviouslyCreatedFile.xml"
        request = litleBatchFileRequest(requestFileName)
        requestFile = request.requestFile.name
        self.assertTrue(os.path.exists(requestFile))
        configFromFile = request.config
        self.assertEqual('prelive.litle.com', configFromFile.batchHost)
        self.assertEqual('15000', configFromFile.batchPort)
        requestDir = configFromFile.batchRequestFolder
        responseDir = configFromFile.batchResponseFolder
        self.prepareTestRequest(request)
        request.prepareForDelivery()
        self.assertTrue(os.path.exists(requestFile))
        self.assertTrue(os.path.getsize(requestFile) > 0)

        tempfile.mkdtemp()
        newRequestDir = tempfile.gettempdir() + '/' + 'request'
        if not os.path.exists(newRequestDir):
            os.makedirs(newRequestDir)
        newRequestFileName = 'litle.xml'
        shutil.copyfile(requestFile, newRequestDir + '/' + newRequestFileName)
        configForRequest2 = copy.deepcopy(configFromFile)
        configForRequest2.batchRequestFolder = newRequestDir

        request2 = litleBatchFileRequest(newRequestFileName, configForRequest2)
        request2.sendRequestOnlyToSFTP(True)

        request3 = litleBatchFileRequest(newRequestFileName, configForRequest2)
        response = request3.retrieveOnlyFromSFTP()

        self.assertPythonApi(request3, response)

        self.assertGeneratedFiles(newRequestDir, responseDir, newRequestFileName, request3)

    def testSendToLitleSFTP_WithFileConfig(self):
        requestFileName = "litleSdk-testBatchFile-testSendToLitleSFTP_WithFileConfig.xml"
        request = litleBatchFileRequest(requestFileName)
        requestFile = request.requestFile.name
        self.assertTrue(os.path.exists(requestFile))
        configFromFile = request.config
        self.assertEqual('prelive.litle.com', configFromFile.batchHost)
        self.assertEqual('15000', configFromFile.batchPort)
        self.assertEquals('True', configFromFile.printXml)
        requestDir = configFromFile.batchRequestFolder
        responseDir = configFromFile.batchResponseFolder

        self.prepareTestRequest(request)

        response = request.sendRequestSFTP()
        self.assertPythonApi(request, response)
        self.assertGeneratedFiles(requestDir, responseDir, requestFileName, request)

    def testSendToLitleSFTP_WithConfigOverrides(self):
        requestDir = tempfile.gettempdir() + '/' + 'request'
        responseDir = tempfile.gettempdir() + '/' + 'response'

        configOverrides = Configuration()

        configOverrides.batchHost = 'prelive.litle.com'
        configOverrides.sftpTimeout = '720000'
        configOverrides.batchRequestFolder = requestDir
        configOverrides.batchResponseFolder = responseDir
        configOverrides.printXml = True

        requestFileName = "litleSdk-testBatchFile-testSendToLitleSFTP_WithConfigOverrides.xml"
        request = litleBatchFileRequest(requestFileName, configOverrides)

        self.assertTrue(os.path.exists(request.requestFile.name))
        self.assertTrue(request.config.printXml)
        
        self.prepareTestRequest(request)

        response = request.sendRequestSFTP()

        self.assertPythonApi(request, response)
        self.assertGeneratedFiles(requestDir, responseDir, requestFileName, request)


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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBatch)
    return suite

if __name__ =='__main__':
    unittest.main()
