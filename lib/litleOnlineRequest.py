import litleXmlFields
from litleXmlFields import litleOnlineResponse
from Communications import *
from xml.dom.minidom import parseString

class litleOnlineRequest:
    
    def _litleToXml(self,litleOnline):
        temp =litleOnline.toxml()
        temp= temp.replace('ns1:','')
        return temp.replace(':ns1','')
    
    def litleXmlMapper(self,transaction):
        litleOnline = self._createTxn(transaction)
        comm = Communications()
        responseXml = comm.http_post(self._litleToXml(litleOnline))
        return self._processResponse(responseXml)
    
    def _createTxn(self,transaction):
        litleOnline = litleXmlFields.litleOnlineRequest()
        litleOnline.merchantId = '101'
        litleOnline.version = 8.10

        authentication = litleXmlFields.authentication()
        authentication.user = 'PHXMLTEST'
        authentication.password = 'certpass'
        authentication.name = '321'
        litleOnline.authentication = authentication
        litleOnline.transaction = transaction
        return litleOnline
    
    def _processResponse(self,responseXml):
         temp = responseXml.replace(' response=',' xmlns="http://www.litle.com/schema" response=')
         return litleXmlFields.CreateFromDocument(temp) 
      