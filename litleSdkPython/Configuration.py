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
        self.__dict = {}
        self.__dict['version'] = 8.25
        self.__dict['reportGroup'] = 'Default Report Group'
        self.__dict['url'] = 'Sandbox'
        self.__dict['proxy'] = None
        self.__dict['timeout'] = 65
        self.__dict['printXml'] = False

    def setProperty(self, key, value):
        self.__dict[key] = value

    def getProperty(self, key, default = None):
        if not self.__dict.has_key(key):
            if default is None:
                raise AttributeError('Property %s has not been set' % key)
            else:
                return default
        else:
            return self.__dict[key]

    def hasProperty(self, key):
        return self.__dict.has_key(key)

    def getUser(self):
        return self.getProperty('username')

    def setUser(self, user):
        self.setProperty('username',user)

    def getMerchantId(self):
        return self.getProperty('merchantId')

    def setMerchantId(self, merchantId):
        self.setProperty('merchantId', merchantId)

    def getPassword(self):
        return self.getProperty('password')

    def setPassword(self, password):
        self.setProperty('password', password)

    def getVersion(self):
        return self.getProperty('version')

    def setVersion(self, version):
        self.setProperty('version', version)

    def getReportGroup(self):
        return self.getProperty('reportGroup')

    def setReportGroup(self, reportGroup):
        self.setProperty('reportGroup', reportGroup)

    def getUrl(self):
        return self._urlMapper(self.getProperty('url'))

    def setUrl(self, url):
        self.setProperty('reportGroup', url)

    def getProxy(self):
        return self.getProperty('proxy')

    def setProxy(self, proxy):
        self.setProperty('proxy', proxy)

    def getTimeout(self):
        return self.getProperty('timeout')

    def setTimeout(self, timeout):
        self.setProperty('timeout', timeout)

    def getBatchHost(self):
        return self.getProperty('batchHost')

    def setBatchHost(self, batchHost):
        self.setProperty('batchHost', batchHost)

    def getSftpTimeout(self):
        return self.getProperty('sftpTimeout')

    def setSftpTimeout(self, sftpTimeout):
        self.setProperty('sftpTimeout', sftpTimeout)

    def getBatchPort(self):
        return self.getProperty('batchPort')

    def setBatchPort(self, batchPort):
        self.setProperty('batchPort', batchPort)

    def getBatchTcpTimeout(self):
        return self.getProperty('batchTcpTimeout')

    def setBatchTcpTimeout(self, batchTcpTimeout):
        self.setProperty('batchTcpTimeout', batchTcpTimeout)

    def getBatchUseSSL(self):
        return self.getProperty('batchUseSSL')

    def setBatchUseSSL(self, batchUseSSL):
        self.setProperty('batchUseSSL', batchUseSSL)

    def getPrintXml(self):
        return self.getProperty('printXml')

    def setPrintXml(self, printXml):
        self.setProperty('printXml', printXml)

    def getBatchRequestPath(self):
        return self.getProperty('batchRequestFolder')

    def setBatchRequestPath(self, batchRequestPath):
        self.setProperty('batchRequestFolder', batchRequestPath)

    def getBatchResponsePath(self):
        return self.getProperty('batchResponseFolder')

    def setBatchResponsePath(self, batchResponsePath):
        self.setProperty('batchResponseFolder', batchResponsePath)

    def getMaxTransactionsPerBatch(self):
        return self.getProperty('maxTransactionsPerBatch')

    def setMaxTransactionsPerBatch(self,maxTransactionsPerBatch):
        self.setProperty('batchResponsePath', maxTransactionsPerBatch)

    def getMaxAllowedTransactionsPerFile(self):
        return self.getProperty('maxAllowedTransactionsPerFile')

    def setMaxAllowedTransactionsPerFile(self,maxAllowedTransactionsPerFile):
        self.setProperty('maxAllowedTransactionsPerFile', maxAllowedTransactionsPerFile)

    def getSftpUsername(self):
        return self.getProperty('sftpUsername')

    def setSftpUsername(self, sftpUsername):
        self.setProperty('sftpUsername', sftpUsername)

    def getSftpPassword(self):
        return self.getProperty('sftpPassword')

    def setSftpPassword(self, sftpPassword):
        self.setProperty('sftpPassword', sftpPassword)

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