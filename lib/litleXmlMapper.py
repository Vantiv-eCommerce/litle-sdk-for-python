
class litleXmlMapper:
    
     def litleToXml(self,litleOnline):
        temp =litleOnline.toxml()
        temp= temp.replace('ns1:','')
        return temp.replace(':ns1','')