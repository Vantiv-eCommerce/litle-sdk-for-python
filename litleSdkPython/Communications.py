#Copyright (c) 2011-2012 Litle & Co.
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

import urllib2

class Communications:
    def __init__(self, Configuration):
        self.Timeout = Configuration.getTimeout()
        self.Proxy = Configuration.getProxy()
        self.Url = Configuration.getUrl()
        
    def http_post(self, post_data, url=None, proxy=None, timeout=None):
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
                response = opener.open(req, timeout = self.Timeout)
            else:
                response = urllib2.urlopen(req, timeout = self.Timeout)
        except Exception,e:
            raise Exception("Error with Https Request, Please Check Proxy and Url configuration",e)
        
        responseXml = response.read()
        return responseXml

