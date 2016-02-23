# coding=utf-8
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

from __future__ import print_function
from __future__ import unicode_literals


import os, sys
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest

import re
import sys
import os

if not (("PYTHONIOENCODING" in os.environ)
            and
        re.search("^utf-?8$", os.environ["PYTHONIOENCODING"], re.I)):
    sys.stderr.write(sys.argv[0] + ": Please set your PYTHONIOENCODING envariable to utf8\n")
    sys.exit(1)

import unicodedata
if unicodedata.unidata_version < "6.0.0":
    print("WARNING: Your old UCD is out of date, expected at least 6.0.0 but got", 
           unicodedata.unidata_version)

wide_enough = (sys.maxunicode >= 0x10FFFF)
if not wide_enough:
    print("WARNING: Narrow build detected, your Python lacks full Unicode support!!")

class TestUtf8(unittest.TestCase):
    
    def testJapaneseCharacters(self):
    	authorization = litleXmlFields.authorization()
    	authorization.orderId = '12344'
    	authorization.amount = 106
    	authorization.orderSource = 'ecommerce'
    	
    	card = litleXmlFields.cardType()
    	card.number = "4100000000000001"
    	card.expDate = "1210"
    	card.type = "VI"
    	card.cardValidationNum = "123"
    	
    	billingAddress = litleXmlFields.contact()
    	billingAddress.addressLine1 = u' チャプター'
        billingAddress.city = "Tokyo"
    	
    	authorization.card = card
    	authorization.billToAddress = billingAddress
    	
    	litleXml = litleOnlineRequest(config)
    	response = litleXml.sendRequest(authorization)
    	
    	self.assertEquals("001",response.response)
    
def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtf8)
    return suite

if __name__ =='__main__':
    unittest.main()