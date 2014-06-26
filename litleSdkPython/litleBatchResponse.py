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
from responseParser import *

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
