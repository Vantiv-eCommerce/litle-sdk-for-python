import urllib2

class Communications:
    def __init__(self,Configuration):
        self.timeout = Configuration.getTimeout()
        self.proxy = Configuration.getProxy()
        self.url = Configuration.getUrl()
        
    def http_post(self,post_data):
       
        req = urllib2.Request(url= self.url, data=post_data)
        req.add_header('Content-type', 'text/xml')
            
        try: 
            if (self.proxy != None) :  
                proxy_handler = urllib2.ProxyHandler({'https': self.proxy}) 
                opener = urllib2.build_opener(proxy_handler)
                response = opener.open(req, timeout=self.timeout)
            else:
                response = urllib2.urlopen(req, timeout=self.timeout)
                
        except:
            raise Exception("Error with Https Request, Please Check Proxy and Url configuration")
        
        responseXml = response.read()
        return responseXml

