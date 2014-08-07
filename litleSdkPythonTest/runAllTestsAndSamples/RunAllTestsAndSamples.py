import inspect, os, sys


lib_path = os.path.abspath('../unit')
os.chdir(lib_path)
os.system("python `which nosetests` --with-xunit")

lib_path = os.path.abspath('../functional')
os.chdir(lib_path)
os.system("python `which nosetests` --with-xunit")

lib_path = os.path.abspath('../certification')
os.chdir(lib_path)
os.system("python `which nosetests` --with-xunit")

lib_path = os.path.abspath('../../samples/sales')

sys.path.append(lib_path)

import saleExample

lib_path = os.path.abspath('../../samples/credit')
sys.path.append(lib_path)

import creditExample

lib_path = os.path.abspath('../../samples/capture')
sys.path.append(lib_path)

import captureExample

lib_path = os.path.abspath('../../samples/paymentFullCycle')
sys.path.append(lib_path)

import paymentFullCycleExample

lib_path = os.path.abspath('../../samples/avsOnlyTransaction')
sys.path.append(lib_path)

import avsOnlyTransactionExample

lib_path = os.path.abspath('../../samples/captureGivenAuthTransaction')
sys.path.append(lib_path)

import captureGivenAuthTransactionExample

lib_path = os.path.abspath('../../samples/forceCaptureTransaction')
sys.path.append(lib_path)

import forceCaptureTransactionExample

lib_path = os.path.abspath('../../samples/registerToken')
sys.path.append(lib_path)

import registerTokenExample

lib_path = os.path.abspath('../../samples/partialCapture')
sys.path.append(lib_path)

import partialCaptureExample

lib_path = os.path.abspath('../../samples/refundTransactionStandAlone')
sys.path.append(lib_path)

import refundTransactionStandAloneExample

lib_path = os.path.abspath('../../samples/voidTransaction')
sys.path.append(lib_path)

import voidTransactionExample


lib_path = os.path.abspath('../../samples/authorization')
sys.path.append(lib_path)

import authorizationExample


lib_path = os.path.abspath('../../samples/payPageRegisteration')
sys.path.append(lib_path)

import payPageRegisterationExample


lib_path = os.path.abspath('../../samples/saleWithToken')
sys.path.append(lib_path)

import saleWithTokenExample


lib_path = os.path.abspath('../../samples/orphanRefund')
sys.path.append(lib_path)

import orphanRefundExample
