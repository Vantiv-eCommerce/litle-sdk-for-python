from litleOnline import *


card = litleXmlFields.cardType()
card.number = "42424242424242424242"
card.expDate = "0912"
card.cardValidationNum = '123'
card.type = 'VI'

authorization = litleXmlFields.authorization()
authorization.orderId = '123'
authorization.reportGroup='planets'
authorization.amount = 123
authorization.orderSource = 'ecommerce'
authorization.card = card

litleXml =  litleOnlineRequest()
response = litleXml.litleXmlMapper(authorization)
print 'Litle transaction ID: %s' %  (response.transactionResponse.litleTxnId)
print 'Litle Message %s' %response.transactionResponse.message
print 'Litle Version %s' %response.version
print 'Litle Fraud AvS Result %s' %response.transactionResponse.fraudResult.avsResult