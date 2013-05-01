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

import unittest
import TestAuth
import TestAuthReversal
import TestCapture
import TestCaptureGivenAuth
import TestCredit
import TestEcheckCredit
import TestEcheckRedeposit
import TestEcheckSale
import TestEcheckVerification
import TestEcheckVoid
import TestForceCapture
import TestSale
import TestToken

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

testutf8 = TestUtf8.suite()

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

unittest.TextTestRunner().run(testutf8)