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

import os, sys
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest

class certTestBatch(unittest.TestCase):
       
    def testEcheckPreNoteSale(self):
        requestFileName = "litleSdk-testBatchFile-EchecPreNoteSaleCert.xml"
        request = litleBatchFileRequest(requestFileName)

        configFromFile = request.config
        self.assertEqual('prelive.litle.com', configFromFile.batchHost)
        self.assertEqual('15000', configFromFile.batchPort)

        batch = request.createBatch()
 
        #echeckSuccess
        echeckSuccess = litleXmlFields.echeck()
        echeckSuccess.accNum = '1092969901'
        echeckSuccess.accType = 'Corporate'
        echeckSuccess.routingNum = '011075150'
        
        #echeckErr1
        echeckErr1 = litleXmlFields.echeck()
        echeckErr1.accNum = '6099999992'
        echeckErr1.accType = 'Checking'
        echeckErr1.routingNum = '053133052'
        
        #echeckErr2
        echeckErr2 = litleXmlFields.echeck()
        echeckErr2.accNum = '10@2969901'
        echeckErr2.accType = 'Savings'
        echeckErr2.routingNum = '011100012'
 
        #billto address
        contact = litleXmlFields.contact()
        contact.name = 'PreNote Sale Corporate'
        contact.firstName = 'unavailable'
        contact.lastName = 'unavailable'
        contact.companyName = 'PreNote Sale Corporate'
        contact.addressLine1 = '1 Lowell Street'
        contact.addressLine2 = 'Tower 2'
        contact.city = 'lowell'
        contact.state = 'MA'
        contact.zip = '01850'
        contact.phone = '1234567890'
        contact.email = 'Bob@litle.com'

        echeckPreNoteSale = litleXmlFields.echeckPreNoteSale();
        echeckPreNoteSale.orderId = "1"
        echeckPreNoteSale.billToAddress = contact
        echeckPreNoteSale.echeck = echeckSuccess
        echeckPreNoteSale.orderSource = 'ecommerce'           
        batch.addTransaction(echeckPreNoteSale)
        
        echeckPreNoteCredit = litleXmlFields.echeckPreNoteCredit();
        echeckPreNoteCredit.orderId = "2"
        echeckPreNoteCredit.billToAddress = contact
        echeckPreNoteCredit.echeck = echeckSuccess
        echeckPreNoteCredit.orderSource = 'ecommerce'         
        batch.addTransaction(echeckPreNoteCredit)
        
        echeckPreNoteSale = litleXmlFields.echeckPreNoteSale();
        echeckPreNoteSale.orderId = "3"
        echeckPreNoteSale.billToAddress = contact
        echeckPreNoteSale.echeck = echeckErr1
        echeckPreNoteSale.orderSource = 'ecommerce'           
        batch.addTransaction(echeckPreNoteSale)
        
        echeckPreNoteCredit = litleXmlFields.echeckPreNoteCredit();
        echeckPreNoteCredit.orderId = "4"
        echeckPreNoteCredit.billToAddress = contact
        echeckPreNoteCredit.echeck = echeckErr1
        echeckPreNoteCredit.orderSource = 'ecommerce'         
        batch.addTransaction(echeckPreNoteCredit)
        
        echeckPreNoteSale = litleXmlFields.echeckPreNoteSale();
        echeckPreNoteSale.orderId = "5"
        echeckPreNoteSale.billToAddress = contact
        echeckPreNoteSale.echeck = echeckErr2
        echeckPreNoteSale.orderSource = 'ecommerce'           
        batch.addTransaction(echeckPreNoteSale)
        
        echeckPreNoteCredit = litleXmlFields.echeckPreNoteCredit();
        echeckPreNoteCredit.orderId = "6"
        echeckPreNoteCredit.billToAddress = contact
        echeckPreNoteCredit.echeck = echeckErr2
        echeckPreNoteCredit.orderSource = 'ecommerce'         
        batch.addTransaction(echeckPreNoteCredit)
 
        transactionCount = batch.numOfTxn
 
        fileResponse = request.sendRequestTCP()
        batchResponse = fileResponse.getNextBatchResponse()
 
        txns = 0
        
        responseDict = {'1':'000','2':'000','3':'900','4':'900','5':'301','6':'301'}

        nextTransaction = True
        
        while nextTransaction:
            try:
                responseTxn = batchResponse.getNextTransaction()
                self.assertEqual(responseTxn.response, responseDict[responseTxn.orderId])
                txns+=1;
            except NoTransactionException:
                nextTransaction = False

        self.assertEqual(transactionCount, txns)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(certTestBatch)
    return suite

if __name__ =='__main__':
    unittest.main()