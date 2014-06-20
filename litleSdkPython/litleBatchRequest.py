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
    def __init__(self, fileRequest):
        self.lbfr = fileRequest
        self.config = fileRequest.config
        self.MerchantId = self.config.getMerchantId()
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
        self._batchRequest.numTokenRegistration = 0
        self._batchRequest.numCaptureGivenAuth = 0
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
        self._batchRequest.numUpdateCardValidationNumOnToken = 0
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

        __tmpDir = self.config.getBatchRequestPath()+'/tmp'
        _maxTransactionsPerBatch_ = int(self.config.getMaxTransactionsPerBatch())
        if not os.path.exists(__tmpDir):
            os.makedirs(__tmpDir)
        _timeInMillisec_ = int(round( time.time() * 1000 ))
        self._filePath = __tmpDir+'/Transactions' + self.MerchantId + str(_timeInMillisec_)

        if int(self.config.getMaxTransactionsPerBatch()) > self.__litleLimit_maxTransactionsPerBatch:
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
            self._batchRequest.numTokenRegistration += 1
            __transactionAdded = True
            self.numOfTxn += 1

        elif isinstance(transaction, litleXmlFields.captureGivenAuth.typeDefinition()):
            self._batchRequest.numCaptureGivenAuth += 1
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
            self._batchRequest.numUpdateCardValidationNumOnToken += 1
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
            self._batchRequest.numActivates += 1
            self._batchRequest.numDeactivates += transaction.amount
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
            try:
                __batchFile.write(self.lbfr.tnxToXml(transaction))
            except pyxb.BindingValidationError,e:
                raise Exception("There was an exception while translating the transaction object.",e)
            return TransactionCode.SUCCESS
        else:
            return TransactionCode.FAILURE



    def verifyFileThresholds(self):
        if self.lbfr.getNumberOfTransactionInFile() == self.config.getMaxAllowedTransactionsPerFile():
            return TransactionCode.FILEFULL
        elif self.numOfTxn == self.config.getMaxTransactionsPerBatch():
            return TransactionCode.BATCHFULL
        return TransactionCode.SUCCESS

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
            confParser.read('/usr/local/litle-home/ashinde/repos/litle-sdk-for-python/litleSdkPython/.litle_Python_SDK_config')
        # propertyList = ["username", "password", "proxyHost",
			# 		"proxyPort", "batchHost", "batchPort",
			# 		"batchTcpTimeout", "batchUseSSL",
			# 		"maxAllowedTransactionsPerFile", "maxTransactionsPerBatch",
			# 		"batchRequestFolder", "batchResponseFolder", "sftpUsername", "sftpPassword"]
        # for p in propertyList:
            self.config.setUser(confParser.get('PythonSDK', 'username'))
            self.config.setPassword(confParser.get('PythonSDK', 'password'))
            self.config.setBatchHost(confParser.get('PythonSDK', 'batchHost'))
            self.config.setBatchPort(confParser.get('PythonSDK', 'batchPort'))
            self.config.setBatchTcpTimeout(confParser.get('PythonSDK', 'batchTcpTimeout'))
            self.config.setBatchUseSSL(confParser.get('PythonSDK', 'batchUseSSL'))
            self.config.setMaxAllowedTransactionsPerFile(confParser.get('PythonSDK', 'maxAllowedTransactionsPerFile'))
            self.config.setMaxTransactionsPerBatch(confParser.get('PythonSDK', 'maxTransactionsPerBatch'))
            self.config.setBatchRequestPath(confParser.get('PythonSDK', 'batchRequestFolder'))
            self.config.setBatchResponsePath(confParser.get('PythonSDK', 'batchResponseFolder'))
            self.config.setSftpUsername(confParser.get('PythonSDK', 'sftpUsername'))
            self.config.setSftpPassword(confParser.get('PythonSDK', 'sftpPassword'))
            self.config.setMerchantId(confParser.get('PythonSDK', 'merchantId'))


        self.communication = Communications(self.config)
        if int(self.config.getMaxAllowedTransactionsPerFile()) > self.__litleLimit_maxAllowedTransactionsPerFile:
            raise Exception('maxAllowedTransactionsPerFile property value cannot exceed'+ \
                            str(self.__litleLimit_maxAllowedTransactionsPerFile))

        __dirRequest = self.config.getBatchRequestPath()
        if not os.path.exists(__dirRequest):
            os.makedirs(__dirRequest)
        self.requestFile = open(__dirRequest + '/' + self._requestFileName,'w')
        self.requestFile.close()
        __dirResponse = self.config.getBatchResponsePath()
        if not os.path.exists(__dirResponse):
            os.makedirs(__dirResponse)
        self.responseFile = open(__dirResponse + '/' + self._requestFileName,'w')
        self.responseFile.close()

    def createBatch(self):
        request = litleBatchRequest(self)
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

    def prepareForDelivery(self):
        writeFolderPath = self.config.getBatchRequestPath()
        self.tempBatchRequestFile = open(writeFolderPath + '/tmp/tempBatchFile','wb')
        for batch in self.batchRequestList:
            batchHeader = self.tnxToXml(batch._batchRequest)
            self.tempBatchRequestFile.write(batchHeader.replace('/>' , '>'))
            with open(batch._filePath,'rb') as batchFile:
                shutil.copyfileobj(batchFile, self.tempBatchRequestFile,4096)
                batchFile.close()
            self.tempBatchRequestFile.write('</batchRequest>\n')
            os.remove(batch._filePath)
        self.tempBatchRequestFile.close()
        self.generateRequestFile()
        shutil.rmtree(writeFolderPath + '/tmp')

    def generateRequestFile(self):
        authentication = litleXmlFields.authentication()
        authentication.password = self.config.getPassword()
        authentication.user = self.config.getUser()

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
            tempBatchFile.close()
        requestFile.write('</litleRequest>\n')
        requestFile.close()
        os.remove(self.tempBatchRequestFile.name)

    def tnxToXml(self, transaction):
        dom = transaction.toDOM()
        temp = dom.toxml('utf-8')
        temp= temp.replace('ns1:','')
        temp =  temp.replace(':ns1','')
        return temp.replace('<?xml version="1.0" encoding="utf-8"?>','')
