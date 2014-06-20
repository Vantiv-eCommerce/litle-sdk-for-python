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

class Configuration:

    def __init__(self):
        self._version = '8.25'
        self._reportGroup = 'Default Report Group'
        self._url = "Sandbox"
        self._proxy = None
        self._timeout = 65
        self._printXml = False
        self._batchRequestPath = None
        self._batchResponsePath = None
        self._maxTransactionsPerBatch = '10000'
        self._maxAllowedTransactionsPerFile = '1000'
        
    def getUser(self):
        return self._user
        
    def setUser(self, user):
        self._user = user
        
    def getMerchantId(self):
        return self._merchantId
        
    def setMerchantId(self, merchantId):
        self._merchantId = merchantId
        
    def getPassword(self):
        return self._password
        
    def setPassword(self, password):
        self._password = password
    
    def getVersion(self):
        return self._version
        
    def setVersion(self, version):
        self._version = version
    
    def getReportGroup(self):
        return self._reportGroup
        
    def setReportGroup(self, reportGroup):
        self._reportGroup = reportGroup
        
    def getUrl(self):
        return self._urlMapper(self._url)
        
    def setUrl(self, url):
        self._url = url
        
    def getProxy(self):
        return self._proxy
        
    def setProxy(self, proxy):
        self._proxy = proxy
        
    def getTimeout(self):
        return self._timeout
        
    def setTimeout(self, timeout):
        self._timeout = timeout
        
    def getPrintXml(self):
        return self._printXml
    
    def setPrintXml(self, printXml):
        self._printXml = printXml

    def setBatchRequestPath(self, batchRequestPath):
        self._batchRequestPath = batchRequestPath

    def getBatchRequestPath(self):
        return self._batchRequestPath

    def setBatchResponsePath(self, batchResponsePath):
        self._batchResponsePath = batchResponsePath

    def getBatchResponsePath(self):
        return self._batchResponsePath

    def getMaxTransactionsPerBatch(self):
        return self._maxTransactionsPerBatch

    def setMaxTransactionsPerBatch(self,maxTransactionsPerBatch):
        self._maxTransactionsPerBatch = maxTransactionsPerBatch

    def getMaxAllowedTransactionsPerFile(self):
        return self._maxAllowedTransactionsPerFile

    def setMaxAllowedTransactionsPerFile(self,maxAllowedTransactionsPerFile):
        self._maxAllowedTransactionsPerFile = maxAllowedTransactionsPerFile

    def setSftpUsername(self, sftpUsername):
        self._sftpUsername = sftpUsername

    def getSftpUsername(self):
        return self._sftpUsername

    def setSftpPassword(self, sftpPassword):
        self._sftpPassword = sftpPassword

    def getSftpPassword(self):
        return self._sftpPassword

    def setBatchHost(self, batchHost):
        self._batchHost = batchHost

    def getBatchHost(self):
        return self._batchHost

    def setSftpTimeout(self, sftpTimeout):
        self._sftpTimeout = sftpTimeout

    def getSftpTimeout(self):
        return self._sftpTimeout

    def setBatchPort(self, batchPort):
        self._batchPort = batchPort

    def getBatchPort(self):
        return self._batchPort

    def setBatchTcpTimeout(self, batchTcpTimeout):
        self._batchTcpTimeout = batchTcpTimeout

    def getBatchTcpTimeout(self):
        return self._batchTcpTimeout

    def setBatchUseSSL(self, batchUseSSL):
        self._batchUseSSL = batchUseSSL

    def getBatchUseSSL(self):
        return self._batchUseSSL

    def _urlMapper(self,target):
        if (target == "Cert"):
            return 'https://cert.litle.com/vap/communicator/online'
        elif(target == "Sandbox"):
            return 'https://www.testlitle.com/sandbox/communicator/online'
        elif(target == "Precert"):
            return 'https://precert.litle.com/vap/communicator/online'
        elif(target == "Prod"):
            return 'https://production.litle.com/vap/communicator/online'
        else:
            return target