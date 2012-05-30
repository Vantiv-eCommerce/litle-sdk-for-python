

class Configuration:

    def __init__(self):
        self._version = 8.10
        self._reportGroup = 'Default Report Group'
        self._url = "Sandbox"
        self._proxy = None
        self._timeout = 65
        
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
        
    def _urlMapper(self,target):
        if (target == "Cert"):
            return 'https://cert.litle.com/vap/communicator/online'
        elif(target == "Precert"):
            return 'https://precert.litle.com/vap/communicator/online'
        elif(target == "Prod"):
            return 'https://production.litle.com/vap/communicator/online'
        else:
            return 'https://www.testlitle.com/sandbox/communicator/online'