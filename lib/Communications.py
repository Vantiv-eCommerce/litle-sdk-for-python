import urllib2

class Communications:
    def __init__(self,Configuration):
        self.Timeout = Configuration.getTimeout()
        self.Proxy = Configuration.getProxy()
        self.Url = Configuration.getUrl()
        
    def http_post(self,post_data,url=None,proxy=None,timeout=None):
        if (url != None):
            self.Url = url
        if (proxy != None):
            self.Proxy = proxy
        if (timeout != None):
            self.Timeout = timeout
            
        req = urllib2.Request(url= self.Url, data=post_data)
        req.add_header('Content-type', 'text/xml')
            
        try: 
            if (self.Proxy != None) :  
                proxy_handler = urllib2.ProxyHandler({'https': self.Proxy}) 
                opener = urllib2.build_opener(proxy_handler)
                response = opener.open(req, timeout=self.Timeout)
            else:
                response = urllib2.urlopen(req, timeout=self.Timeout)
                
        except:
            raise Exception("Error with Https Request, Please Check Proxy and Url configuration")
        
        responseXml = response.read()
        return responseXml

