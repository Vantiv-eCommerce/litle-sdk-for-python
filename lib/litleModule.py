from litleOnline import *

authentication = litleXmlFields.authentication()
authentication.user = 'PHXMLTEST'
authentication.password = 'certpass'
authentication.name = '321'
#print authentication.toxml()
#print authentication.password
card = litleXmlFields.cardType()
card.number = "42424242424242424242"
card.expDate = "0912"
card.cardValidationNum = '123'
card.type = 'VI'
#print card.toxml()
#print card

litleOnline = litleXmlFields.litleOnlineRequest()
litleOnline.authentication = authentication
litleOnline.merchantId = '101'
litleOnline.version = 8.10

authorizationx = litleXmlFields.authorization()
authorizationx.orderId = '123'
authorizationx.reportGroup='planets'
authorizationx.amount = 123
authorizationx.orderSource = 'ecommerce'
authorizationx.card = card
litleOnline.transaction = authorizationx
postData = litleOnline.toxml()
#voidx = litleXmlFields.void()
#voidx.litleTxnId = 123213213213123123
#print voidx.toxml()
#bds = pyxb.utils.domutils.BindingDOMSupport(namespace_prefix_map={litleXmlFields.Namespace : ''})
temp= litleOnline.toxml()
temp= temp.replace('ns1:','')
print temp.replace(':ns1','')
conn = httplib.HTTPConnection("cert.litle.com")
conn.request("POST", '/vap/communicator/online',postData )#card.toxml()
response = conn.getresponse()
print response.status, response.reason, response.msg 
conn.close()
