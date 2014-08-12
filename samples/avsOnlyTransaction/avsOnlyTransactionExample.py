from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"
 
#AVS Only
auth = litleXmlFields.authorization()
auth.orderId = '1'
auth.amount = 10010
auth.orderSource = 'ecommerce'
contact = litleXmlFields.contact();
contact.name="John Smith"
contact.addressLine1="1 Main St."
contact.city="Burlington"
contact.state="MA"
contact.zip="01803-3747"
contact.country="USA"
auth.billToAddress = contact
card = litleXmlFields.cardType()
card.number = "4457010000000009"
card.expDate = "0112"
card.cardValidationNum = "349"
card.type = 'VI'
auth.card = card
 
litleXml = litleOnlineRequest(config)
response = litleXml.sendRequest(auth)
 
#display results
print "Response: " + response.response
print "Message: " + response.message
print "LitleTransaction ID: " + str(response.litleTxnId)
print "AVS Result: " + response.fraudResult.avsResult

if response.response != "000":
        raise Exception("Invalid response")
