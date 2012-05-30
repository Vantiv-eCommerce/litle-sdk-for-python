#import litleXmlFields
#from litleXmlFields import litleOnlineResponse
#from Communications import *
from litleOnline import *

class litleOnlineRequest:
        
    def __init__(self,Configuration):
        self.user = Configuration.getUser()
        self.merchantId = Configuration.getMerchantId()
        self.password = Configuration.getPassword()
        
    def _litleToXml(self,litleOnline):
        temp =litleOnline.toxml()
        # TODO 
        temp= temp.replace('ns1:','')
        return temp.replace(':ns1','')
    
    def litleXmlMapper(self,transaction):
        litleOnline = self._createTxn(transaction)
        comm = Communications()
        responseXml = comm.http_post(self._litleToXml(litleOnline))
        return self._processResponse(responseXml)
    
    def _createTxn(self,transaction):
        litleOnline = litleXmlFields.litleOnlineRequest()
        litleOnline.merchantId = self.merchantId
        litleOnline.version = CONST_VERSION

        authentication = litleXmlFields.authentication()
        authentication.user = self.user
        authentication.password =  self.password 
        litleOnline.authentication = authentication
        litleOnline.transaction = transaction
        return litleOnline
    
    def _processResponse(self,responseXml):
         temp = responseXml.replace(' response=',' xmlns="http://www.litle.com/schema" response=')
         return litleXmlFields.CreateFromDocument(temp) 
      