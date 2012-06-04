import os, sys
lib_path = os.path.abspath('../../lib')
sys.path.append(lib_path)

from litleOnlineRequest import *


config = Configuration()
config.setPassword('certpass')
config.setUser('PHXMLTEST')
config.setMerchantId('101')
config.setReportGroup('Planets')
config.setProxy('smoothproxy:8080')
config.setUrl('Sandbox')

