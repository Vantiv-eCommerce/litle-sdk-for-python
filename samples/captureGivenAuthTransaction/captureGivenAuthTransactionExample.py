from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"
 
#Capture Given Auth
capturegivenauth = litleXmlFields.captureGivenAuth()
capturegivenauth.orderId = '12344'
capturegivenauth.amount = 106
authInfo = litleXmlFields.authInformation()
date = pyxb.binding.datatypes.date(2002, 10, 9)
authInfo.authDate = date
authInfo.authCode = "543216"
authInfo.authAmount = 12345
capturegivenauth.authInformation = authInfo
capturegivenauth.orderSource = 'ecommerce'
card = litleXmlFields.cardType()
card.number = "4100000000000001"
card.expDate = "1210"
card.type = 'VI'
capturegivenauth.card = card
 
litleXml = litleOnlineRequest(config)
response = litleXml.sendRequest(capturegivenauth)
 
#display results
print "Response: " + response.response
print "Message: " + response.message
print "LitleTransaction ID: " + str(response.litleTxnId)

if response.response != "000":
	raise Exception("Invalid response")
