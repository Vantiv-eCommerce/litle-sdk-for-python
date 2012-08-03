litle-sdk-for-python
====================

About Litle
------------
[Litle &amp; Co.](http://www.litle.com) powers the payment processing engines for leading companies that sell directly to consumers through  internet retail, direct response marketing (TV, radio and telephone), and online services. Litle & Co. is the leading, independent authority in card-not-present (CNP) commerce, transaction processing and merchant services.


About this SDK
--------------
The Litle Python SDK is a Python implementation of the [Litle &amp; Co.](http://www.litle.com/developers). XML API. This SDK was created to make it as easy as possible to connect process your payments with Litle.  This SDK utilizes  the HTTPS protocol to securely connect to Litle.  Using the SDK requires coordination with the Litle team in order to be provided with credentials for accessing our systems.

Our Python supports all of the functionality present in Litle XML v8. Please see the online copy of our XSD for Litle XML to get more details on what is supported by the Litle payments engine.

This SDK is implemented to support the Python programming language and was created by Litle & Co. It is intended use is for online transactions processing utilizing your account on the Litle payments engine.

See LICENSE file for details on using this software.

Source Code available from : https://github.com/LitleCo/litle-sdk-for-Python

Please contact [Litle &amp; Co.](http://www.litle.com/developers) to receive valid merchant credentials in order to run tests successfully or if you require assistance in any way.  We are reachable at sdksupport@litle.com

SDK Python Dependencies
----------------------
pyxb : available at http://pyxb.sourceforge.net/overview_how.html

mock(only for running tests): available at http://pypi.python.org/pypi/mock

Setup
-----
1) To download and install:

Using pip 

>pip install LitleSdkPython

Without Pip

>wget http://pypi.python.org/packages/source/L/LitleSdkPython/LitleSdkPython-8.13.0.tar.gz#md5=30c83ed753f37482ce5f04e84836a74d

>tar xf LitleSdkPython-VERSION.tar.gz

>cd LitleSdkPython-VERSION

>python setup.py install

2) To run tests see [SDK Testing Info](https://github.com/LitleCo/litle-sdk-for-python/wiki/Testing)

3) Create a python file similar to:

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

4) Next run this file.  You should see the following result.

    Message: Valid Format
    Litle Transaction ID: <your-numeric-litle-txn-id>
    
For information on cofiguration settings go to: [SDK Config Info](https://github.com/LitleCo/litle-sdk-for-python/wiki/Config-Settings).

More examples can be found here [Python Gists](https://gist.github.com/gists/search?q=Litle+Python+SDK&page=1)

Please contact Litle & Co. with any further questions.   You can reach us at SDKSupport@litle.com
