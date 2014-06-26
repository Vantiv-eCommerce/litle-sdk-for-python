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