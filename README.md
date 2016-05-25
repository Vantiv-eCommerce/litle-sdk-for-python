litle-sdk-for-python
====================

About Vantiv eCommerce
------------
[Vantiv eCommerce](http://www.vantiv.com) powers the payment processing engines for leading companies that sell directly to consumers through  internet retail, direct response marketing (TV, radio and telephone), and online services. Vantiv eCommerce is the leading authority in card-not-present (CNP) commerce, transaction processing and merchant services.


About this SDK
--------------
The Vantiv eCommerce Python SDK is a Python implementation of the [Vantiv eCommerce](http://www.vantiv.com/developers) XML API. This SDK was created to make it as easy as possible to connect to and process payments through Vantiv eCommerce.  This SDK utilizes  the HTTPS protocol to securely connect to Vantiv eCommerce.  Using the SDK requires coordination with the Vantiv eCommerce team to obtain credentials for accessing our systems.

Each Python SDK release supports all of the functionality present in the associated Vantiv eCommerce XML version (e.g., SDK v9.3.2 supports Vantiv eCommerce XML v9.3). Please see the online copy of our XSD for Vantiv eCommerce XML to get more details on what the Vantiv eCommerce payments engine supports .

This SDK was implemented to support the Python programming language and was created by Vantiv eCommerce Its intended use is for online transaction processing utilizing your account on the Vantiv eCommerce payments engine.

See LICENSE file for details on using this software.

Source Code available from : https://github.com/LitleCo/litle-sdk-for-Python

Please contact [Vantiv eCommerce](http://www.vantiv.com/developers) to receive valid merchant credentials and determine which version of the SDK is right for your business requirements or if you require assistance in any other way.  You can reach us at sdksupport@Vantiv.com

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

# sale
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

# display results
print "Message: " + response.message
print "LitleTransaction ID: " + str(response.transactionResponse.litleTxnId)
```
NOTE: you may need to edit the proxy to to work for your system

4) Next run this file.  You should see the following result.

    Message: Valid Format
    Litle Transaction ID: <your-numeric-litle-txn-id>
    
For information on configuration settings go to: [SDK Config Info](https://github.com/LitleCo/litle-sdk-for-python/wiki/Config-Settings).

More examples can be found here [Python Gists](https://gist.github.com/gists/search?q=Litle+Python+SDK&page=1)

Please contact Vantiv eCommerce with any further questions. You can reach us at SDKSupport@Vantiv.com
