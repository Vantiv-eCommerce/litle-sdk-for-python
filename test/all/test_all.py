import os, sys
import unittest

# Cert Tests
lib_path = os.path.abspath('../certification')
sys.path.append(lib_path)

import certTest1, certTest2, certTest3, certTest4, certTest5

ct1 = certTest1.suite()
ct2 = certTest2.suite()
ct3 = certTest3.suite()
ct4 = certTest4.suite()
ct5 = certTest5.suite()

unittest.TextTestRunner().run(ct1)
unittest.TextTestRunner().run(ct2)
unittest.TextTestRunner().run(ct3)
unittest.TextTestRunner().run(ct4)
unittest.TextTestRunner().run(ct5)

# Functional Tests
lib_path = os.path.abspath('../functional')
sys.path.append(lib_path)

import TestAuth, TestAuthReversal, TestCapture, TestCaptureGivenAuth, TestCredit
import TestEcheckCredit, TestEcheckRedeposit, TestEcheckSale, TestEcheckVerification
import TestEcheckVoid, TestForceCapture, TestSale, TestToken

testauth = TestAuth.suite()
testauthreverasal = TestAuthReversal.suite()
testcapture = TestCapture.suite()
testcapturegivenauth = TestCaptureGivenAuth.suite()
testcredit = TestCredit.suite()

testecheckcredit = TestEcheckCredit.suite()
testecheckredeposit = TestEcheckRedeposit.suite()
testechecksale = TestEcheckSale.suite()
testecheckverfication = TestEcheckVerification.suite()

testecheckvoid = TestEcheckVoid.suite()
testforcecapture = TestForceCapture.suite()
testsale = TestSale.suite()
testtoken = TestToken.suite()

unittest.TextTestRunner().run(testauth)
unittest.TextTestRunner().run(testauthreverasal)
unittest.TextTestRunner().run(testcapture)
unittest.TextTestRunner().run(testcapturegivenauth)
unittest.TextTestRunner().run(testcredit)

unittest.TextTestRunner().run(testecheckcredit)
unittest.TextTestRunner().run(testecheckredeposit)
unittest.TextTestRunner().run(testechecksale)
unittest.TextTestRunner().run(testecheckverfication)

unittest.TextTestRunner().run(testecheckvoid)
unittest.TextTestRunner().run(testforcecapture)
unittest.TextTestRunner().run(testsale)
unittest.TextTestRunner().run(testtoken)

# Unit Tests
lib_path = os.path.abspath('../unit')
sys.path.append(lib_path)

