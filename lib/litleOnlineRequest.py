from litleOnline import *

class litleOnlineRequest:
        
    def __init__(self,Configuration):
        self.Configuration = Configuration
        self.merchantId = Configuration.getMerchantId()
        self.user = Configuration.getUser()
        self.password = Configuration.getPassword()
        self.version = Configuration.getVersion()
        self.reportGroup = Configuration.getReportGroup()
        
    def _litleToXml(self,litleOnline):
        try:
            temp =litleOnline.toxml()
        except:
            raise Exception("Missing Required Field")
        # TODO 
        temp= temp.replace('ns1:','')
        return temp.replace(':ns1','')
    
    def litleXmlMapper(self,transaction):
        litleOnline = self._createTxn(transaction)
        comm = Communications(self.Configuration)
        responseXml = comm.http_post(self._litleToXml(litleOnline))
        return self._processResponse(responseXml)
    
    def _createTxn(self,transaction):
        litleOnline = litleXmlFields.litleOnlineRequest()
        litleOnline.merchantId = self.merchantId
        litleOnline.version = self.version

        authentication = litleXmlFields.authentication()
        authentication.user = self.user
        authentication.password =  self.password 
        litleOnline.authentication = authentication
        transaction.reportGroup = self.reportGroup
        litleOnline.transaction = transaction
        return litleOnline
    
    def _addNamespace(self,responseXml):
        if ((responseXml.count("xmlns='http://www.litle.com/schema'") == 0) and (responseXml.count('xmlns="http://www.litle.com/schema"') == 0)):
            return responseXml.replace(' response=',' xmlns="http://www.litle.com/schema" response=')    
        return responseXml
    
    def _processResponse(self,responseXml):
        temp = self._addNamespace(responseXml)
        return litleXmlFields.CreateFromDocument(temp)
      