#Copyright (c) 2017 Vantiv eCommerce
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

import os, sys
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest

class TestFraudCheck(unittest.TestCase):
        
    def testFraudCheckNoCustomAttributes(self):
        fraudCheck = litleXmlFields.fraudCheck()
        
        advancedFraudChecks = litleXmlFields.advancedFraudChecksType()
        advancedFraudChecks.threatMetrixSessionId = "123"
        
        fraudCheck.advancedFraudChecks = advancedFraudChecks
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(fraudCheck)

        self.assertEquals('Call Discover', response.message)
        
    def testFraudCheckOneCustomAttributes(self):
        fraudCheck = litleXmlFields.fraudCheck()
        
        advancedFraudChecks = litleXmlFields.advancedFraudChecksType()
        advancedFraudChecks.threatMetrixSessionId = "123"
        advancedFraudChecks.customAttribute1 = 'abc'
        
        fraudCheck.advancedFraudChecks = advancedFraudChecks
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(fraudCheck)

        self.assertEquals('pass', response.advancedFraudResults.deviceReviewStatus)
        
    def testFraudCheckTwoCustomAttributes(self):
        fraudCheck = litleXmlFields.fraudCheck()
        
        advancedFraudChecks = litleXmlFields.advancedFraudChecksType()
        advancedFraudChecks.threatMetrixSessionId = "123"
        advancedFraudChecks.customAttribute1 = 'abc'
        advancedFraudChecks.customAttribute2 = 'def'
        
        fraudCheck.advancedFraudChecks = advancedFraudChecks
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(fraudCheck)

        self.assertEquals(42, response.advancedFraudResults.deviceReputationScore)
        
    def testFraudCheckThreeCustomAttributes(self):
        fraudCheck = litleXmlFields.fraudCheck()
        
        advancedFraudChecks = litleXmlFields.advancedFraudChecksType()
        advancedFraudChecks.threatMetrixSessionId = "123"
        advancedFraudChecks.customAttribute1 = 'abc'
        advancedFraudChecks.customAttribute2 = 'def'
        advancedFraudChecks.customAttribute3 = 'ghi'
        
        fraudCheck.advancedFraudChecks = advancedFraudChecks
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(fraudCheck)

        self.assertEquals('Call Discover', response.message)
        
    def testFraudCheckFourCustomAttributes(self):
        fraudCheck = litleXmlFields.fraudCheck()
        
        advancedFraudChecks = litleXmlFields.advancedFraudChecksType()
        advancedFraudChecks.threatMetrixSessionId = "123"
        advancedFraudChecks.customAttribute1 = 'abc'
        advancedFraudChecks.customAttribute2 = 'def'
        advancedFraudChecks.customAttribute3 = 'ghi'
        advancedFraudChecks.customAttribute4 = 'jkl'
        
        fraudCheck.advancedFraudChecks = advancedFraudChecks
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(fraudCheck)

        self.assertEquals('pass', response.advancedFraudResults.deviceReviewStatus)
        
    def testFraudCheckFiveCustomAttributes(self):
        fraudCheck = litleXmlFields.fraudCheck()
        
        advancedFraudChecks = litleXmlFields.advancedFraudChecksType()
        advancedFraudChecks.threatMetrixSessionId = "123"
        advancedFraudChecks.customAttribute1 = 'abc'
        advancedFraudChecks.customAttribute2 = 'def'
        advancedFraudChecks.customAttribute3 = 'ghi'
        advancedFraudChecks.customAttribute4 = 'jkl'
        advancedFraudChecks.customAttribute5 = 'mno'
        
        fraudCheck.advancedFraudChecks = advancedFraudChecks
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(fraudCheck)

        self.assertEquals(42, response.advancedFraudResults.deviceReputationScore)
        
    def testFraudCheckBillToAddress(self):
        fraudCheck = litleXmlFields.fraudCheck()
        
        advancedFraudChecks = litleXmlFields.advancedFraudChecksType()
        advancedFraudChecks.threatMetrixSessionId = "123"
        
        contact = litleXmlFields.contact()
        contact.firstName = "Fetty"
        contact.lastName = "Wap"
        contact.addressLine1 = "1738 Trap Street"
        contact.city = "Queens"
        contact.state = "New York"
        contact.zip = "11412"
        
        fraudCheck.advancedFraudChecks = advancedFraudChecks
        fraudCheck.billToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(fraudCheck)

        self.assertEquals('Call Discover', response.message)
        
    def testFraudCheckShipToAddress(self):
        fraudCheck = litleXmlFields.fraudCheck()
        
        advancedFraudChecks = litleXmlFields.advancedFraudChecksType()
        advancedFraudChecks.threatMetrixSessionId = "123"
        
        contact = litleXmlFields.contact()
        contact.firstName = "Fetty"
        contact.lastName = "Wap"
        contact.addressLine1 = "1738 Trap Street"
        contact.city = "Queens"
        contact.state = "New York"
        contact.zip = "11412"
        
        fraudCheck.advancedFraudChecks = advancedFraudChecks
        fraudCheck.shipToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(fraudCheck)

        self.assertEquals('pass', response.advancedFraudResults.deviceReviewStatus)
        
    def testFraudCheckAmount(self):
        fraudCheck = litleXmlFields.fraudCheck()
        
        advancedFraudChecks = litleXmlFields.advancedFraudChecksType()
        advancedFraudChecks.threatMetrixSessionId = "123"
        
        fraudCheck.advancedFraudChecks = advancedFraudChecks
        fraudCheck.amount = 100
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(fraudCheck)

        self.assertEquals(42, response.advancedFraudResults.deviceReputationScore)
    
def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFraudCheck)
    return suite

if __name__ =='__main__':
    unittest.main()