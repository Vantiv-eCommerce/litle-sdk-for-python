

class Configuration:

    def __init__(self):
        self.version = 8.10
        
    def setMerchantId(self, merchantId):
        self.merchantId = merchantId
        
    def setUser(self, user):
        self.user = user
        
    def setPassword(self, password):
        self.password = password
        
    def getMerchantId(self):
        return self.merchantId
        
    def getUser(self):
        return self.user
        
    def getPassword(self):
        return self.password
    
    def getVersion(self):
        return self.version
        
    def setVersion(self,version):
        self.Version = version
    