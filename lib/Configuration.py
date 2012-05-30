

class Configuration:

    def __init__(self):
        self.version = 8.10
        self.reportGroup = 'Default Report Group'
        self.url = 'https://www.testlitle.com/sandbox/communicator/online'
        self.proxy = None
        self.timeout = 65
        
    def getUser(self):
        return self.user
        
    def setUser(self, user):
        self.user = user
        
    def getMerchantId(self):
        return self.merchantId
        
    def setMerchantId(self, merchantId):
        self.merchantId = merchantId
        
    def getPassword(self):
        return self.password
        
    def setPassword(self, password):
        self.password = password
    
    def getVersion(self):
        return self.version
        
    def setVersion(self, version):
        self.version = version
    
    def getReportGroup(self):
        return self.reportGroup
        
    def setReportGroup(self, reportGroup):
        self.reportGroup = reportGroup
        
    def getUrl(self):
        return self.url
        
    def setUrl(self, url):
        self.url = url
        
    def getProxy(self):
        return self.proxy
        
    def setProxy(self, proxy):
        self.proxy = proxy
        
    def getTimeout(self):
        return self.timeout
        
    def setTimeout(self, timeout):
        self.timeout = timeout