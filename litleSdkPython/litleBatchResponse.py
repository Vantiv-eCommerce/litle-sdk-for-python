import litleXmlFields
import pyxb
import os
import shutil
from responseParser import *
from Communications import *
from Configuration import *

class litleBatchResponse:
    def __init__(self, parser):
        self.parser = parser
        self.allTransactionRetrieved = False
        batchResponseXML = self.parser.getNextTag("batchResponse")
        batchResponseXML = responseUtil.addNamespace(batchResponseXML)
        self.batchResponse = litleXmlFields.CreateFromDocument(batchResponseXML)

    def getNextTransaction(self):
        if self.allTransactionRetrieved:
            raise NoTransactionException("All transactions from this batch have already been retrieved")
        try:
            self.txnXML = self.parser.getNextTag("transactionResponse")
        except:
            self.allTransactionRetrieved = True
            raise NoTransactionException("All transactions from this batch have already been retrieved")
        self.txnXML = responseUtil.addNamespace(self.txnXML)
        self.transaction = litleXmlFields.CreateFromDocument(self.txnXML)
        return self.transaction

class litleBatchFileResponse:
    def __init__(self, xmlFile):
        self.xmlFile = xmlFile
        self.parser = ResponseParser(xmlFile)
        litleResponseXml = self.parser.getNextTag('litleResponse')
        litleResponseXml = responseUtil.addNamespace(litleResponseXml)
        self.litleResponse = litleXmlFields.CreateFromDocument(litleResponseXml)

    def getNextBatchResponse(self):
        batchResponse = litleBatchResponse(self.parser)
        return batchResponse

class responseUtil:
    @staticmethod
    def addNamespace(responseXml):
        if responseXml.count("xmlns='http://www.litle.com/schema'") == 0 and \
            responseXml.count('xmlns="http://www.litle.com/schema"') == 0:
            return responseXml.replace('>', ' xmlns="http://www.litle.com/schema">', 1)
        return responseXml

class NoTransactionException(Exception):
    def __init__(self, value):
        self.value = value
