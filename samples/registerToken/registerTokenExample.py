from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"
 
#Register an account number to receive a Litle Token
token = litleXmlFields.registerTokenRequest()
token.orderId = '12344'
token.accountNumber = '1233456789103801'
 
litleXml =  litleOnlineRequest(config)
response = litleXml.sendRequest(token)
 
#display results
print "Response: " + response.response
print "Message: " + response.message
print "LitleTransaction ID: " + str(response.litleTxnId)
print "Litle Token: " + response.litleToken

if response.response != "801":
        raise Exception("Invalid response")
