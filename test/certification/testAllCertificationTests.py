import unittest
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