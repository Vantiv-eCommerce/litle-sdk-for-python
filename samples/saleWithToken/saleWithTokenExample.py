from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"
 
#sale
sale = litleXmlFields.sale()
sale.orderId = "1"
sale.amount = 10010
sale.orderSource = "ecommerce"
contact = litleXmlFields.contact();
contact.name="John Smith"
contact.addressLine1="1 Main St."
contact.city="Burlington"
contact.state="MA"
contact.zip="01803-3747"
contact.country="USA"
sale.billToAddress = contact
token = litleXmlFields.cardTokenType()
token.litleToken = "1234123412341234"
token.expDate = "0112"
token.cardValidationNum = "349"
token.type = "VI"
sale.token = token
 
litleXml = litleOnlineRequest(config)
response = litleXml.sendRequest(sale)
 
#display results
print "Response: " + response.response
print "Message: " + response.message
print "LitleTransaction ID: " + str(response.litleTxnId)

if response.response != "000":
	raise Exception("Incorrect response")
