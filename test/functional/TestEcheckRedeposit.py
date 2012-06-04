from SetupTest import *
import unittest
from telnetlib import ECHO

class TestEcheckRedeposit(unittest.TestCase):
    
    def test_simpleEcheckRedeposit(self):
        echeckredeposit = litleXmlFields.echeckRedeposit()
        echeckredeposit.litleTxnId = 123456
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckredeposit)
        self.assertEquals("Approved",response.transactionResponse.message)

    def test_echeckRedepositWithEcheck(self):
        echeckredeposit = litleXmlFields.echeckRedeposit()
        echeckredeposit.litleTxnId = 123456
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echeckredeposit.echeck = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckredeposit)
        self.assertEquals("Approved",response.transactionResponse.message)

    def test_echeckRedepositWithEcheckToken(self):
        echeckredeposit = litleXmlFields.echeckRedeposit()
        echeckredeposit.litleTxnId = 123456
        
        echeckToken = litleXmlFields.echeckTokenType()
        echeckToken.litleToken = "1234565789012"
        echeckToken.routingNum = "123456789"
        echeckToken.checkNum = "123455"
        echeckredeposit.echeckToken = echeckToken
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckredeposit)
        self.assertEquals("Approved",response.transactionResponse.message)
