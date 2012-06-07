import unittest
import TestConfigOverride, TestCreateFromDom, TestLitleOnline

testconfigoverride = TestConfigOverride.suite()
testcreatefromdom = TestCreateFromDom.suite()
testlitleonline = TestLitleOnline.suite()

unittest.TextTestRunner().run(testconfigoverride)
unittest.TextTestRunner().run(testcreatefromdom)
unittest.TextTestRunner().run(testlitleonline)
