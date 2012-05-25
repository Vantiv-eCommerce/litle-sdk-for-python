import litleXmlFields
from litleXmlFields import authorization, sale, captureGivenAuth, authentication,\
    litleOnlineRequest
import pyxb
#authentication = litleXmlFields.authorization
#authentication
#litleXmlFields.authentication;
#lor = litleXmlFields.litleOnlineRequest()
#litleOnlineRequest.
#auth = litleXmlFields.authentication()
ttwrg =litleXmlFields.transactionTypeWithReportGroup()
auth = litleXmlFields.authentication()
litleXmlFields.Namespace = 'litle'
#auth  = litleXmlFields.authorization.__init__(


lor = litleXmlFields.litleOnlineRequest()
ttwrg.reportGroup = 'Planets'
print ttwrg.toxml()
lor.customerId = '123'
#print lor
authorization = litleXmlFields.authorization()
authentication  = litleXmlFields.CTD_ANON_22()
authentication.user = 'PHXMLTEST'
authentication.password = 'certpass'
authentication.name = 'authorization'
#litleOnlineRequest.abstract()
card = litleXmlFields.cardType()
card.number = "42424242424242424242"
card.expDate = "0912"
card.cardValidationNum = '123'
card.type = 'VI'
print card.toxml()
litleXmlFields.authorization = pyxb.BIND()
ttwrg = litleXmlFields.transactionTypeWithReportGroup()
#order = litleXmlFields.CreateFromDocument(xml_text, default_namespace, location_base)