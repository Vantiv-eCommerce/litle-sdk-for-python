#Copyright (c) 2011-2012 Litle & Co.
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

import litleXmlFields
import pyxb
import os
import shutil
from Communications import *
from litleBatchResponse import *
from Configuration import *
import time
from ConfigParser import *

class litleBatchRequest:
    def __init__(self, fileRequest, merchantId = None):
        self.lbfr = fileRequest
        self.config = fileRequest.config
        self.MerchantId = self.config.merchantId if merchantId is None else merchantId
        self.numOfTxn = 0
        self.__litleLimit_maxTransactionsPerBatch = 100000

        self._batchRequest = litleXmlFields.batchRequest()
        self._batchRequest.id = None
        self._batchRequest.merchantId = self.MerchantId
        self._batchRequest.numAuths = 0
        self._batchRequest.authAmount = 0
        self._batchRequest.numSales = 0
        self._batchRequest.saleAmount = 0
        self._batchRequest.numCredits = 0
        self._batchRequest.creditAmount = 0
        self._batchRequest.numTokenRegistrations = 0
        self._batchRequest.numCaptureGivenAuths = 0
        self._batchRequest.captureGivenAuthAmount = 0
        self._batchRequest.numForceCaptures = 0
        self._batchRequest.forceCaptureAmount = 0
        self._batchRequest.numAuthReversals = 0
        self._batchRequest.authReversalAmount = 0
        self._batchRequest.numCaptures = 0
        self._batchRequest.captureAmount = 0
        self._batchRequest.numEcheckVerification = 0
        self._batchRequest.echeckVerificationAmount = 0
        self._batchRequest.numEcheckCredit = 0
        self._batchRequest.echeckCreditAmount = 0
        self._batchRequest.numEcheckRedeposit = 0
        self._batchRequest.numEcheckSales = 0
        self._batchRequest.echeckSalesAmount = 0
        self._batchRequest.numUpdateCardValidationNumOnTokens = 0
        self._batchRequest.numAccountUpdates = 0
        self._batchRequest.total = 0
        self._batchRequest.numCancelSubscriptions = 0
        self._batchRequest.numUpdateSubscriptions = 0
        self._batchRequest.numCreatePlans = 0
        self._batchRequest.numUpdatePlans = 0
        self._batchRequest.numActivates = 0
        self._batchRequest.activateAmount =0
        self._batchRequest.numDeactivates = 0
        self._batchRequest.numLoads = 0
        self._batchRequest.loadAmount = 0
        self._batchRequest.numUnloads = 0
        self._batchRequest.unloadAmount = 0
        self._batchRequest.numBalanceInquirys = 0
        self._batchRequest.merchantSdk = None

        __tmpDir = self.config.batchRequestFolder+'/tmp'
        self._maxTransactionsPerBatch = int(getattr(self.config, 'maxTransactionsPerBatch', '10000'))
        if not os.path.exists(__tmpDir):
            os.makedirs(__tmpDir)
        _timeInMillisec_ = int(round( time.time() * 1000 ))
        self._filePath = __tmpDir+'/Transactions' + self.MerchantId + str(_timeInMillisec_)

        if int(self.config.maxTransactionsPerBatch) > self.__litleLimit_maxTransactionsPerBatch:
            raise Exception('maxTransactionsPerBatch property value cannot exceed'+ \
                            str(self.__litleLimit_maxTransactionsPerBatch))

    def addTransaction(self, transaction):
        if self.numOfTxn == 0:
            __batchFile = open(self._filePath, 'w')
        else:
            __batchFile = open(self._filePath, 'a')

        if self.numOfTxn > 0 and self._batchRequest.numAccountUpdates != self.numOfTxn\
            and isinstance(transaction,litleXmlFields.accountUpdate.typeDefinition()):
            raise Exception('An account update cannot be added to a batch containing transactions other than other AccountUpdates.')
        elif self.numOfTxn > 0 and self._batchRequest.numAccountUpdates == self.numOfTxn\
            and not isinstance(transaction,litleXmlFields.accountUpdate.typeDefinition()):
            raise Exception('Transactions that are not AccountUpdates cannot be added to a batch containing AccountUpdates.')

        batchFileStatus = self.verifyFileThresholds()
        if batchFileStatus == TransactionCode.FILEFULL:
            raise Exception('Batch File is already full -- it has reached the maximum number of transactions allowed per batch file.')
        elif batchFileStatus == TransactionCode.BATCHFULL:
            raise Exception('Batch is already full -- it has reached the maximum number of transactions allowed per batch.')

        __transactionAdded = False
        if isinstance(transaction, litleXmlFields.sale.typeDefinition()):
            self._batchRequest.numSales += 1
            self._batchRequest.saleAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.authorization.typeDefinition()):
            self._batchRequest.numAuths += 1
            self._batchRequest.authAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.credit.typeDefinition()):
            self._batchRequest.numCredits += 1
            self._batchRequest.creditAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.registerTokenRequest.typeDefinition()):
            self._batchRequest.numTokenRegistrations += 1
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.captureGivenAuth.typeDefinition()):
            self._batchRequest.numCaptureGivenAuths += 1
            self._batchRequest.captureGivenAuthAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.forceCapture.typeDefinition()):
            self._batchRequest.numForceCaptures += 1
            self._batchRequest.forceCaptureAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.authReversal.typeDefinition()):
            self._batchRequest.numAuthReversals += 1
            self._batchRequest.authReversalAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.capture.typeDefinition()):
            self._batchRequest.numCaptures += 1
            self._batchRequest.captureAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.echeckVerification.typeDefinition()):
            self._batchRequest.numEcheckVerification += 1
            self._batchRequest.echeckVerificationAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.echeckCredit.typeDefinition()):
            self._batchRequest.numEcheckCredit += 1
            self._batchRequest.echeckCreditAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.echeckRedeposit.typeDefinition()):
            self._batchRequest.numEcheckRedeposit += 1
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.echeckSale.typeDefinition()):
            self._batchRequest.numEcheckSales += 1
            self._batchRequest.echeckSalesAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.updateCardValidationNumOnToken.typeDefinition()):
            self._batchRequest.numUpdateCardValidationNumOnTokens += 1
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.updateSubscription.typeDefinition()):
            self._batchRequest.numUpdateSubscriptions += 1
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.cancelSubscription.typeDefinition()):
            self._batchRequest.numCancelSubscriptions += 1
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.createPlan.typeDefinition()):
            self._batchRequest.numCreatePlans += 1
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.updatePlan.typeDefinition()):
            self._batchRequest.numUpdatePlans += 1
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.activate.typeDefinition()):
            self._batchRequest.numActivates += 1
            self._batchRequest.activateAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.deactivate.typeDefinition()):
            self._batchRequest.numDeactivates += 1
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.load.typeDefinition()):
            self._batchRequest.numLoads += 1
            self._batchRequest.loadAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.unload.typeDefinition()):
            self._batchRequest.numUnloads += 1
            self._batchRequest.unloadAmount += transaction.amount
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.balanceInquiry.typeDefinition()):
            self._batchRequest.numBalanceInquirys += 1
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.accountUpdate.typeDefinition()):
            self._batchRequest.numAccountUpdates += 1
            __transactionAdded = True
            self.numOfTxn += 1

        batchFileStatus = self.verifyFileThresholds()
        if batchFileStatus == TransactionCode.FILEFULL:
            return TransactionCode.FILEFULL
        elif batchFileStatus == TransactionCode.BATCHFULL:
            return TransactionCode.BATCHFULL

        if __transactionAdded:
            if hasattr(transaction, 'reportGroup') and transaction.reportGroup is None:
                transaction.reportGroup = self.config.reportGroup
            try:
                __batchFile.write(self.lbfr.tnxToXml(transaction))
            except pyxb.BindingValidationError,e:
                raise Exception("There was an exception while translating the transaction object.",e)
            __batchFile.close()
            return TransactionCode.SUCCESS
        else:
            __batchFile.close()
            return TransactionCode.FAILURE

    def verifyFileThresholds(self):
        if self.lbfr.getNumberOfTransactionInFile() == self.lbfr._maxAllowedTransactionsPerFile:
            return TransactionCode.FILEFULL
        elif self.numOfTxn == self._maxTransactionsPerBatch:
            return TransactionCode.BATCHFULL
        return TransactionCode.SUCCESS

    def isFull(self):
        return self.numOfTxn == self._maxTransactionsPerBatch

class TransactionCode:
    SUCCESS = "Success"
    FAILURE = "Failed"
    BATCHFULL = "Batch is Full"
    FILEFULL = "File is Full"


class litleBatchFileRequest:

    def __init__(self,requestFileName, config = None):
        self.config = config
        self._requestFileName = requestFileName
        self.batchRequestList = []
        self.__litleLimit_maxAllowedTransactionsPerFile = 500000
        self.requestId = None

        if config is None:
            self.config = Configuration()
        confParser = ConfigParser()

        configFilePath = self.config.configFolder + '/' + self.config.getConfigFileName()

        if not os.path.exists(configFilePath):
            f = open(configFilePath, 'a')
            f.close()

        confParser.read(configFilePath)
        propertyList = ["username", "password", "merchantId", "proxyHost",
			 		    "proxyPort", "batchHost", "batchPort",
			 		    "batchTcpTimeout", "batchUseSSL",
			 		    "maxAllowedTransactionsPerFile", "maxTransactionsPerBatch",
			 		    "batchRequestFolder", "batchResponseFolder", "sftpUsername", "sftpPassword", "sftpTimeout"]

        for prop in propertyList:
            if confParser.has_option('PythonSDK', prop) and not hasattr(self.config, prop):
                setattr(self.config, prop, confParser.get('PythonSDK', prop))

        self.communication = Communications(self.config)

        self._maxAllowedTransactionsPerFile = int(getattr(self.config, 'maxAllowedTransactionsPerFile', '1000'))
        if self._maxAllowedTransactionsPerFile > self.__litleLimit_maxAllowedTransactionsPerFile:
            raise Exception('maxAllowedTransactionsPerFile property value cannot exceed'+ \
                            str(self.__litleLimit_maxAllowedTransactionsPerFile))

        __dirRequest = self.config.batchRequestFolder
        if not os.path.exists(__dirRequest):
            os.makedirs(__dirRequest)


        self.requestFile = open(__dirRequest + '/' + self._requestFileName,'a')
        self.requestFile.close()

        __dirResponse = self.config.batchResponseFolder
        if not os.path.exists(__dirResponse):
            os.makedirs(__dirResponse)

        self.responseFile = open(__dirResponse + '/' + self._requestFileName,'a')
        self.responseFile.close()

    def createBatch(self, merchantId = None):
        request = litleBatchRequest(self, merchantId)
        self.batchRequestList.append(request)
        return request

    def getNumberOfTransactionInFile(self):
        totalNumOfTxns = 0
        for batch in self.batchRequestList:
            totalNumOfTxns += batch.numOfTxn
        return totalNumOfTxns

    def sendRequestTCP(self):
        self.prepareForDelivery()
        self.communication.sendRequestFileToIBC(self.requestFile.name, self.responseFile.name, self.config)
        response = litleBatchFileResponse(self.responseFile.name)
        return response

    def sendRequestSFTP(self, useExistingFile = False):
        if not useExistingFile:
            self.prepareForDelivery()
        self.communication.sendRequestFileToSFTP(self.requestFile.name, self.config)
        self.communication.receiveResponseFileFromSFTP(self.requestFile.name, self.responseFile.name, self.config)
        response = litleBatchFileResponse(self.responseFile.name)
        return response

    def sendRequestOnlyToSFTP(self, useExistingFile = False):
        if not useExistingFile:
            self.prepareForDelivery()
        self.communication.sendRequestFileToSFTP(self.requestFile.name, self.config)

    def retrieveOnlyFromSFTP(self):
        self.communication.receiveResponseFileFromSFTP(self.requestFile.name, self.responseFile.name, self.config)
        response = litleBatchFileResponse(self.responseFile.name)
        return response

    def prepareForDelivery(self):
        writeFolderPath = self.config.batchRequestFolder
        self.tempBatchRequestFile = open(writeFolderPath + '/tmp/tempBatchFile','wb')
        for batch in self.batchRequestList:
            batchHeader = self.tnxToXml(batch._batchRequest)
            self.tempBatchRequestFile.write(batchHeader.replace('/>' , '>'))
            with open(batch._filePath,'rb') as batchFile:
                shutil.copyfileobj(batchFile, self.tempBatchRequestFile,4096)
            self.tempBatchRequestFile.write('</batchRequest>\n')
            os.remove(batch._filePath)
        self.tempBatchRequestFile.close()
        self.generateRequestFile()
        shutil.rmtree(writeFolderPath + '/tmp')

    def generateRequestFile(self):
        authentication = litleXmlFields.authentication()
        authentication.password = self.config.password
        authentication.user = self.config.username

        litleRequest = litleXmlFields.litleRequest()
        if self.requestId is not None and len(self.requestId) != 0:
            litleRequest.id = self.requestId

        litleRequest.authentication = authentication
        litleRequest.version = '8.25'
        litleRequest.numBatchRequests = len(self.batchRequestList)
        requestFile = open(self.requestFile.name,'wb')
        requestFile.write(self.tnxToXml(litleRequest).replace('</litleRequest>', ''))
        with open(self.tempBatchRequestFile.name,'rb') as tempBatchFile:
            shutil.copyfileobj(tempBatchFile, requestFile, 4096)
        requestFile.write('</litleRequest>\n')
        requestFile.close()
        os.remove(self.tempBatchRequestFile.name)

    def tnxToXml(self, transaction):
        dom = transaction.toDOM()
        temp = dom.toxml('utf-8')
        temp= temp.replace('ns1:','')
        temp =  temp.replace(':ns1','')
        return temp.replace('<?xml version="1.0" encoding="utf-8"?>','')

    def getNumberOfBatches(self):
        return len(self.batchRequestList)

    def isEmpty(self):
        return True if self.getNumberOfTransactionInFile() == 0 else False

    def isFull(self):
        return self.getNumberOfTransactionInFile() == self._maxAllowedTransactionsPerFile
