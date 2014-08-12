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
from mock import *

class TestLitleBatchResponse(unittest.TestCase):
    @patch.object(litleXmlFields, 'CreateFromDocument')
    @patch.object(responseUtil, 'addNamespace')
    def testInit(self,  mock_addNamespace, mock_CreateFromDocument):
        parser = MagicMock()
        parser.getNextTag = MagicMock(return_value = None)
        mock_addNamespace.return_value = None

        batchResponse = litleXmlFields.batchResponse()
        batchResponse.id = '101'
        batchResponse.litleBatchId = 562
        batchResponse.merchantId = '101'

        mock_CreateFromDocument.return_value = batchResponse

        response = litleBatchResponse(parser)
        mock_CreateFromDocument.assert_called_once_with(None)
        mock_addNamespace.assert_called_once_with(None)
        self.assertEqual(response.batchResponse.id, '101')
        self.assertEqual(response.batchResponse.litleBatchId, 562)
        self.assertEqual(response.batchResponse.merchantId, '101')

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLitleBatchResponse)
    return suite