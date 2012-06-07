#Copyright (c) 2011-2012 Litle & Co.
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

from litleOnlineRequest import *

config = Configuration()
config.setPassword('certpass')
config.setUser('PHXMLTEST')
config.setMerchantId('101')
config.setReportGroup('Planets')
config.setProxy('smoothproxy:8080')
config.setUrl('Sandbox')

authorization = litleXmlFields.authorization()
authorization.litleTxnId = "1000000000000000002"
authorization.orderId = '123'
authorization.amount = 123
authorization.orderSource = 'ecommerce'

#card = litleXmlFields.cardType()
#card.number = "42424242424242424242"
#card.expDate = "0912"
#card.cardValidationNum = '123'
#card.type = 'VI'
#
#authorization.card = card

litleXml =  litleOnlineRequest(config)
response = litleXml.sendRequest(authorization)

print response.message

#print 'Litle transaction ID: %s' %  (response.transactionResponse.litleTxnId)
#print 'Litle Message %s' %response.transactionResponse.message
#print 'Litle Version %s' %response.version
#print 'Litle Fraud AvS Result %s' %response.transactionResponse.fraudResult.avsResult
