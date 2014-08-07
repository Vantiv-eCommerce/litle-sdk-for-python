from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"
 
#Credit
#litleTxnId contains the Litle Transaction Id returned on
#the capture or sale transaction being credited
#the amount is optional, if it isn't submitted the full amount will be credited
 
credit = litleXmlFields.credit()
credit.amount = 106
credit.litleTxnId = '100000000000000002'
 
litleXml =  litleOnlineRequest(config)
response = litleXml.sendRequest(credit)
 
#display results
print "Response: " + response.response
print "Message: " + response.message
print "LitleTransaction ID: " + str(response.litleTxnId)

if response.response != "000":
	raise Exception("Incorrect Response")
