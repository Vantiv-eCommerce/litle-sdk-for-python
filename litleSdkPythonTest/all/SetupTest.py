import os, sys,re
import litleSdkPython

from litleSdkPython.litleOnlineRequest import *

try:
    import litleSdkPythonTest.testConfig
except:
    raise Exception('please run setUpTest.py before running tests')
config = litleSdkPythonTest.testConfig.config

class RegexMatcher(object):
    def __init__(self, pattern):
         self.pattern = pattern
    def __eq__(self, other):         
        return re.match(self.pattern,other)
     
