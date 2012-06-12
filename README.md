litle-sdk-for-python
====================

About Litle
------------
[Litle &amp; Co.](http://www.litle.com) powers the payment processing engines for leading companies that sell directly to consumers through  internet retail, direct response marketing (TV, radio and telephone), and online services. Litle & Co. is the leading, independent authority in card-not-present (CNP) commerce, transaction processing and merchant services.


About this SDK
--------------
The Litle Python SDK is a Python implementation of the [Litle &amp; Co.](http://www.litle.com). XML API. This SDK was created to make it as easy as possible to connect process your payments with Litle.  This SDK utilizes  the HTTPS protocol to securely connect to Litle.  Using the SDK requires coordination with the Litle team in order to be provided with credentials for accessing our systems.

Our Python supports all of the functionality present in Litle XML v8. Please see the online copy of our XSD for Litle XML to get more details on what is supported by the Litle payments engine.

This SDK is implemented to support the Python programming language and was created by Litle & Co. It is intended use is for online transactions processing utilizing your account on the Litle payments engine.

See LICENSE file for details on using this software.

Source Code available from : https://github.com/LitleCo/litle-sdk-for-Python

Please contact [Litle &amp; Co.](http://www.litle.com) to receive valid merchant credentials in order to run tests successfully or if you require assistance in any way.  We are reachable at sdksupport@litle.com

SDK Python Dependencies
----------------------
pyxb

mock

Setup
-----
1) Download and install the PyXB library from http://pyxb.sourceforge.net/overview_how.html

2) Download and install the mock library from http://pypi.python.org/pypi/mock

3) Install the LitleOnline Python SDK.

>git clone git://github.com/LitleCo/litle-sdk-for-python.git

4) Add the LitleSdkPython library to your Project References or interpreter path

5) To run tests see [SDK Testing Info](https://github.com/LitleCo/litle-sdk-for-python/wiki/Testing)

6) Create a python file similar to:

```python
from litleSdkPython.litleOnlineRequest import *

config = Configuration()
config.setUser("User")
config.setPassword("Pass")
config.setMerchantId("123")
config.setUrl("Sandbox")
config.setProxy("")

#sale
sale = litleXmlFields.sale()
sale.orderId = '1'
sale.amount = 10010
sale.orderSource = 'ecommerce'
contact = litleXmlFields.contact();
contact.name="John Smith"
contact.addressLine1="1 Main St."
contact.city="Burlington"
contact.state="MA"
contact.zip="01803-3747"
contact.country="USA"
sale.billToAddress = contact
card = litleXmlFields.cardType()
card.number = "4457010000000009"
card.expDate = "0112"
card.cardValidationNum = "349"
card.type = 'VI'
sale.card = card

litleXml = litleOnlineRequest(config)
response = litleXml.sendRequest(sale)

#display results
print "Message: " + response.message
print "LitleTransaction ID: " + str(response.transactionResponse.litleTxnId)
```
NOTE: you may need to edit the proxy to to work for your system

8) Next run this file.  You should see the following result provided you have connectivity to the Litle certification environment.  You will see an HTTP error if you don't have access to the Litle URL.

    Message: Valid Format
    Litle Transaction ID: <your-numeric-litle-txn-id>
    
For information on cofiguration settings go to: [SDK Config Info](https://github.com/LitleCo/litle-sdk-for-python/wiki/Config-Settings).

Please contact Litle & Co. with any further questions.   You can reach us at SDKSupport@litle.com
