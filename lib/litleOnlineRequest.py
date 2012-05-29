import litleXmlFields

class litleOnlineRequest:
    
    def litleToXml(self,litleOnline):
        temp =litleOnline.toxml()
        temp= temp.replace('ns1:','')
        return temp.replace(':ns1','')
    
    def litleXmlMapper(self,transaction):
        litleOnline = self.createTxn(transaction)
        return self.litleToXml(litleOnline)
       # self.communications
       # response = self.ToDom
        #return response
    
    def createTxn(self,transaction):
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