from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"
 
#Register an account number to receive a Litle Token
request = litleXmlFields.registerTokenRequest()
request.orderId = '12344'
request.paypageRegistrationId = 'bzB1ckJSa0cwb2JiYkU2aHVXaWdiMDZOKzRxdHo4ZjRhNHFQMDc1am45THBnODBHM2RyOU5oVXREMjhHTVRYRg=='
 
litleXml = litleOnlineRequest(config)
response = litleXml.sendRequest(request)
 
#display results
print "Response: " + response.response
print "Message: " + response.message
print "LitleTransaction ID: " + str(response.litleTxnId)
print "Litle Token: " + response.litleToken

if response.response != "801":
	raise Exception("Incorrect response")
