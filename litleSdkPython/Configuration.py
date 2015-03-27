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

import os

class Configuration(object):

    def __init__(self):
        self.reportGroup = 'Default Report Group'
        self._url = 'Sandbox'
        self.proxy = None
        #default http timeout set to 500 ms
        self.timeout = 500
        self.printXml = False
        self.configFolder = os.environ['LITLE_SDK_CONFIG']\
            if 'LITLE_SDK_CONFIG' in os.environ else os.path.expanduser('~')
        self.__LITLE_SDK_CONFIG = '.litle_Python_SDK_config'

    @property
    def url(self):
        return self._urlMapper(self._url)

    @url.setter
    def url(self, value):
        self._url = value

    def setUser(self, user):
        self.username = user
        
    def setPassword(self, password):
        self.password = password
        
    def setMerchantId(self, merchantId):
        self.merchantId = merchantId
        
    def setUrl(self, url):
        self.url = url
        
    def setProxy(self, proxy):
        self.proxy = proxy
        
    def setVersion(self, version):
        self.version = version
        
    def setReportGroup(self, reportGroup):
        self.reportGroup = reportGroup
        
    def setTimeout(self, timeout):
        self.timeout = timeout
        
    def setPrintXml(self, printXml):
        self.printXml = printXml

    def getConfigFileName(self):
        return self.__LITLE_SDK_CONFIG

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
