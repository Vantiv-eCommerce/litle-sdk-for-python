from litleOnline import *

litleOnline = litleXmlFields.litleOnlineRequest()
litleOnline.merchantId = '101'
litleOnline.version = 8.10

authentication = litleXmlFields.authentication()
authentication.user = 'PHXMLTEST'
authentication.password = 'certpass'
authentication.name = '321'
litleOnline.authentication = authentication

card = litleXmlFields.cardType()
card.number = "42424242424242424242"
card.expDate = "0912"
card.cardValidationNum = '123'
card.type = 'VI'

authorizationx = litleXmlFields.authorization()
authorizationx.orderId = '123'
authorizationx.reportGroup='planets'
authorizationx.amount = 123
authorizationx.orderSource = 'ecommerce'
authorizationx.card = card


litleXml =  litleOnlineRequest()
print litleXml.litleXmlMapper(authorizationx)

