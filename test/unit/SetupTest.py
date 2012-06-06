import os, sys,re
lib_path = os.path.abspath('../../lib')
sys.path.append(lib_path)

from litleOnlineRequest import *

config_path = os.path.abspath('../')
sys.path.append(config_path)
try:
    import testConfig
except:
    raise Exception('please run setUpTest.py before running tests')
config = testConfig.config

class RegexMatcher(object):
    def __init__(self, pattern):
         self.pattern = pattern
    def __eq__(self, other):         
        return re.match(self.pattern,other)
     
