from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"
 
#Auth
#Puts a hold on the fund
auth = litleXmlFields.authorization()
auth.amount = 10010
auth.orderId = "1"
auth.orderSource = 'ecommerce'
 
billtoaddress = litleXmlFields.contact()
billtoaddress.name = "John Smith"
billtoaddress.addressLine1 = "1 Main St."
billtoaddress.city = "Burlington"
billtoaddress.state = "MA"
billtoaddress.zip = "01803-3747"
billtoaddress.country = "USA"
auth.billToAddress = billtoaddress
 
card = litleXmlFields.cardType()
card.type = 'VI'
card.number = "4457010000000009"
card.expDate = "0112"
card.cardValidationNum = "349"
auth.card = card
 
litleXml = litleOnlineRequest(config)
authResponse = litleXml.sendRequest(auth)
 
#Auth Results
print "Response: " + authResponse.response
print "Message: " + authResponse.message
print "LitleTransaction ID: " + str(authResponse.litleTxnId)

if authResponse.response != "000":
	raise Exception("Invalid auth response")
	
#Capture
#Captures the authorization and results in money movement
capture = litleXmlFields.capture()
capture.litleTxnId = authResponse.litleTxnId
captureResponse = litleXml.sendRequest(capture)

 
#Capture Results
print "Capture Response: " + captureResponse.response
print "Message: " + captureResponse.message
print "LitleTransaction ID: " + str(captureResponse.litleTxnId)

if captureResponse.response != "000":
        raise Exception("Invalid capture response")
 
#Credit
#Refund the customer
credit = litleXmlFields.credit()
credit.litleTxnId = captureResponse.litleTxnId
creditResponse = litleXml.sendRequest(credit)
 
#Credit Results
print "Credit Response: " + creditResponse.response
print "Message: " + creditResponse.message
print "LitleTransaction ID: " + str(creditResponse.litleTxnId)

if creditResponse.response != "000":
        raise Exception("Invalid credit response")
 
#Void
#Cancel the refund, note that a deposit can be Voided as well
void = litleXmlFields.void()
void.litleTxnId = creditResponse.litleTxnId
voidResponse = litleXml.sendRequest(void)
 
#Void Results
print "Void Response: " + voidResponse.response
print "Message: " + voidResponse.message
print "LitleTransaction ID: " + str(voidResponse.litleTxnId)


if authResponse.response != "000":
        raise Exception("Invalid void response")
