from litleBatchRequest import *

lbfr = litleBatchFileRequest('TestSFTPTransactions20140617100')
lbr1 = lbfr.createBatch()

sale = litleXmlFields.sale()
sale.litleTxnId = 123456L
sale.amount = 106L
sale.orderId = '12344'
sale.orderSource = 'ecommerce'
sale.reportGroup = 'default'

card = litleXmlFields.cardType()
card.type = 'VI'
card.number = "4100000000000001"
card.expDate = "1210"
sale.card = card

for i in range(100):
    lbr1.addTransaction(sale)

response = lbfr.sendRequestTCP()
batch = response.getNextBatchResponse()
for j in range(100):
    txn = batch.getNextTransaction()
    print txn.litleTxnId



