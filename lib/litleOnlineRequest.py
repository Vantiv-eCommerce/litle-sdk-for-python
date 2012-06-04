from litleOnline import *

class litleOnlineRequest:
        
    def __init__(self,Configuration):
        self.Configuration = Configuration
        self.MerchantId = Configuration.getMerchantId()
        self.User = Configuration.getUser()
        self.Password = Configuration.getPassword()
        self.Version = Configuration.getVersion()
        self.ReportGroup = Configuration.getReportGroup()
        
    def _litleToXml(self,litleOnline):
        temp =litleOnline.toxml()
        temp= temp.replace('ns1:','')
        return temp.replace(':ns1','')
        
    def sendRequest(self,transaction,user = None, password = None, version = None,  merchantId = None,reportGroup = None, timeout = None,url = None, proxy = None):
        if (user != None):
            self.User = user
        if (password != None):
            self.Password = password
        if (version != None):
            self.Version = version
        if (merchantId != None):
            self.MerchantId = merchantId
        if (reportGroup != None):
            self.ReportGroup = reportGroup
            
        litleOnline = self._createTxn(transaction)        
        comm = Communications(self.Configuration)
        responseXml = comm.http_post(self._litleToXml(litleOnline),url=url,proxy=proxy,timeout=timeout)
        return self._processResponse(responseXml)
    
    def _createTxn(self,transaction):
        litleOnline = litleXmlFields.litleOnlineRequest()
        litleOnline.merchantId = self.MerchantId
        litleOnline.version = self.Version

        authentication = litleXmlFields.authentication()
        authentication.user = self.User
        authentication.password =  self.Password 
        litleOnline.authentication = authentication
        transaction.reportGroup = self.ReportGroup
        litleOnline.transaction = transaction
        return litleOnline
    
    def _addNamespace(self,responseXml):
        if ((responseXml.count("xmlns='http://www.litle.com/schema'") == 0) and (responseXml.count('xmlns="http://www.litle.com/schema"') == 0)):
            return responseXml.replace(' response=',' xmlns="http://www.litle.com/schema" response=')    
        return responseXml
    
    def _processResponse(self,responseXml):
        temp = self._addNamespace(responseXml)
        return litleXmlFields.CreateFromDocument(temp)
      