from litleOnlineRequest import *

config = Configuration()
config.setPassword('certpass')
config.setUser('PHXMLTEST')
config.setMerchantId('101')
config.setReportGroup('Planets')
#config.setProxy('smoothproxy:8080')
config.setUrl('Cert')

authorization = litleXmlFields.authorization()
authorization.orderId = '123'
authorization.amount = 123
authorization.orderSource = 'ecommerce'

card = litleXmlFields.cardType()
card.number = "42424242424242424242"
card.expDate = "0912"
card.cardValidationNum = '123'
card.type = 'VI'

authorization.card = card

litleXml =  litleOnlineRequest(config)
response = litleXml.sendRequest(authorization)

print 'Litle transaction ID: %s' %  (response.transactionResponse.litleTxnId)
print 'Litle Message %s' %response.transactionResponse.message
print 'Litle Version %s' %response.version
#print 'Litle Fraud AvS Result %s' %response.transactionResponse.fraudResult.avsResult