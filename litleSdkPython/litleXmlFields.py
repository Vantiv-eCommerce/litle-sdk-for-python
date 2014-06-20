# ./tempgen.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f03bd2be92cca0df00d3d054794f8a47756ec009
# Generated 2014-06-13 12:24:00.558365 by PyXB version 1.1.5
# Namespace http://www.litle.com/schema

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import xml.dom

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1ff22574-f317-11e3-af96-001a4a010645')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.litle.com/schema', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if (True):
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
   
   
   
   

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return LitleAnyCreateFromDOM(pyxb.binding.basis.element,node, _fallback_namespace=default_namespace)

def LitleAnyCreateFromDOM (cls, node, _fallback_namespace):
    if xml.dom.Node.DOCUMENT_NODE == node.nodeType:
        node = node.documentElement
    expanded_name = pyxb.namespace.ExpandedName(node, fallback_namespace=_fallback_namespace)
    elt = expanded_name.elementBinding()
    if elt is None:
        return
    assert isinstance(elt, pyxb.binding.basis.element)
    return elt._createFromDOM(node, expanded_name, _fallback_namespace=_fallback_namespace)


# Atomic simple type: {http://www.litle.com/schema}litleIdType
class litleIdType (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'litleIdType')
    _Documentation = None
litleIdType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(19L))
litleIdType._InitializeFacetMap(litleIdType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', u'litleIdType', litleIdType)

# Atomic simple type: {http://www.litle.com/schema}string25Type
class string25Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'string25Type')
    _Documentation = None
string25Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
string25Type._InitializeFacetMap(string25Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'string25Type', string25Type)

# Atomic simple type: {http://www.litle.com/schema}customerIdType
class customerIdType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customerIdType')
    _Documentation = None
customerIdType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
customerIdType._InitializeFacetMap(customerIdType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'customerIdType', customerIdType)

# Atomic simple type: {http://www.litle.com/schema}reportGroupType
class reportGroupType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reportGroupType')
    _Documentation = None
reportGroupType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
reportGroupType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
reportGroupType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
reportGroupType._InitializeFacetMap(reportGroupType._CF_whiteSpace,
   reportGroupType._CF_minLength,
   reportGroupType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'reportGroupType', reportGroupType)

# Atomic simple type: {http://www.litle.com/schema}routingNumberType
class routingNumberType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'routingNumberType')
    _Documentation = None
routingNumberType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(9L))
routingNumberType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9L))
routingNumberType._InitializeFacetMap(routingNumberType._CF_minLength,
   routingNumberType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'routingNumberType', routingNumberType)

# Atomic simple type: {http://www.litle.com/schema}checkNumberType
class checkNumberType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'checkNumberType')
    _Documentation = None
checkNumberType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
checkNumberType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15L))
checkNumberType._InitializeFacetMap(checkNumberType._CF_minLength,
   checkNumberType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'checkNumberType', checkNumberType)

# Atomic simple type: {http://www.litle.com/schema}ccAccountNumberType
class ccAccountNumberType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ccAccountNumberType')
    _Documentation = None
ccAccountNumberType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(13L))
ccAccountNumberType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
ccAccountNumberType._InitializeFacetMap(ccAccountNumberType._CF_minLength,
   ccAccountNumberType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'ccAccountNumberType', ccAccountNumberType)

# Atomic simple type: {http://www.litle.com/schema}echeckAccountNumberType
class echeckAccountNumberType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'echeckAccountNumberType')
    _Documentation = None
echeckAccountNumberType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(17L))
echeckAccountNumberType._InitializeFacetMap(echeckAccountNumberType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'echeckAccountNumberType', echeckAccountNumberType)

# Atomic simple type: {http://www.litle.com/schema}nameType
class nameType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameType')
    _Documentation = None
nameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
nameType._InitializeFacetMap(nameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'nameType', nameType)

# Atomic simple type: {http://www.litle.com/schema}trackDataType
class trackDataType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'trackDataType')
    _Documentation = None
trackDataType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
trackDataType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
trackDataType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256L))
trackDataType._InitializeFacetMap(trackDataType._CF_whiteSpace,
   trackDataType._CF_minLength,
   trackDataType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'trackDataType', trackDataType)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(4L))
STD_ANON._InitializeFacetMap(STD_ANON._CF_totalDigits)

# Atomic simple type: {http://www.litle.com/schema}messageType
class messageType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'messageType')
    _Documentation = None
messageType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(512L))
messageType._InitializeFacetMap(messageType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'messageType', messageType)

# Atomic simple type: {http://www.litle.com/schema}versionType
class versionType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'versionType')
    _Documentation = None
versionType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
versionType._InitializeFacetMap(versionType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'versionType', versionType)

# Atomic simple type: {http://www.litle.com/schema}responseType
class responseType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'responseType')
    _Documentation = None
responseType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
responseType._InitializeFacetMap(responseType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'responseType', responseType)

# Atomic simple type: {http://www.litle.com/schema}numberOfPaymentsType
class numberOfPaymentsType (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'numberOfPaymentsType')
    _Documentation = None
numberOfPaymentsType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=numberOfPaymentsType, value=pyxb.binding.datatypes.integer(99L))
numberOfPaymentsType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=numberOfPaymentsType, value=pyxb.binding.datatypes.integer(1L))
numberOfPaymentsType._InitializeFacetMap(numberOfPaymentsType._CF_maxInclusive,
   numberOfPaymentsType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'numberOfPaymentsType', numberOfPaymentsType)

# Atomic simple type: {http://www.litle.com/schema}authCodeType
class authCodeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'authCodeType')
    _Documentation = None
authCodeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(6L))
authCodeType._InitializeFacetMap(authCodeType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'authCodeType', authCodeType)

# Atomic simple type: {http://www.litle.com/schema}trialIntervalTypeEnum
class trialIntervalTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'trialIntervalTypeEnum')
    _Documentation = None
trialIntervalTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=trialIntervalTypeEnum, enum_prefix=None)
trialIntervalTypeEnum.MONTH = trialIntervalTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MONTH', tag=u'MONTH')
trialIntervalTypeEnum.DAY = trialIntervalTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DAY', tag=u'DAY')
trialIntervalTypeEnum._InitializeFacetMap(trialIntervalTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'trialIntervalTypeEnum', trialIntervalTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}string2Type
class string2Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'string2Type')
    _Documentation = None
string2Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
string2Type._InitializeFacetMap(string2Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'string2Type', string2Type)

# Atomic simple type: {http://www.litle.com/schema}payPalNotesType
class payPalNotesType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'payPalNotesType')
    _Documentation = None
payPalNotesType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255L))
payPalNotesType._InitializeFacetMap(payPalNotesType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'payPalNotesType', payPalNotesType)

# Atomic simple type: {http://www.litle.com/schema}transactionAmountType
class transactionAmountType (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'transactionAmountType')
    _Documentation = None
transactionAmountType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
transactionAmountType._InitializeFacetMap(transactionAmountType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', u'transactionAmountType', transactionAmountType)

# Atomic simple type: {http://www.litle.com/schema}riskEstimator
class riskEstimator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'riskEstimator')
    _Documentation = None
riskEstimator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
riskEstimator._InitializeFacetMap(riskEstimator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'riskEstimator', riskEstimator)

# Atomic simple type: {http://www.litle.com/schema}cardNumberLast4Type
class cardNumberLast4Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cardNumberLast4Type')
    _Documentation = None
cardNumberLast4Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
cardNumberLast4Type._InitializeFacetMap(cardNumberLast4Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'cardNumberLast4Type', cardNumberLast4Type)

# Atomic simple type: {http://www.litle.com/schema}orderSourceType
class orderSourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'orderSourceType')
    _Documentation = None
orderSourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=orderSourceType, enum_prefix=None)
orderSourceType.ecommerce = orderSourceType._CF_enumeration.addEnumeration(unicode_value=u'ecommerce', tag=u'ecommerce')
orderSourceType.installment = orderSourceType._CF_enumeration.addEnumeration(unicode_value=u'installment', tag=u'installment')
orderSourceType.mailorder = orderSourceType._CF_enumeration.addEnumeration(unicode_value=u'mailorder', tag=u'mailorder')
orderSourceType.recurring = orderSourceType._CF_enumeration.addEnumeration(unicode_value=u'recurring', tag=u'recurring')
orderSourceType.retail = orderSourceType._CF_enumeration.addEnumeration(unicode_value=u'retail', tag=u'retail')
orderSourceType.telephone = orderSourceType._CF_enumeration.addEnumeration(unicode_value=u'telephone', tag=u'telephone')
orderSourceType.n3dsAuthenticated = orderSourceType._CF_enumeration.addEnumeration(unicode_value=u'3dsAuthenticated', tag=u'n3dsAuthenticated')
orderSourceType.n3dsAttempted = orderSourceType._CF_enumeration.addEnumeration(unicode_value=u'3dsAttempted', tag=u'n3dsAttempted')
orderSourceType.recurringtel = orderSourceType._CF_enumeration.addEnumeration(unicode_value=u'recurringtel', tag=u'recurringtel')
orderSourceType._InitializeFacetMap(orderSourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'orderSourceType', orderSourceType)

# Atomic simple type: {http://www.litle.com/schema}redeliveryCycle
class redeliveryCycle (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'redeliveryCycle')
    _Documentation = None
redeliveryCycle._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(1L))
redeliveryCycle._InitializeFacetMap(redeliveryCycle._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', u'redeliveryCycle', redeliveryCycle)

# Atomic simple type: {http://www.litle.com/schema}authenticationTransactionIdType
class authenticationTransactionIdType (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'authenticationTransactionIdType')
    _Documentation = None
authenticationTransactionIdType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(28L))
authenticationTransactionIdType._InitializeFacetMap(authenticationTransactionIdType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'authenticationTransactionIdType', authenticationTransactionIdType)

# Atomic simple type: {http://www.litle.com/schema}numberOfDeposits
class numberOfDeposits (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'numberOfDeposits')
    _Documentation = None
numberOfDeposits._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(1L))
numberOfDeposits._InitializeFacetMap(numberOfDeposits._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', u'numberOfDeposits', numberOfDeposits)

# Atomic simple type: {http://www.litle.com/schema}batchTotalAmountType
class batchTotalAmountType (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'batchTotalAmountType')
    _Documentation = None
batchTotalAmountType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(10L))
batchTotalAmountType._InitializeFacetMap(batchTotalAmountType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', u'batchTotalAmountType', batchTotalAmountType)

# Atomic simple type: {http://www.litle.com/schema}merchantIdentificationType
class merchantIdentificationType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'merchantIdentificationType')
    _Documentation = None
merchantIdentificationType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
merchantIdentificationType._InitializeFacetMap(merchantIdentificationType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'merchantIdentificationType', merchantIdentificationType)

# Atomic simple type: {http://www.litle.com/schema}companyName
class companyName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'companyName')
    _Documentation = None
companyName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40L))
companyName._InitializeFacetMap(companyName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'companyName', companyName)

# Atomic simple type: {http://www.litle.com/schema}virtualAuthenticationKeyData
class virtualAuthenticationKeyData (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualAuthenticationKeyData')
    _Documentation = None
virtualAuthenticationKeyData._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
virtualAuthenticationKeyData._InitializeFacetMap(virtualAuthenticationKeyData._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'virtualAuthenticationKeyData', virtualAuthenticationKeyData)

# Atomic simple type: {http://www.litle.com/schema}addressLineType
class addressLineType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'addressLineType')
    _Documentation = None
addressLineType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35L))
addressLineType._InitializeFacetMap(addressLineType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'addressLineType', addressLineType)

# Atomic simple type: {http://www.litle.com/schema}cvNumType
class cvNumType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cvNumType')
    _Documentation = None
cvNumType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
cvNumType._InitializeFacetMap(cvNumType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'cvNumType', cvNumType)

# Atomic simple type: {http://www.litle.com/schema}template
class template (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'template')
    _Documentation = None
template._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
template._InitializeFacetMap(template._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'template', template)

# Atomic simple type: {http://www.litle.com/schema}threatMetrixSessionIdType
class threatMetrixSessionIdType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'threatMetrixSessionIdType')
    _Documentation = None
threatMetrixSessionIdType._CF_pattern = pyxb.binding.facets.CF_pattern()
threatMetrixSessionIdType._CF_pattern.addPattern(pattern=u'[-a-zA-Z0-9_]{1,128}')
threatMetrixSessionIdType._InitializeFacetMap(threatMetrixSessionIdType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'threatMetrixSessionIdType', threatMetrixSessionIdType)

# Atomic simple type: {http://www.litle.com/schema}commodityCodeType
class commodityCodeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'commodityCodeType')
    _Documentation = None
commodityCodeType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
commodityCodeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12L))
commodityCodeType._InitializeFacetMap(commodityCodeType._CF_minLength,
   commodityCodeType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'commodityCodeType', commodityCodeType)

# Atomic simple type: {http://www.litle.com/schema}unitCostType
class unitCostType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unitCostType')
    _Documentation = None
unitCostType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=unitCostType, value=pyxb.binding.datatypes.decimal(0.0))
unitCostType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
unitCostType._InitializeFacetMap(unitCostType._CF_minInclusive,
   unitCostType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', u'unitCostType', unitCostType)

# Atomic simple type: {http://www.litle.com/schema}methodOfPaymentTypeEnum
class methodOfPaymentTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'methodOfPaymentTypeEnum')
    _Documentation = None
methodOfPaymentTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=methodOfPaymentTypeEnum, enum_prefix=None)
methodOfPaymentTypeEnum.MC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MC', tag=u'MC')
methodOfPaymentTypeEnum.VI = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VI', tag=u'VI')
methodOfPaymentTypeEnum.AX = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AX', tag=u'AX')
methodOfPaymentTypeEnum.DC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DC', tag=u'DC')
methodOfPaymentTypeEnum.DI = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DI', tag=u'DI')
methodOfPaymentTypeEnum.PP = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PP', tag=u'PP')
methodOfPaymentTypeEnum.JC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'JC', tag=u'JC')
methodOfPaymentTypeEnum.BL = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BL', tag=u'BL')
methodOfPaymentTypeEnum.EC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'EC', tag=u'EC')
methodOfPaymentTypeEnum.GC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GC', tag=u'GC')
methodOfPaymentTypeEnum.emptyString = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'', tag='emptyString')
methodOfPaymentTypeEnum._InitializeFacetMap(methodOfPaymentTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'methodOfPaymentTypeEnum', methodOfPaymentTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}actionReasonType
class actionReasonType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'actionReasonType')
    _Documentation = None
actionReasonType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255L))
actionReasonType._InitializeFacetMap(actionReasonType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'actionReasonType', actionReasonType)

# Atomic simple type: {http://www.litle.com/schema}echeckAccountTypeEnum
class echeckAccountTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'echeckAccountTypeEnum')
    _Documentation = None
echeckAccountTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=echeckAccountTypeEnum, enum_prefix=None)
echeckAccountTypeEnum.Checking = echeckAccountTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'Checking', tag=u'Checking')
echeckAccountTypeEnum.Savings = echeckAccountTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'Savings', tag=u'Savings')
echeckAccountTypeEnum.Corporate = echeckAccountTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'Corporate', tag=u'Corporate')
echeckAccountTypeEnum.Corp_Savings = echeckAccountTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'Corp Savings', tag=u'Corp_Savings')
echeckAccountTypeEnum._InitializeFacetMap(echeckAccountTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'echeckAccountTypeEnum', echeckAccountTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}unitOfMeasureType
class unitOfMeasureType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'unitOfMeasureType')
    _Documentation = None
unitOfMeasureType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
unitOfMeasureType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12L))
unitOfMeasureType._InitializeFacetMap(unitOfMeasureType._CF_minLength,
   unitOfMeasureType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'unitOfMeasureType', unitOfMeasureType)

# Atomic simple type: {http://www.litle.com/schema}customBillingPhoneType
class customBillingPhoneType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customBillingPhoneType')
    _Documentation = None
customBillingPhoneType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13L))
customBillingPhoneType._CF_pattern = pyxb.binding.facets.CF_pattern()
customBillingPhoneType._CF_pattern.addPattern(pattern=u'[0-9]*')
customBillingPhoneType._InitializeFacetMap(customBillingPhoneType._CF_maxLength,
   customBillingPhoneType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'customBillingPhoneType', customBillingPhoneType)

# Atomic simple type: {http://www.litle.com/schema}string256Type
class string256Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'string256Type')
    _Documentation = None
string256Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256L))
string256Type._InitializeFacetMap(string256Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'string256Type', string256Type)

# Atomic simple type: {http://www.litle.com/schema}descriptorType
class descriptorType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'descriptorType')
    _Documentation = None
descriptorType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
descriptorType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
descriptorType._CF_pattern = pyxb.binding.facets.CF_pattern()
descriptorType._CF_pattern.addPattern(pattern=u"[A-Z,a-z,0-9, ,\\*,,,\\-,',#,&,.]*")
descriptorType._InitializeFacetMap(descriptorType._CF_minLength,
   descriptorType._CF_maxLength,
   descriptorType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'descriptorType', descriptorType)

# Atomic simple type: {http://www.litle.com/schema}recycleByTypeEnum
class recycleByTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recycleByTypeEnum')
    _Documentation = None
recycleByTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=recycleByTypeEnum, enum_prefix=None)
recycleByTypeEnum.Merchant = recycleByTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'Merchant', tag=u'Merchant')
recycleByTypeEnum.Litle = recycleByTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'Litle', tag=u'Litle')
recycleByTypeEnum.None_ = recycleByTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'None', tag=u'None_')
recycleByTypeEnum._InitializeFacetMap(recycleByTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'recycleByTypeEnum', recycleByTypeEnum)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_length)

# Atomic simple type: {http://www.litle.com/schema}affluenceTypeEnum
class affluenceTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'affluenceTypeEnum')
    _Documentation = None
affluenceTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=affluenceTypeEnum, enum_prefix=None)
affluenceTypeEnum.AFFLUENT = affluenceTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AFFLUENT', tag=u'AFFLUENT')
affluenceTypeEnum.MASS_AFFLUENT = affluenceTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MASS AFFLUENT', tag=u'MASS_AFFLUENT')
affluenceTypeEnum._InitializeFacetMap(affluenceTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'affluenceTypeEnum', affluenceTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}customBillingCityType
class customBillingCityType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customBillingCityType')
    _Documentation = None
customBillingCityType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35L))
customBillingCityType._InitializeFacetMap(customBillingCityType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'customBillingCityType', customBillingCityType)

# Atomic simple type: {http://www.litle.com/schema}customBillingUrlType
class customBillingUrlType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customBillingUrlType')
    _Documentation = None
customBillingUrlType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13L))
customBillingUrlType._CF_pattern = pyxb.binding.facets.CF_pattern()
customBillingUrlType._CF_pattern.addPattern(pattern=u'[A-Z,a-z,0-9,/,\\-,_,.]*')
customBillingUrlType._InitializeFacetMap(customBillingUrlType._CF_maxLength,
   customBillingUrlType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'customBillingUrlType', customBillingUrlType)

# Atomic simple type: {http://www.litle.com/schema}addressIndicator
class addressIndicator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'addressIndicator')
    _Documentation = None
addressIndicator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
addressIndicator._InitializeFacetMap(addressIndicator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'addressIndicator', addressIndicator)

# Atomic simple type: {http://www.litle.com/schema}posCatLevelEnum
class posCatLevelEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'posCatLevelEnum')
    _Documentation = None
posCatLevelEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=posCatLevelEnum, enum_prefix=None)
posCatLevelEnum.self_service = posCatLevelEnum._CF_enumeration.addEnumeration(unicode_value=u'self service', tag=u'self_service')
posCatLevelEnum._InitializeFacetMap(posCatLevelEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'posCatLevelEnum', posCatLevelEnum)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_2._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_2._CF_pattern.addPattern(pattern=u'(\\d{5})?\\d{4}')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_pattern)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.CNC = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'CNC', tag=u'CNC')
STD_ANON_3.DIG = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'DIG', tag=u'DIG')
STD_ANON_3.PHY = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'PHY', tag=u'PHY')
STD_ANON_3.SVC = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'SVC', tag=u'SVC')
STD_ANON_3.TBD = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'TBD', tag=u'TBD')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: {http://www.litle.com/schema}string50Type
class string50Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'string50Type')
    _Documentation = None
string50Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
string50Type._InitializeFacetMap(string50Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'string50Type', string50Type)

# Atomic simple type: {http://www.litle.com/schema}string3Type
class string3Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'string3Type')
    _Documentation = None
string3Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
string3Type._InitializeFacetMap(string3Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'string3Type', string3Type)

# Atomic simple type: {http://www.litle.com/schema}cardProductTypeEnum
class cardProductTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cardProductTypeEnum')
    _Documentation = None
cardProductTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=cardProductTypeEnum, enum_prefix=None)
cardProductTypeEnum.UNKNOWN = cardProductTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWN', tag=u'UNKNOWN')
cardProductTypeEnum.COMMERCIAL = cardProductTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'COMMERCIAL', tag=u'COMMERCIAL')
cardProductTypeEnum.CONSUMER = cardProductTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CONSUMER', tag=u'CONSUMER')
cardProductTypeEnum._InitializeFacetMap(cardProductTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'cardProductTypeEnum', cardProductTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}zipType
class zipType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'zipType')
    _Documentation = None
zipType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
zipType._InitializeFacetMap(zipType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'zipType', zipType)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.New = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'New', tag=u'New')
STD_ANON_4.Existing = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'Existing', tag=u'Existing')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: {http://www.litle.com/schema}riskQueueAssignment
class riskQueueAssignment (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'riskQueueAssignment')
    _Documentation = None
riskQueueAssignment._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
riskQueueAssignment._InitializeFacetMap(riskQueueAssignment._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'riskQueueAssignment', riskQueueAssignment)

# Atomic simple type: {http://www.litle.com/schema}string20Type
class string20Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'string20Type')
    _Documentation = None
string20Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
string20Type._InitializeFacetMap(string20Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'string20Type', string20Type)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.Own = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'Own', tag=u'Own')
STD_ANON_5.Rent = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'Rent', tag=u'Rent')
STD_ANON_5.Other = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'Other', tag=u'Other')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)

# Atomic simple type: {http://www.litle.com/schema}countryTypeEnum
class countryTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'countryTypeEnum')
    _Documentation = None
countryTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=countryTypeEnum, enum_prefix=None)
countryTypeEnum.USA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'USA', tag=u'USA')
countryTypeEnum.AF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AF', tag=u'AF')
countryTypeEnum.AX = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AX', tag=u'AX')
countryTypeEnum.AL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AL', tag=u'AL')
countryTypeEnum.DZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DZ', tag=u'DZ')
countryTypeEnum.AS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AS', tag=u'AS')
countryTypeEnum.AD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AD', tag=u'AD')
countryTypeEnum.AO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AO', tag=u'AO')
countryTypeEnum.AI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AI', tag=u'AI')
countryTypeEnum.AQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AQ', tag=u'AQ')
countryTypeEnum.AG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AG', tag=u'AG')
countryTypeEnum.AR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AR', tag=u'AR')
countryTypeEnum.AM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AM', tag=u'AM')
countryTypeEnum.AW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AW', tag=u'AW')
countryTypeEnum.AU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AU', tag=u'AU')
countryTypeEnum.AT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AT', tag=u'AT')
countryTypeEnum.AZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AZ', tag=u'AZ')
countryTypeEnum.BS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BS', tag=u'BS')
countryTypeEnum.BH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BH', tag=u'BH')
countryTypeEnum.BD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BD', tag=u'BD')
countryTypeEnum.BB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BB', tag=u'BB')
countryTypeEnum.BY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BY', tag=u'BY')
countryTypeEnum.BE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BE', tag=u'BE')
countryTypeEnum.BZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BZ', tag=u'BZ')
countryTypeEnum.BJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BJ', tag=u'BJ')
countryTypeEnum.BM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BM', tag=u'BM')
countryTypeEnum.BT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BT', tag=u'BT')
countryTypeEnum.BO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BO', tag=u'BO')
countryTypeEnum.BQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BQ', tag=u'BQ')
countryTypeEnum.BA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BA', tag=u'BA')
countryTypeEnum.BW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BW', tag=u'BW')
countryTypeEnum.BV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BV', tag=u'BV')
countryTypeEnum.BR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BR', tag=u'BR')
countryTypeEnum.IO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IO', tag=u'IO')
countryTypeEnum.BN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BN', tag=u'BN')
countryTypeEnum.BG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BG', tag=u'BG')
countryTypeEnum.BF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BF', tag=u'BF')
countryTypeEnum.BI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BI', tag=u'BI')
countryTypeEnum.KH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KH', tag=u'KH')
countryTypeEnum.CM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CM', tag=u'CM')
countryTypeEnum.CA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CA', tag=u'CA')
countryTypeEnum.CV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CV', tag=u'CV')
countryTypeEnum.KY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KY', tag=u'KY')
countryTypeEnum.CF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CF', tag=u'CF')
countryTypeEnum.TD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TD', tag=u'TD')
countryTypeEnum.CL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CL', tag=u'CL')
countryTypeEnum.CN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CN', tag=u'CN')
countryTypeEnum.CX = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CX', tag=u'CX')
countryTypeEnum.CC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CC', tag=u'CC')
countryTypeEnum.CO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CO', tag=u'CO')
countryTypeEnum.KM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KM', tag=u'KM')
countryTypeEnum.CG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CG', tag=u'CG')
countryTypeEnum.CD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CD', tag=u'CD')
countryTypeEnum.CK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CK', tag=u'CK')
countryTypeEnum.CR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CR', tag=u'CR')
countryTypeEnum.CI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CI', tag=u'CI')
countryTypeEnum.HR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HR', tag=u'HR')
countryTypeEnum.CU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CU', tag=u'CU')
countryTypeEnum.CW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CW', tag=u'CW')
countryTypeEnum.CY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CY', tag=u'CY')
countryTypeEnum.CZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CZ', tag=u'CZ')
countryTypeEnum.DK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DK', tag=u'DK')
countryTypeEnum.DJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DJ', tag=u'DJ')
countryTypeEnum.DM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DM', tag=u'DM')
countryTypeEnum.DO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DO', tag=u'DO')
countryTypeEnum.TL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TL', tag=u'TL')
countryTypeEnum.EC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'EC', tag=u'EC')
countryTypeEnum.EG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'EG', tag=u'EG')
countryTypeEnum.SV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SV', tag=u'SV')
countryTypeEnum.GQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GQ', tag=u'GQ')
countryTypeEnum.ER = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ER', tag=u'ER')
countryTypeEnum.EE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'EE', tag=u'EE')
countryTypeEnum.ET = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ET', tag=u'ET')
countryTypeEnum.FK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FK', tag=u'FK')
countryTypeEnum.FO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FO', tag=u'FO')
countryTypeEnum.FJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FJ', tag=u'FJ')
countryTypeEnum.FI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FI', tag=u'FI')
countryTypeEnum.FR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FR', tag=u'FR')
countryTypeEnum.GF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GF', tag=u'GF')
countryTypeEnum.PF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PF', tag=u'PF')
countryTypeEnum.TF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TF', tag=u'TF')
countryTypeEnum.GA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GA', tag=u'GA')
countryTypeEnum.GM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GM', tag=u'GM')
countryTypeEnum.GE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GE', tag=u'GE')
countryTypeEnum.DE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DE', tag=u'DE')
countryTypeEnum.GH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GH', tag=u'GH')
countryTypeEnum.GI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GI', tag=u'GI')
countryTypeEnum.GR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GR', tag=u'GR')
countryTypeEnum.GL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GL', tag=u'GL')
countryTypeEnum.GD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GD', tag=u'GD')
countryTypeEnum.GP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GP', tag=u'GP')
countryTypeEnum.GU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GU', tag=u'GU')
countryTypeEnum.GT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GT', tag=u'GT')
countryTypeEnum.GG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GG', tag=u'GG')
countryTypeEnum.GN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GN', tag=u'GN')
countryTypeEnum.GW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GW', tag=u'GW')
countryTypeEnum.GY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GY', tag=u'GY')
countryTypeEnum.HT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HT', tag=u'HT')
countryTypeEnum.HM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HM', tag=u'HM')
countryTypeEnum.HN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HN', tag=u'HN')
countryTypeEnum.HK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HK', tag=u'HK')
countryTypeEnum.HU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HU', tag=u'HU')
countryTypeEnum.IS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IS', tag=u'IS')
countryTypeEnum.IN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IN', tag=u'IN')
countryTypeEnum.ID = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ID', tag=u'ID')
countryTypeEnum.IR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IR', tag=u'IR')
countryTypeEnum.IQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IQ', tag=u'IQ')
countryTypeEnum.IE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IE', tag=u'IE')
countryTypeEnum.IM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IM', tag=u'IM')
countryTypeEnum.IL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IL', tag=u'IL')
countryTypeEnum.IT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IT', tag=u'IT')
countryTypeEnum.JM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'JM', tag=u'JM')
countryTypeEnum.JP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'JP', tag=u'JP')
countryTypeEnum.JE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'JE', tag=u'JE')
countryTypeEnum.JO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'JO', tag=u'JO')
countryTypeEnum.KZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KZ', tag=u'KZ')
countryTypeEnum.KE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KE', tag=u'KE')
countryTypeEnum.KI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KI', tag=u'KI')
countryTypeEnum.KP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KP', tag=u'KP')
countryTypeEnum.KR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KR', tag=u'KR')
countryTypeEnum.KW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KW', tag=u'KW')
countryTypeEnum.KG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KG', tag=u'KG')
countryTypeEnum.LA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LA', tag=u'LA')
countryTypeEnum.LV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LV', tag=u'LV')
countryTypeEnum.LB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LB', tag=u'LB')
countryTypeEnum.LS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LS', tag=u'LS')
countryTypeEnum.LR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LR', tag=u'LR')
countryTypeEnum.LY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LY', tag=u'LY')
countryTypeEnum.LI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LI', tag=u'LI')
countryTypeEnum.LT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LT', tag=u'LT')
countryTypeEnum.LU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LU', tag=u'LU')
countryTypeEnum.MO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MO', tag=u'MO')
countryTypeEnum.MK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MK', tag=u'MK')
countryTypeEnum.MG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MG', tag=u'MG')
countryTypeEnum.MW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MW', tag=u'MW')
countryTypeEnum.MY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MY', tag=u'MY')
countryTypeEnum.MV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MV', tag=u'MV')
countryTypeEnum.ML = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ML', tag=u'ML')
countryTypeEnum.MT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MT', tag=u'MT')
countryTypeEnum.MH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MH', tag=u'MH')
countryTypeEnum.MQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MQ', tag=u'MQ')
countryTypeEnum.MR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MR', tag=u'MR')
countryTypeEnum.MU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MU', tag=u'MU')
countryTypeEnum.YT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'YT', tag=u'YT')
countryTypeEnum.MX = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MX', tag=u'MX')
countryTypeEnum.FM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FM', tag=u'FM')
countryTypeEnum.MD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MD', tag=u'MD')
countryTypeEnum.MC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MC', tag=u'MC')
countryTypeEnum.MN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MN', tag=u'MN')
countryTypeEnum.MS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MS', tag=u'MS')
countryTypeEnum.MA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MA', tag=u'MA')
countryTypeEnum.MZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MZ', tag=u'MZ')
countryTypeEnum.MM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MM', tag=u'MM')
countryTypeEnum.NA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NA', tag=u'NA')
countryTypeEnum.NR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NR', tag=u'NR')
countryTypeEnum.NP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NP', tag=u'NP')
countryTypeEnum.NL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NL', tag=u'NL')
countryTypeEnum.AN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AN', tag=u'AN')
countryTypeEnum.NC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NC', tag=u'NC')
countryTypeEnum.NZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NZ', tag=u'NZ')
countryTypeEnum.NI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NI', tag=u'NI')
countryTypeEnum.NE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NE', tag=u'NE')
countryTypeEnum.NG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NG', tag=u'NG')
countryTypeEnum.NU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NU', tag=u'NU')
countryTypeEnum.NF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NF', tag=u'NF')
countryTypeEnum.MP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MP', tag=u'MP')
countryTypeEnum.NO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NO', tag=u'NO')
countryTypeEnum.OM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'OM', tag=u'OM')
countryTypeEnum.PK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PK', tag=u'PK')
countryTypeEnum.PW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PW', tag=u'PW')
countryTypeEnum.PS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PS', tag=u'PS')
countryTypeEnum.PA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PA', tag=u'PA')
countryTypeEnum.PG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PG', tag=u'PG')
countryTypeEnum.PY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PY', tag=u'PY')
countryTypeEnum.PE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PE', tag=u'PE')
countryTypeEnum.PH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PH', tag=u'PH')
countryTypeEnum.PN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PN', tag=u'PN')
countryTypeEnum.PL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PL', tag=u'PL')
countryTypeEnum.PT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PT', tag=u'PT')
countryTypeEnum.PR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PR', tag=u'PR')
countryTypeEnum.QA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'QA', tag=u'QA')
countryTypeEnum.RE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'RE', tag=u'RE')
countryTypeEnum.RO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'RO', tag=u'RO')
countryTypeEnum.RU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'RU', tag=u'RU')
countryTypeEnum.RW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'RW', tag=u'RW')
countryTypeEnum.BL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BL', tag=u'BL')
countryTypeEnum.KN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KN', tag=u'KN')
countryTypeEnum.LC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LC', tag=u'LC')
countryTypeEnum.MF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MF', tag=u'MF')
countryTypeEnum.VC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VC', tag=u'VC')
countryTypeEnum.WS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'WS', tag=u'WS')
countryTypeEnum.SM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SM', tag=u'SM')
countryTypeEnum.ST = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ST', tag=u'ST')
countryTypeEnum.SA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SA', tag=u'SA')
countryTypeEnum.SN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SN', tag=u'SN')
countryTypeEnum.SC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SC', tag=u'SC')
countryTypeEnum.SL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SL', tag=u'SL')
countryTypeEnum.SG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SG', tag=u'SG')
countryTypeEnum.SX = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SX', tag=u'SX')
countryTypeEnum.SK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SK', tag=u'SK')
countryTypeEnum.SI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SI', tag=u'SI')
countryTypeEnum.SB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SB', tag=u'SB')
countryTypeEnum.SO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SO', tag=u'SO')
countryTypeEnum.ZA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ZA', tag=u'ZA')
countryTypeEnum.GS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GS', tag=u'GS')
countryTypeEnum.ES = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ES', tag=u'ES')
countryTypeEnum.LK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LK', tag=u'LK')
countryTypeEnum.SH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SH', tag=u'SH')
countryTypeEnum.PM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PM', tag=u'PM')
countryTypeEnum.SD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SD', tag=u'SD')
countryTypeEnum.SR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SR', tag=u'SR')
countryTypeEnum.SJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SJ', tag=u'SJ')
countryTypeEnum.SZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SZ', tag=u'SZ')
countryTypeEnum.SE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SE', tag=u'SE')
countryTypeEnum.CH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CH', tag=u'CH')
countryTypeEnum.SY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SY', tag=u'SY')
countryTypeEnum.TW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TW', tag=u'TW')
countryTypeEnum.TJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TJ', tag=u'TJ')
countryTypeEnum.TZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TZ', tag=u'TZ')
countryTypeEnum.TH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TH', tag=u'TH')
countryTypeEnum.TG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TG', tag=u'TG')
countryTypeEnum.TK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TK', tag=u'TK')
countryTypeEnum.TO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TO', tag=u'TO')
countryTypeEnum.TT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TT', tag=u'TT')
countryTypeEnum.TN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TN', tag=u'TN')
countryTypeEnum.TR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TR', tag=u'TR')
countryTypeEnum.TM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TM', tag=u'TM')
countryTypeEnum.TC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TC', tag=u'TC')
countryTypeEnum.TV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TV', tag=u'TV')
countryTypeEnum.UG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UG', tag=u'UG')
countryTypeEnum.UA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UA', tag=u'UA')
countryTypeEnum.AE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AE', tag=u'AE')
countryTypeEnum.GB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GB', tag=u'GB')
countryTypeEnum.US = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'US', tag=u'US')
countryTypeEnum.UM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UM', tag=u'UM')
countryTypeEnum.UY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UY', tag=u'UY')
countryTypeEnum.UZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UZ', tag=u'UZ')
countryTypeEnum.VU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VU', tag=u'VU')
countryTypeEnum.VA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VA', tag=u'VA')
countryTypeEnum.VE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VE', tag=u'VE')
countryTypeEnum.VN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VN', tag=u'VN')
countryTypeEnum.VG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VG', tag=u'VG')
countryTypeEnum.VI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VI', tag=u'VI')
countryTypeEnum.WF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'WF', tag=u'WF')
countryTypeEnum.EH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'EH', tag=u'EH')
countryTypeEnum.YE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'YE', tag=u'YE')
countryTypeEnum.ZM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ZM', tag=u'ZM')
countryTypeEnum.ZW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ZW', tag=u'ZW')
countryTypeEnum.RS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'RS', tag=u'RS')
countryTypeEnum.ME = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ME', tag=u'ME')
countryTypeEnum.SS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SS', tag=u'SS')
countryTypeEnum._InitializeFacetMap(countryTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'countryTypeEnum', countryTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}customerReferenceType
class customerReferenceType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customerReferenceType')
    _Documentation = None
customerReferenceType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
customerReferenceType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
customerReferenceType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(17L))
customerReferenceType._InitializeFacetMap(customerReferenceType._CF_whiteSpace,
   customerReferenceType._CF_minLength,
   customerReferenceType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'customerReferenceType', customerReferenceType)

# Atomic simple type: {http://www.litle.com/schema}taxTypeIdentifierEnum
class taxTypeIdentifierEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'taxTypeIdentifierEnum')
    _Documentation = None
taxTypeIdentifierEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=taxTypeIdentifierEnum, enum_prefix=None)
taxTypeIdentifierEnum.n00 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'00', tag=u'n00')
taxTypeIdentifierEnum.n01 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'01', tag=u'n01')
taxTypeIdentifierEnum.n02 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'02', tag=u'n02')
taxTypeIdentifierEnum.n03 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'03', tag=u'n03')
taxTypeIdentifierEnum.n04 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'04', tag=u'n04')
taxTypeIdentifierEnum.n05 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'05', tag=u'n05')
taxTypeIdentifierEnum.n06 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'06', tag=u'n06')
taxTypeIdentifierEnum.n10 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'10', tag=u'n10')
taxTypeIdentifierEnum.n11 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'11', tag=u'n11')
taxTypeIdentifierEnum.n12 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'12', tag=u'n12')
taxTypeIdentifierEnum.n13 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'13', tag=u'n13')
taxTypeIdentifierEnum.n14 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'14', tag=u'n14')
taxTypeIdentifierEnum.n20 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'20', tag=u'n20')
taxTypeIdentifierEnum.n21 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'21', tag=u'n21')
taxTypeIdentifierEnum.n22 = taxTypeIdentifierEnum._CF_enumeration.addEnumeration(unicode_value=u'22', tag=u'n22')
taxTypeIdentifierEnum._InitializeFacetMap(taxTypeIdentifierEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'taxTypeIdentifierEnum', taxTypeIdentifierEnum)

# Atomic simple type: {http://www.litle.com/schema}cardAcceptorTaxIdType
class cardAcceptorTaxIdType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cardAcceptorTaxIdType')
    _Documentation = None
cardAcceptorTaxIdType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
cardAcceptorTaxIdType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
cardAcceptorTaxIdType._InitializeFacetMap(cardAcceptorTaxIdType._CF_minLength,
   cardAcceptorTaxIdType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'cardAcceptorTaxIdType', cardAcceptorTaxIdType)

# Atomic simple type: {http://www.litle.com/schema}authenticationValueType
class authenticationValueType (pyxb.binding.datatypes.base64Binary):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'authenticationValueType')
    _Documentation = None
authenticationValueType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32L))
authenticationValueType._InitializeFacetMap(authenticationValueType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'authenticationValueType', authenticationValueType)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_6._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(4L))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_totalDigits)

# Atomic simple type: {http://www.litle.com/schema}quantityType
class quantityType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'quantityType')
    _Documentation = None
quantityType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=quantityType, value=pyxb.binding.datatypes.decimal(0.0))
quantityType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
quantityType._InitializeFacetMap(quantityType._CF_minInclusive,
   quantityType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', u'quantityType', quantityType)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_7._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5L))
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_totalDigits)

# Atomic simple type: {http://www.litle.com/schema}currencyCodeEnum
class currencyCodeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'currencyCodeEnum')
    _Documentation = None
currencyCodeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=currencyCodeEnum, enum_prefix=None)
currencyCodeEnum.AUD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'AUD', tag=u'AUD')
currencyCodeEnum.CAD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'CAD', tag=u'CAD')
currencyCodeEnum.CHF = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'CHF', tag=u'CHF')
currencyCodeEnum.DKK = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'DKK', tag=u'DKK')
currencyCodeEnum.EUR = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'EUR', tag=u'EUR')
currencyCodeEnum.GBP = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'GBP', tag=u'GBP')
currencyCodeEnum.HKD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'HKD', tag=u'HKD')
currencyCodeEnum.JPY = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'JPY', tag=u'JPY')
currencyCodeEnum.NOK = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'NOK', tag=u'NOK')
currencyCodeEnum.NZD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'NZD', tag=u'NZD')
currencyCodeEnum.SEK = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'SEK', tag=u'SEK')
currencyCodeEnum.SGD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'SGD', tag=u'SGD')
currencyCodeEnum.USD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'USD', tag=u'USD')
currencyCodeEnum._InitializeFacetMap(currencyCodeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'currencyCodeEnum', currencyCodeEnum)

# Atomic simple type: {http://www.litle.com/schema}authorizationSourcePlatform
class authorizationSourcePlatform (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'authorizationSourcePlatform')
    _Documentation = None
authorizationSourcePlatform._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
authorizationSourcePlatform._InitializeFacetMap(authorizationSourcePlatform._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'authorizationSourcePlatform', authorizationSourcePlatform)

# Atomic simple type: {http://www.litle.com/schema}expDateType
class expDateType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'expDateType')
    _Documentation = None
expDateType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
expDateType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
expDateType._InitializeFacetMap(expDateType._CF_minLength,
   expDateType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'expDateType', expDateType)

# Atomic simple type: {http://www.litle.com/schema}merchantCategoryCodeType
class merchantCategoryCodeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'merchantCategoryCodeType')
    _Documentation = None
merchantCategoryCodeType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
merchantCategoryCodeType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
merchantCategoryCodeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
merchantCategoryCodeType._InitializeFacetMap(merchantCategoryCodeType._CF_whiteSpace,
   merchantCategoryCodeType._CF_minLength,
   merchantCategoryCodeType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'merchantCategoryCodeType', merchantCategoryCodeType)

# Atomic simple type: {http://www.litle.com/schema}sellerIdType
class sellerIdType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sellerIdType')
    _Documentation = None
sellerIdType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
sellerIdType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
sellerIdType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16L))
sellerIdType._InitializeFacetMap(sellerIdType._CF_whiteSpace,
   sellerIdType._CF_minLength,
   sellerIdType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'sellerIdType', sellerIdType)

# Atomic simple type: {http://www.litle.com/schema}affiliateType
class affiliateType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'affiliateType')
    _Documentation = None
affiliateType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
affiliateType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
affiliateType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
affiliateType._InitializeFacetMap(affiliateType._CF_whiteSpace,
   affiliateType._CF_minLength,
   affiliateType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'affiliateType', affiliateType)

# Atomic simple type: {http://www.litle.com/schema}emailType
class emailType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'emailType')
    _Documentation = None
emailType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
emailType._InitializeFacetMap(emailType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'emailType', emailType)

# Atomic simple type: [anonymous]
class STD_ANON_8 (emailType):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_8._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_maxLength)

# Atomic simple type: {http://www.litle.com/schema}merchantGroupingIdType
class merchantGroupingIdType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'merchantGroupingIdType')
    _Documentation = None
merchantGroupingIdType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
merchantGroupingIdType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
merchantGroupingIdType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
merchantGroupingIdType._InitializeFacetMap(merchantGroupingIdType._CF_whiteSpace,
   merchantGroupingIdType._CF_minLength,
   merchantGroupingIdType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'merchantGroupingIdType', merchantGroupingIdType)

# Atomic simple type: {http://www.litle.com/schema}middleInitialType
class middleInitialType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'middleInitialType')
    _Documentation = None
middleInitialType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
middleInitialType._InitializeFacetMap(middleInitialType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'middleInitialType', middleInitialType)

# Atomic simple type: {http://www.litle.com/schema}govtTaxTypeEnum
class govtTaxTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'govtTaxTypeEnum')
    _Documentation = None
govtTaxTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=govtTaxTypeEnum, enum_prefix=None)
govtTaxTypeEnum.payment = govtTaxTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'payment', tag=u'payment')
govtTaxTypeEnum.fee = govtTaxTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'fee', tag=u'fee')
govtTaxTypeEnum._InitializeFacetMap(govtTaxTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'govtTaxTypeEnum', govtTaxTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}driversLicenseType
class driversLicenseType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'driversLicenseType')
    _Documentation = None
driversLicenseType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30L))
driversLicenseType._InitializeFacetMap(driversLicenseType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'driversLicenseType', driversLicenseType)

# Atomic simple type: {http://www.litle.com/schema}lastNameType
class lastNameType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lastNameType')
    _Documentation = None
lastNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
lastNameType._InitializeFacetMap(lastNameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'lastNameType', lastNameType)

# Atomic simple type: {http://www.litle.com/schema}phoneType
class phoneType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phoneType')
    _Documentation = None
phoneType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
phoneType._InitializeFacetMap(phoneType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'phoneType', phoneType)

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_9._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(2L))
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_totalDigits)

# Atomic simple type: {http://www.litle.com/schema}reloadablePrepaidTypeEnum
class reloadablePrepaidTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reloadablePrepaidTypeEnum')
    _Documentation = None
reloadablePrepaidTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=reloadablePrepaidTypeEnum, enum_prefix=None)
reloadablePrepaidTypeEnum.UNKNOWN = reloadablePrepaidTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWN', tag=u'UNKNOWN')
reloadablePrepaidTypeEnum.YES = reloadablePrepaidTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'YES', tag=u'YES')
reloadablePrepaidTypeEnum.NO = reloadablePrepaidTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NO', tag=u'NO')
reloadablePrepaidTypeEnum._InitializeFacetMap(reloadablePrepaidTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'reloadablePrepaidTypeEnum', reloadablePrepaidTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}cityType
class cityType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cityType')
    _Documentation = None
cityType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35L))
cityType._InitializeFacetMap(cityType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'cityType', cityType)

# Atomic simple type: {http://www.litle.com/schema}IIASFlagType
class IIASFlagType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IIASFlagType')
    _Documentation = None
IIASFlagType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IIASFlagType, enum_prefix=None)
IIASFlagType.Y = IIASFlagType._CF_enumeration.addEnumeration(unicode_value=u'Y', tag=u'Y')
IIASFlagType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
IIASFlagType._InitializeFacetMap(IIASFlagType._CF_enumeration,
   IIASFlagType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'IIASFlagType', IIASFlagType)

# Atomic simple type: {http://www.litle.com/schema}stateCodeType
class stateCodeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'stateCodeType')
    _Documentation = None
stateCodeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
stateCodeType._InitializeFacetMap(stateCodeType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'stateCodeType', stateCodeType)

# Atomic simple type: {http://www.litle.com/schema}taxRateType
class taxRateType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'taxRateType')
    _Documentation = None
taxRateType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5L))
taxRateType._InitializeFacetMap(taxRateType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', u'taxRateType', taxRateType)

# Atomic simple type: {http://www.litle.com/schema}fundingSourceTypeEnum
class fundingSourceTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fundingSourceTypeEnum')
    _Documentation = None
fundingSourceTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fundingSourceTypeEnum, enum_prefix=None)
fundingSourceTypeEnum.UNKNOWN = fundingSourceTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWN', tag=u'UNKNOWN')
fundingSourceTypeEnum.PREPAID = fundingSourceTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PREPAID', tag=u'PREPAID')
fundingSourceTypeEnum.FSA = fundingSourceTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FSA', tag=u'FSA')
fundingSourceTypeEnum.CREDIT = fundingSourceTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CREDIT', tag=u'CREDIT')
fundingSourceTypeEnum.DEBIT = fundingSourceTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DEBIT', tag=u'DEBIT')
fundingSourceTypeEnum._InitializeFacetMap(fundingSourceTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'fundingSourceTypeEnum', fundingSourceTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}itemSequenceNumberType
class itemSequenceNumberType (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'itemSequenceNumberType')
    _Documentation = None
itemSequenceNumberType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=itemSequenceNumberType, value=pyxb.binding.datatypes.integer(99L))
itemSequenceNumberType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=itemSequenceNumberType, value=pyxb.binding.datatypes.integer(1L))
itemSequenceNumberType._InitializeFacetMap(itemSequenceNumberType._CF_maxInclusive,
   itemSequenceNumberType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'itemSequenceNumberType', itemSequenceNumberType)

# Atomic simple type: {http://www.litle.com/schema}stateType
class stateType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'stateType')
    _Documentation = None
stateType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30L))
stateType._InitializeFacetMap(stateType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'stateType', stateType)

# Atomic simple type: {http://www.litle.com/schema}campaignType
class campaignType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'campaignType')
    _Documentation = None
campaignType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
campaignType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
campaignType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
campaignType._InitializeFacetMap(campaignType._CF_whiteSpace,
   campaignType._CF_minLength,
   campaignType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'campaignType', campaignType)

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_10._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(8L))
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_totalDigits)

# Atomic simple type: {http://www.litle.com/schema}virtualAuthenticationKeyPresenceIndicator
class virtualAuthenticationKeyPresenceIndicator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualAuthenticationKeyPresenceIndicator')
    _Documentation = None
virtualAuthenticationKeyPresenceIndicator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
virtualAuthenticationKeyPresenceIndicator._InitializeFacetMap(virtualAuthenticationKeyPresenceIndicator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'virtualAuthenticationKeyPresenceIndicator', virtualAuthenticationKeyPresenceIndicator)

# Atomic simple type: {http://www.litle.com/schema}itemDescriptionType
class itemDescriptionType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'itemDescriptionType')
    _Documentation = None
itemDescriptionType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
itemDescriptionType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(26L))
itemDescriptionType._InitializeFacetMap(itemDescriptionType._CF_minLength,
   itemDescriptionType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'itemDescriptionType', itemDescriptionType)

# Atomic simple type: {http://www.litle.com/schema}loanToValueEstimator
class loanToValueEstimator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loanToValueEstimator')
    _Documentation = None
loanToValueEstimator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
loanToValueEstimator._InitializeFacetMap(loanToValueEstimator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'loanToValueEstimator', loanToValueEstimator)

# Atomic simple type: {http://www.litle.com/schema}ksnType
class ksnType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ksnType')
    _Documentation = None
ksnType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
ksnType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1028L))
ksnType._InitializeFacetMap(ksnType._CF_minLength,
   ksnType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'ksnType', ksnType)

# Atomic simple type: {http://www.litle.com/schema}formatIdType
class formatIdType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'formatIdType')
    _Documentation = None
formatIdType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
formatIdType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1028L))
formatIdType._InitializeFacetMap(formatIdType._CF_minLength,
   formatIdType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'formatIdType', formatIdType)

# Atomic simple type: {http://www.litle.com/schema}encryptedTrackType
class encryptedTrackType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'encryptedTrackType')
    _Documentation = None
encryptedTrackType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
encryptedTrackType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1028L))
encryptedTrackType._InitializeFacetMap(encryptedTrackType._CF_minLength,
   encryptedTrackType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'encryptedTrackType', encryptedTrackType)

# Atomic simple type: {http://www.litle.com/schema}trackStatusType
class trackStatusType (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'trackStatusType')
    _Documentation = None
trackStatusType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=trackStatusType, value=pyxb.binding.datatypes.int(1028))
trackStatusType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=trackStatusType, value=pyxb.binding.datatypes.int(0))
trackStatusType._InitializeFacetMap(trackStatusType._CF_maxInclusive,
   trackStatusType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'trackStatusType', trackStatusType)

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_11._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(2L))
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_totalDigits)

# Atomic simple type: {http://www.litle.com/schema}dateOfBirthType
class dateOfBirthType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dateOfBirthType')
    _Documentation = None
dateOfBirthType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
dateOfBirthType._InitializeFacetMap(dateOfBirthType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'dateOfBirthType', dateOfBirthType)

# Atomic simple type: {http://www.litle.com/schema}authenticationResultType
class authenticationResultType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'authenticationResultType')
    _Documentation = None
authenticationResultType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
authenticationResultType._InitializeFacetMap(authenticationResultType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'authenticationResultType', authenticationResultType)

# Atomic simple type: {http://www.litle.com/schema}intervalTypeEnum
class intervalTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'intervalTypeEnum')
    _Documentation = None
intervalTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=intervalTypeEnum, enum_prefix=None)
intervalTypeEnum.ANNUAL = intervalTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ANNUAL', tag=u'ANNUAL')
intervalTypeEnum.SEMIANNUAL = intervalTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SEMIANNUAL', tag=u'SEMIANNUAL')
intervalTypeEnum.QUARTERLY = intervalTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'QUARTERLY', tag=u'QUARTERLY')
intervalTypeEnum.MONTHLY = intervalTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MONTHLY', tag=u'MONTHLY')
intervalTypeEnum.WEEKLY = intervalTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'WEEKLY', tag=u'WEEKLY')
intervalTypeEnum._InitializeFacetMap(intervalTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'intervalTypeEnum', intervalTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}firstNameType
class firstNameType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'firstNameType')
    _Documentation = None
firstNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
firstNameType._InitializeFacetMap(firstNameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'firstNameType', firstNameType)

# Atomic simple type: {http://www.litle.com/schema}invoiceReferenceNumberType
class invoiceReferenceNumberType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'invoiceReferenceNumberType')
    _Documentation = None
invoiceReferenceNumberType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
invoiceReferenceNumberType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15L))
invoiceReferenceNumberType._InitializeFacetMap(invoiceReferenceNumberType._CF_minLength,
   invoiceReferenceNumberType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'invoiceReferenceNumberType', invoiceReferenceNumberType)

# Atomic simple type: {http://www.litle.com/schema}string512Type
class string512Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'string512Type')
    _Documentation = None
string512Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(512L))
string512Type._InitializeFacetMap(string512Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'string512Type', string512Type)

# Atomic simple type: {http://www.litle.com/schema}posEntryModeTypeEnum
class posEntryModeTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'posEntryModeTypeEnum')
    _Documentation = None
posEntryModeTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=posEntryModeTypeEnum, enum_prefix=None)
posEntryModeTypeEnum.notused = posEntryModeTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'notused', tag=u'notused')
posEntryModeTypeEnum.keyed = posEntryModeTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'keyed', tag=u'keyed')
posEntryModeTypeEnum.track1 = posEntryModeTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'track1', tag=u'track1')
posEntryModeTypeEnum.track2 = posEntryModeTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'track2', tag=u'track2')
posEntryModeTypeEnum.completeread = posEntryModeTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'completeread', tag=u'completeread')
posEntryModeTypeEnum._InitializeFacetMap(posEntryModeTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'posEntryModeTypeEnum', posEntryModeTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}posCardholderIdTypeEnum
class posCardholderIdTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'posCardholderIdTypeEnum')
    _Documentation = None
posCardholderIdTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=posCardholderIdTypeEnum, enum_prefix=None)
posCardholderIdTypeEnum.signature = posCardholderIdTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'signature', tag=u'signature')
posCardholderIdTypeEnum.pin = posCardholderIdTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'pin', tag=u'pin')
posCardholderIdTypeEnum.nopin = posCardholderIdTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'nopin', tag=u'nopin')
posCardholderIdTypeEnum.directmarket = posCardholderIdTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'directmarket', tag=u'directmarket')
posCardholderIdTypeEnum._InitializeFacetMap(posCardholderIdTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'posCardholderIdTypeEnum', posCardholderIdTypeEnum)

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_12._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
STD_ANON_12._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_12._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(127L))
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_whiteSpace,
   STD_ANON_12._CF_minLength,
   STD_ANON_12._CF_maxLength)

# Atomic simple type: {http://www.litle.com/schema}posCapabilityTypeEnum
class posCapabilityTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'posCapabilityTypeEnum')
    _Documentation = None
posCapabilityTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=posCapabilityTypeEnum, enum_prefix=None)
posCapabilityTypeEnum.notused = posCapabilityTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'notused', tag=u'notused')
posCapabilityTypeEnum.magstripe = posCapabilityTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'magstripe', tag=u'magstripe')
posCapabilityTypeEnum.keyedonly = posCapabilityTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'keyedonly', tag=u'keyedonly')
posCapabilityTypeEnum._InitializeFacetMap(posCapabilityTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'posCapabilityTypeEnum', posCapabilityTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}ipAddress
class ipAddress (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ipAddress')
    _Documentation = None
ipAddress._CF_pattern = pyxb.binding.facets.CF_pattern()
ipAddress._CF_pattern.addPattern(pattern=u'(\\d{1,3}.){3}\\d{1,3}')
ipAddress._InitializeFacetMap(ipAddress._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ipAddress', ipAddress)

# Atomic simple type: {http://www.litle.com/schema}productCodeType
class productCodeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'productCodeType')
    _Documentation = None
productCodeType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
productCodeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12L))
productCodeType._InitializeFacetMap(productCodeType._CF_minLength,
   productCodeType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'productCodeType', productCodeType)

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_13._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
STD_ANON_13._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_13._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(17L))
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_whiteSpace,
   STD_ANON_13._CF_minLength,
   STD_ANON_13._CF_maxLength)

# Complex type {http://www.litle.com/schema}voidRecyclingResponseType with content type ELEMENT_ONLY
class voidRecyclingResponseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'voidRecyclingResponseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}creditLitleTxnId uses Python identifier creditLitleTxnId
    __creditLitleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'creditLitleTxnId'), 'creditLitleTxnId', '__httpwww_litle_comschema_voidRecyclingResponseType_httpwww_litle_comschemacreditLitleTxnId', False)

    
    creditLitleTxnId = property(__creditLitleTxnId.value, __creditLitleTxnId.set, None, None)


    _ElementMap = {
        __creditLitleTxnId.name() : __creditLitleTxnId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'voidRecyclingResponseType', voidRecyclingResponseType)


# Complex type {http://www.litle.com/schema}transactionType with content type EMPTY
class transactionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'transactionType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_litle_comschema_transactionType_id', string25Type)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute customerId uses Python identifier customerId
    __customerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'customerId'), 'customerId', '__httpwww_litle_comschema_transactionType_customerId', customerIdType)
    
    customerId = property(__customerId.value, __customerId.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id,
        __customerId.name() : __customerId
    }
Namespace.addCategoryObject('typeBinding', u'transactionType', transactionType)


# Complex type {http://www.litle.com/schema}transactionTypeWithReportGroup with content type EMPTY
class transactionTypeWithReportGroup (transactionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'transactionTypeWithReportGroup')
    # Base type is transactionType
    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup uses Python identifier reportGroup
    __reportGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'reportGroup'), 'reportGroup', '__httpwww_litle_comschema_transactionTypeWithReportGroup_reportGroup', reportGroupType, required=True)
    
    reportGroup = property(__reportGroup.value, __reportGroup.set, None, None)

    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionType._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = transactionType._AttributeMap.copy()
    _AttributeMap.update({
        __reportGroup.name() : __reportGroup
    })
Namespace.addCategoryObject('typeBinding', u'transactionTypeWithReportGroup', transactionTypeWithReportGroup)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}approvedTermsCode uses Python identifier approvedTermsCode
    __approvedTermsCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'approvedTermsCode'), 'approvedTermsCode', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemaapprovedTermsCode', False)

    
    approvedTermsCode = property(__approvedTermsCode.value, __approvedTermsCode.set, None, None)

    
    # Element {http://www.litle.com/schema}riskEstimator uses Python identifier riskEstimator
    __riskEstimator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'riskEstimator'), 'riskEstimator', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemariskEstimator', False)

    
    riskEstimator = property(__riskEstimator.value, __riskEstimator.set, None, None)

    
    # Element {http://www.litle.com/schema}creditLine uses Python identifier creditLine
    __creditLine = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'creditLine'), 'creditLine', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemacreditLine', False)

    
    creditLine = property(__creditLine.value, __creditLine.set, None, None)

    
    # Element {http://www.litle.com/schema}riskQueueAssignment uses Python identifier riskQueueAssignment
    __riskQueueAssignment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'riskQueueAssignment'), 'riskQueueAssignment', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemariskQueueAssignment', False)

    
    riskQueueAssignment = property(__riskQueueAssignment.value, __riskQueueAssignment.set, None, None)

    
    # Element {http://www.litle.com/schema}bmlMerchantId uses Python identifier bmlMerchantId
    __bmlMerchantId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bmlMerchantId'), 'bmlMerchantId', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemabmlMerchantId', False)

    
    bmlMerchantId = property(__bmlMerchantId.value, __bmlMerchantId.set, None, None)

    
    # Element {http://www.litle.com/schema}addressIndicator uses Python identifier addressIndicator
    __addressIndicator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addressIndicator'), 'addressIndicator', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemaaddressIndicator', False)

    
    addressIndicator = property(__addressIndicator.value, __addressIndicator.set, None, None)

    
    # Element {http://www.litle.com/schema}promotionalOfferCode uses Python identifier promotionalOfferCode
    __promotionalOfferCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'promotionalOfferCode'), 'promotionalOfferCode', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemapromotionalOfferCode', False)

    
    promotionalOfferCode = property(__promotionalOfferCode.value, __promotionalOfferCode.set, None, None)

    
    # Element {http://www.litle.com/schema}loanToValueEstimator uses Python identifier loanToValueEstimator
    __loanToValueEstimator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'loanToValueEstimator'), 'loanToValueEstimator', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemaloanToValueEstimator', False)

    
    loanToValueEstimator = property(__loanToValueEstimator.value, __loanToValueEstimator.set, None, None)


    _ElementMap = {
        __approvedTermsCode.name() : __approvedTermsCode,
        __riskEstimator.name() : __riskEstimator,
        __creditLine.name() : __creditLine,
        __riskQueueAssignment.name() : __riskQueueAssignment,
        __bmlMerchantId.name() : __bmlMerchantId,
        __addressIndicator.name() : __addressIndicator,
        __promotionalOfferCode.name() : __promotionalOfferCode,
        __loanToValueEstimator.name() : __loanToValueEstimator
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}catLevel uses Python identifier catLevel
    __catLevel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'catLevel'), 'catLevel', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemacatLevel', False)

    
    catLevel = property(__catLevel.value, __catLevel.set, None, None)

    
    # Element {http://www.litle.com/schema}cardholderId uses Python identifier cardholderId
    __cardholderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardholderId'), 'cardholderId', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemacardholderId', False)

    
    cardholderId = property(__cardholderId.value, __cardholderId.set, None, None)

    
    # Element {http://www.litle.com/schema}terminalId uses Python identifier terminalId
    __terminalId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'terminalId'), 'terminalId', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschematerminalId', False)

    
    terminalId = property(__terminalId.value, __terminalId.set, None, None)

    
    # Element {http://www.litle.com/schema}capability uses Python identifier capability
    __capability = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'capability'), 'capability', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemacapability', False)

    
    capability = property(__capability.value, __capability.set, None, None)

    
    # Element {http://www.litle.com/schema}entryMode uses Python identifier entryMode
    __entryMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'entryMode'), 'entryMode', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemaentryMode', False)

    
    entryMode = property(__entryMode.value, __entryMode.set, None, None)


    _ElementMap = {
        __catLevel.name() : __catLevel,
        __cardholderId.name() : __cardholderId,
        __terminalId.name() : __terminalId,
        __capability.name() : __capability,
        __entryMode.name() : __entryMode
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}RFRResponse uses Python identifier RFRResponse
    __RFRResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RFRResponse'), 'RFRResponse', '__httpwww_litle_comschema_CTD_ANON_3_httpwww_litle_comschemaRFRResponse', False)

    
    RFRResponse = property(__RFRResponse.value, __RFRResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}batchResponse uses Python identifier batchResponse
    __batchResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'batchResponse'), 'batchResponse', '__httpwww_litle_comschema_CTD_ANON_3_httpwww_litle_comschemabatchResponse', True)

    
    batchResponse = property(__batchResponse.value, __batchResponse.set, None, None)

    
    # Attribute response uses Python identifier response
    __response = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_3_response', responseType, required=True)
    
    response = property(__response.value, __response.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_litle_comschema_CTD_ANON_3_version', versionType, required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_litle_comschema_CTD_ANON_3_id', string25Type)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute litleSessionId uses Python identifier litleSessionId
    __litleSessionId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'litleSessionId'), 'litleSessionId', '__httpwww_litle_comschema_CTD_ANON_3_litleSessionId', litleIdType, required=True)
    
    litleSessionId = property(__litleSessionId.value, __litleSessionId.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_3_message', messageType, required=True)
    
    message = property(__message.value, __message.set, None, None)


    _ElementMap = {
        __RFRResponse.name() : __RFRResponse,
        __batchResponse.name() : __batchResponse
    }
    _AttributeMap = {
        __response.name() : __response,
        __version.name() : __version,
        __id.name() : __id,
        __litleSessionId.name() : __litleSessionId,
        __message.name() : __message
    }



# Complex type {http://www.litle.com/schema}cardType with content type ELEMENT_ONLY
class cardType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cardType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}type uses Python identifier type
    __type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_litle_comschema_cardType_httpwww_litle_comschematype', False)

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://www.litle.com/schema}cardValidationNum uses Python identifier cardValidationNum
    __cardValidationNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), 'cardValidationNum', '__httpwww_litle_comschema_cardType_httpwww_litle_comschemacardValidationNum', False)

    
    cardValidationNum = property(__cardValidationNum.value, __cardValidationNum.set, None, None)

    
    # Element {http://www.litle.com/schema}track uses Python identifier track
    __track = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'track'), 'track', '__httpwww_litle_comschema_cardType_httpwww_litle_comschematrack', False)

    
    track = property(__track.value, __track.set, None, None)

    
    # Element {http://www.litle.com/schema}expDate uses Python identifier expDate
    __expDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'expDate'), 'expDate', '__httpwww_litle_comschema_cardType_httpwww_litle_comschemaexpDate', False)

    
    expDate = property(__expDate.value, __expDate.set, None, None)

    
    # Element {http://www.litle.com/schema}number uses Python identifier number
    __number = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'number'), 'number', '__httpwww_litle_comschema_cardType_httpwww_litle_comschemanumber', False)

    
    number = property(__number.value, __number.set, None, None)


    _ElementMap = {
        __type.name() : __type,
        __cardValidationNum.name() : __cardValidationNum,
        __track.name() : __track,
        __expDate.name() : __expDate,
        __number.name() : __number
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cardType', cardType)


# Complex type {http://www.litle.com/schema}recurringTransactionResponseType with content type ELEMENT_ONLY
class recurringTransactionResponseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recurringTransactionResponseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_recurringTransactionResponseType_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_recurringTransactionResponseType_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_recurringTransactionResponseType_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_recurringTransactionResponseType_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)


    _ElementMap = {
        __responseTime.name() : __responseTime,
        __message.name() : __message,
        __litleTxnId.name() : __litleTxnId,
        __response.name() : __response
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'recurringTransactionResponseType', recurringTransactionResponseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}originalTokenInfo uses Python identifier originalTokenInfo
    __originalTokenInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'originalTokenInfo'), 'originalTokenInfo', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemaoriginalTokenInfo', False)

    
    originalTokenInfo = property(__originalTokenInfo.value, __originalTokenInfo.set, None, None)

    
    # Element {http://www.litle.com/schema}newCardInfo uses Python identifier newCardInfo
    __newCardInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'newCardInfo'), 'newCardInfo', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemanewCardInfo', False)

    
    newCardInfo = property(__newCardInfo.value, __newCardInfo.set, None, None)

    
    # Element {http://www.litle.com/schema}newTokenInfo uses Python identifier newTokenInfo
    __newTokenInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'newTokenInfo'), 'newTokenInfo', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemanewTokenInfo', False)

    
    newTokenInfo = property(__newTokenInfo.value, __newTokenInfo.set, None, None)

    
    # Element {http://www.litle.com/schema}extendedCardResponse uses Python identifier extendedCardResponse
    __extendedCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extendedCardResponse'), 'extendedCardResponse', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemaextendedCardResponse', False)

    
    extendedCardResponse = property(__extendedCardResponse.value, __extendedCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}newAccountInfo uses Python identifier newAccountInfo
    __newAccountInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'newAccountInfo'), 'newAccountInfo', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemanewAccountInfo', False)

    
    newAccountInfo = property(__newAccountInfo.value, __newAccountInfo.set, None, None)

    
    # Element {http://www.litle.com/schema}originalAccountInfo uses Python identifier originalAccountInfo
    __originalAccountInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'originalAccountInfo'), 'originalAccountInfo', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemaoriginalAccountInfo', False)

    
    originalAccountInfo = property(__originalAccountInfo.value, __originalAccountInfo.set, None, None)

    
    # Element {http://www.litle.com/schema}originalCardInfo uses Python identifier originalCardInfo
    __originalCardInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'originalCardInfo'), 'originalCardInfo', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemaoriginalCardInfo', False)

    
    originalCardInfo = property(__originalCardInfo.value, __originalCardInfo.set, None, None)

    
    # Element {http://www.litle.com/schema}originalCardTokenInfo uses Python identifier originalCardTokenInfo
    __originalCardTokenInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'originalCardTokenInfo'), 'originalCardTokenInfo', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemaoriginalCardTokenInfo', False)

    
    originalCardTokenInfo = property(__originalCardTokenInfo.value, __originalCardTokenInfo.set, None, None)

    
    # Element {http://www.litle.com/schema}newCardTokenInfo uses Python identifier newCardTokenInfo
    __newCardTokenInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'newCardTokenInfo'), 'newCardTokenInfo', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemanewCardTokenInfo', False)

    
    newCardTokenInfo = property(__newCardTokenInfo.value, __newCardTokenInfo.set, None, None)


    _ElementMap = {
        __originalTokenInfo.name() : __originalTokenInfo,
        __newCardInfo.name() : __newCardInfo,
        __newTokenInfo.name() : __newTokenInfo,
        __extendedCardResponse.name() : __extendedCardResponse,
        __newAccountInfo.name() : __newAccountInfo,
        __originalAccountInfo.name() : __originalAccountInfo,
        __originalCardInfo.name() : __originalCardInfo,
        __originalCardTokenInfo.name() : __originalCardTokenInfo,
        __newCardTokenInfo.name() : __newCardTokenInfo
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_5_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}recurringTransactionType with content type EMPTY
class recurringTransactionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recurringTransactionType')
    # Base type is pyxb.binding.datatypes.anyType

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'recurringTransactionType', recurringTransactionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (recurringTransactionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is recurringTransactionType
    
    # Element {http://www.litle.com/schema}active uses Python identifier active
    __active = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpwww_litle_comschema_CTD_ANON_6_httpwww_litle_comschemaactive', False)

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://www.litle.com/schema}planCode uses Python identifier planCode
    __planCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'planCode'), 'planCode', '__httpwww_litle_comschema_CTD_ANON_6_httpwww_litle_comschemaplanCode', False)

    
    planCode = property(__planCode.value, __planCode.set, None, None)


    _ElementMap = recurringTransactionType._ElementMap.copy()
    _ElementMap.update({
        __active.name() : __active,
        __planCode.name() : __planCode
    })
    _AttributeMap = recurringTransactionType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}cardTokenType with content type ELEMENT_ONLY
class cardTokenType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cardTokenType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}expDate uses Python identifier expDate
    __expDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'expDate'), 'expDate', '__httpwww_litle_comschema_cardTokenType_httpwww_litle_comschemaexpDate', False)

    
    expDate = property(__expDate.value, __expDate.set, None, None)

    
    # Element {http://www.litle.com/schema}cardValidationNum uses Python identifier cardValidationNum
    __cardValidationNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), 'cardValidationNum', '__httpwww_litle_comschema_cardTokenType_httpwww_litle_comschemacardValidationNum', False)

    
    cardValidationNum = property(__cardValidationNum.value, __cardValidationNum.set, None, None)

    
    # Element {http://www.litle.com/schema}litleToken uses Python identifier litleToken
    __litleToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), 'litleToken', '__httpwww_litle_comschema_cardTokenType_httpwww_litle_comschemalitleToken', False)

    
    litleToken = property(__litleToken.value, __litleToken.set, None, None)

    
    # Element {http://www.litle.com/schema}type uses Python identifier type
    __type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_litle_comschema_cardTokenType_httpwww_litle_comschematype', False)

    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        __expDate.name() : __expDate,
        __cardValidationNum.name() : __cardValidationNum,
        __litleToken.name() : __litleToken,
        __type.name() : __type
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cardTokenType', cardTokenType)


# Complex type {http://www.litle.com/schema}cardTokenTypeAU with content type ELEMENT_ONLY
class cardTokenTypeAU (cardTokenType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cardTokenTypeAU')
    # Base type is cardTokenType
    
    # Element cardValidationNum ({http://www.litle.com/schema}cardValidationNum) inherited from {http://www.litle.com/schema}cardTokenType
    
    # Element expDate ({http://www.litle.com/schema}expDate) inherited from {http://www.litle.com/schema}cardTokenType
    
    # Element type ({http://www.litle.com/schema}type) inherited from {http://www.litle.com/schema}cardTokenType
    
    # Element litleToken ({http://www.litle.com/schema}litleToken) inherited from {http://www.litle.com/schema}cardTokenType
    
    # Element {http://www.litle.com/schema}bin uses Python identifier bin
    __bin = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bin'), 'bin', '__httpwww_litle_comschema_cardTokenTypeAU_httpwww_litle_comschemabin', False)

    
    bin = property(__bin.value, __bin.set, None, None)


    _ElementMap = cardTokenType._ElementMap.copy()
    _ElementMap.update({
        __bin.name() : __bin
    })
    _AttributeMap = cardTokenType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'cardTokenTypeAU', cardTokenTypeAU)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}beginningBalance uses Python identifier beginningBalance
    __beginningBalance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'beginningBalance'), 'beginningBalance', '__httpwww_litle_comschema_CTD_ANON_7_httpwww_litle_comschemabeginningBalance', False)

    
    beginningBalance = property(__beginningBalance.value, __beginningBalance.set, None, None)

    
    # Element {http://www.litle.com/schema}cashBackAmount uses Python identifier cashBackAmount
    __cashBackAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cashBackAmount'), 'cashBackAmount', '__httpwww_litle_comschema_CTD_ANON_7_httpwww_litle_comschemacashBackAmount', False)

    
    cashBackAmount = property(__cashBackAmount.value, __cashBackAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}availableBalance uses Python identifier availableBalance
    __availableBalance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'availableBalance'), 'availableBalance', '__httpwww_litle_comschema_CTD_ANON_7_httpwww_litle_comschemaavailableBalance', False)

    
    availableBalance = property(__availableBalance.value, __availableBalance.set, None, None)

    
    # Element {http://www.litle.com/schema}endingBalance uses Python identifier endingBalance
    __endingBalance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'endingBalance'), 'endingBalance', '__httpwww_litle_comschema_CTD_ANON_7_httpwww_litle_comschemaendingBalance', False)

    
    endingBalance = property(__endingBalance.value, __endingBalance.set, None, None)


    _ElementMap = {
        __beginningBalance.name() : __beginningBalance,
        __cashBackAmount.name() : __cashBackAmount,
        __availableBalance.name() : __availableBalance,
        __endingBalance.name() : __endingBalance
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_8_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (recurringTransactionResponseType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is recurringTransactionResponseType
    
    # Element {http://www.litle.com/schema}subscriptionId uses Python identifier subscriptionId
    __subscriptionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), 'subscriptionId', '__httpwww_litle_comschema_CTD_ANON_9_httpwww_litle_comschemasubscriptionId', False)

    
    subscriptionId = property(__subscriptionId.value, __subscriptionId.set, None, None)

    
    # Element message ({http://www.litle.com/schema}message) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element litleTxnId ({http://www.litle.com/schema}litleTxnId) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element response ({http://www.litle.com/schema}response) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element responseTime ({http://www.litle.com/schema}responseTime) inherited from {http://www.litle.com/schema}recurringTransactionResponseType

    _ElementMap = recurringTransactionResponseType._ElementMap.copy()
    _ElementMap.update({
        __subscriptionId.name() : __subscriptionId
    })
    _AttributeMap = recurringTransactionResponseType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}batchRequest uses Python identifier batchRequest
    __batchRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'batchRequest'), 'batchRequest', '__httpwww_litle_comschema_CTD_ANON_10_httpwww_litle_comschemabatchRequest', True)

    
    batchRequest = property(__batchRequest.value, __batchRequest.set, None, None)

    
    # Element {http://www.litle.com/schema}authentication uses Python identifier authentication
    __authentication = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authentication'), 'authentication', '__httpwww_litle_comschema_CTD_ANON_10_httpwww_litle_comschemaauthentication', False)

    
    authentication = property(__authentication.value, __authentication.set, None, None)

    
    # Element {http://www.litle.com/schema}RFRRequest uses Python identifier RFRRequest
    __RFRRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RFRRequest'), 'RFRRequest', '__httpwww_litle_comschema_CTD_ANON_10_httpwww_litle_comschemaRFRRequest', False)

    
    RFRRequest = property(__RFRRequest.value, __RFRRequest.set, None, None)

    
    # Attribute numBatchRequests uses Python identifier numBatchRequests
    __numBatchRequests = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numBatchRequests'), 'numBatchRequests', '__httpwww_litle_comschema_CTD_ANON_10_numBatchRequests', pyxb.binding.datatypes.integer, required=True)
    
    numBatchRequests = property(__numBatchRequests.value, __numBatchRequests.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_litle_comschema_CTD_ANON_10_version', versionType, required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_litle_comschema_CTD_ANON_10_id', string25Type)
    
    id = property(__id.value, __id.set, None, None)


    _ElementMap = {
        __batchRequest.name() : __batchRequest,
        __authentication.name() : __authentication,
        __RFRRequest.name() : __RFRRequest
    }
    _AttributeMap = {
        __numBatchRequests.name() : __numBatchRequests,
        __version.name() : __version,
        __id.name() : __id
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (recurringTransactionResponseType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is recurringTransactionResponseType
    
    # Element responseTime ({http://www.litle.com/schema}responseTime) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element {http://www.litle.com/schema}subscriptionId uses Python identifier subscriptionId
    __subscriptionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), 'subscriptionId', '__httpwww_litle_comschema_CTD_ANON_11_httpwww_litle_comschemasubscriptionId', False)

    
    subscriptionId = property(__subscriptionId.value, __subscriptionId.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponse uses Python identifier tokenResponse
    __tokenResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), 'tokenResponse', '__httpwww_litle_comschema_CTD_ANON_11_httpwww_litle_comschematokenResponse', False)

    
    tokenResponse = property(__tokenResponse.value, __tokenResponse.set, None, None)

    
    # Element response ({http://www.litle.com/schema}response) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element litleTxnId ({http://www.litle.com/schema}litleTxnId) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element message ({http://www.litle.com/schema}message) inherited from {http://www.litle.com/schema}recurringTransactionResponseType

    _ElementMap = recurringTransactionResponseType._ElementMap.copy()
    _ElementMap.update({
        __subscriptionId.name() : __subscriptionId,
        __tokenResponse.name() : __tokenResponse
    })
    _AttributeMap = recurringTransactionResponseType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_12_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_12_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_12_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __card.name() : __card,
        __orderId.name() : __orderId,
        __orderSource.name() : __orderSource
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}deleteAddOnType with content type ELEMENT_ONLY
class deleteAddOnType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'deleteAddOnType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}addOnCode uses Python identifier addOnCode
    __addOnCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addOnCode'), 'addOnCode', '__httpwww_litle_comschema_deleteAddOnType_httpwww_litle_comschemaaddOnCode', False)

    
    addOnCode = property(__addOnCode.value, __addOnCode.set, None, None)


    _ElementMap = {
        __addOnCode.name() : __addOnCode
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'deleteAddOnType', deleteAddOnType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}shippingAmount uses Python identifier shippingAmount
    __shippingAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'shippingAmount'), 'shippingAmount', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemashippingAmount', False)

    
    shippingAmount = property(__shippingAmount.value, __shippingAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}deliveryType uses Python identifier deliveryType
    __deliveryType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'deliveryType'), 'deliveryType', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemadeliveryType', False)

    
    deliveryType = property(__deliveryType.value, __deliveryType.set, None, None)

    
    # Element {http://www.litle.com/schema}orderDate uses Python identifier orderDate
    __orderDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderDate'), 'orderDate', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemaorderDate', False)

    
    orderDate = property(__orderDate.value, __orderDate.set, None, None)

    
    # Element {http://www.litle.com/schema}dutyAmount uses Python identifier dutyAmount
    __dutyAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dutyAmount'), 'dutyAmount', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemadutyAmount', False)

    
    dutyAmount = property(__dutyAmount.value, __dutyAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}destinationPostalCode uses Python identifier destinationPostalCode
    __destinationPostalCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'destinationPostalCode'), 'destinationPostalCode', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemadestinationPostalCode', False)

    
    destinationPostalCode = property(__destinationPostalCode.value, __destinationPostalCode.set, None, None)

    
    # Element {http://www.litle.com/schema}invoiceReferenceNumber uses Python identifier invoiceReferenceNumber
    __invoiceReferenceNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'invoiceReferenceNumber'), 'invoiceReferenceNumber', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemainvoiceReferenceNumber', False)

    
    invoiceReferenceNumber = property(__invoiceReferenceNumber.value, __invoiceReferenceNumber.set, None, None)

    
    # Element {http://www.litle.com/schema}lineItemData uses Python identifier lineItemData
    __lineItemData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lineItemData'), 'lineItemData', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemalineItemData', True)

    
    lineItemData = property(__lineItemData.value, __lineItemData.set, None, None)

    
    # Element {http://www.litle.com/schema}customerReference uses Python identifier customerReference
    __customerReference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerReference'), 'customerReference', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemacustomerReference', False)

    
    customerReference = property(__customerReference.value, __customerReference.set, None, None)

    
    # Element {http://www.litle.com/schema}salesTax uses Python identifier salesTax
    __salesTax = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'salesTax'), 'salesTax', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemasalesTax', False)

    
    salesTax = property(__salesTax.value, __salesTax.set, None, None)

    
    # Element {http://www.litle.com/schema}discountAmount uses Python identifier discountAmount
    __discountAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'discountAmount'), 'discountAmount', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemadiscountAmount', False)

    
    discountAmount = property(__discountAmount.value, __discountAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}taxExempt uses Python identifier taxExempt
    __taxExempt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxExempt'), 'taxExempt', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemataxExempt', False)

    
    taxExempt = property(__taxExempt.value, __taxExempt.set, None, None)

    
    # Element {http://www.litle.com/schema}shipFromPostalCode uses Python identifier shipFromPostalCode
    __shipFromPostalCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'shipFromPostalCode'), 'shipFromPostalCode', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemashipFromPostalCode', False)

    
    shipFromPostalCode = property(__shipFromPostalCode.value, __shipFromPostalCode.set, None, None)

    
    # Element {http://www.litle.com/schema}destinationCountryCode uses Python identifier destinationCountryCode
    __destinationCountryCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'destinationCountryCode'), 'destinationCountryCode', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemadestinationCountryCode', False)

    
    destinationCountryCode = property(__destinationCountryCode.value, __destinationCountryCode.set, None, None)

    
    # Element {http://www.litle.com/schema}detailTax uses Python identifier detailTax
    __detailTax = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'detailTax'), 'detailTax', '__httpwww_litle_comschema_CTD_ANON_13_httpwww_litle_comschemadetailTax', True)

    
    detailTax = property(__detailTax.value, __detailTax.set, None, None)


    _ElementMap = {
        __shippingAmount.name() : __shippingAmount,
        __deliveryType.name() : __deliveryType,
        __orderDate.name() : __orderDate,
        __dutyAmount.name() : __dutyAmount,
        __destinationPostalCode.name() : __destinationPostalCode,
        __invoiceReferenceNumber.name() : __invoiceReferenceNumber,
        __lineItemData.name() : __lineItemData,
        __customerReference.name() : __customerReference,
        __salesTax.name() : __salesTax,
        __discountAmount.name() : __discountAmount,
        __taxExempt.name() : __taxExempt,
        __shipFromPostalCode.name() : __shipFromPostalCode,
        __destinationCountryCode.name() : __destinationCountryCode,
        __detailTax.name() : __detailTax
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (recurringTransactionResponseType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is recurringTransactionResponseType
    
    # Element {http://www.litle.com/schema}planCode uses Python identifier planCode
    __planCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'planCode'), 'planCode', '__httpwww_litle_comschema_CTD_ANON_14_httpwww_litle_comschemaplanCode', False)

    
    planCode = property(__planCode.value, __planCode.set, None, None)

    
    # Element message ({http://www.litle.com/schema}message) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element litleTxnId ({http://www.litle.com/schema}litleTxnId) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element response ({http://www.litle.com/schema}response) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element responseTime ({http://www.litle.com/schema}responseTime) inherited from {http://www.litle.com/schema}recurringTransactionResponseType

    _ElementMap = recurringTransactionResponseType._ElementMap.copy()
    _ElementMap.update({
        __planCode.name() : __planCode
    })
    _AttributeMap = recurringTransactionResponseType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}createAddOnType with content type ELEMENT_ONLY
class createAddOnType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'createAddOnType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}endDate uses Python identifier endDate
    __endDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'endDate'), 'endDate', '__httpwww_litle_comschema_createAddOnType_httpwww_litle_comschemaendDate', False)

    
    endDate = property(__endDate.value, __endDate.set, None, None)

    
    # Element {http://www.litle.com/schema}startDate uses Python identifier startDate
    __startDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'startDate'), 'startDate', '__httpwww_litle_comschema_createAddOnType_httpwww_litle_comschemastartDate', False)

    
    startDate = property(__startDate.value, __startDate.set, None, None)

    
    # Element {http://www.litle.com/schema}addOnCode uses Python identifier addOnCode
    __addOnCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addOnCode'), 'addOnCode', '__httpwww_litle_comschema_createAddOnType_httpwww_litle_comschemaaddOnCode', False)

    
    addOnCode = property(__addOnCode.value, __addOnCode.set, None, None)

    
    # Element {http://www.litle.com/schema}name uses Python identifier name
    __name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_litle_comschema_createAddOnType_httpwww_litle_comschemaname', False)

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_createAddOnType_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)


    _ElementMap = {
        __endDate.name() : __endDate,
        __startDate.name() : __startDate,
        __addOnCode.name() : __addOnCode,
        __name.name() : __name,
        __amount.name() : __amount
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'createAddOnType', createAddOnType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}bypassVelocityCheck uses Python identifier bypassVelocityCheck
    __bypassVelocityCheck = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bypassVelocityCheck'), 'bypassVelocityCheck', '__httpwww_litle_comschema_CTD_ANON_15_httpwww_litle_comschemabypassVelocityCheck', False)

    
    bypassVelocityCheck = property(__bypassVelocityCheck.value, __bypassVelocityCheck.set, None, None)


    _ElementMap = {
        __bypassVelocityCheck.name() : __bypassVelocityCheck
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}city uses Python identifier city
    __city = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httpwww_litle_comschema_CTD_ANON_16_httpwww_litle_comschemacity', False)

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://www.litle.com/schema}url uses Python identifier url
    __url = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'url'), 'url', '__httpwww_litle_comschema_CTD_ANON_16_httpwww_litle_comschemaurl', False)

    
    url = property(__url.value, __url.set, None, None)

    
    # Element {http://www.litle.com/schema}descriptor uses Python identifier descriptor
    __descriptor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'descriptor'), 'descriptor', '__httpwww_litle_comschema_CTD_ANON_16_httpwww_litle_comschemadescriptor', False)

    
    descriptor = property(__descriptor.value, __descriptor.set, None, None)

    
    # Element {http://www.litle.com/schema}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'phone'), 'phone', '__httpwww_litle_comschema_CTD_ANON_16_httpwww_litle_comschemaphone', False)

    
    phone = property(__phone.value, __phone.set, None, None)


    _ElementMap = {
        __city.name() : __city,
        __url.name() : __url,
        __descriptor.name() : __descriptor,
        __phone.name() : __phone
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (recurringTransactionResponseType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is recurringTransactionResponseType
    
    # Element {http://www.litle.com/schema}planCode uses Python identifier planCode
    __planCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'planCode'), 'planCode', '__httpwww_litle_comschema_CTD_ANON_17_httpwww_litle_comschemaplanCode', False)

    
    planCode = property(__planCode.value, __planCode.set, None, None)

    
    # Element message ({http://www.litle.com/schema}message) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element litleTxnId ({http://www.litle.com/schema}litleTxnId) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element response ({http://www.litle.com/schema}response) inherited from {http://www.litle.com/schema}recurringTransactionResponseType
    
    # Element responseTime ({http://www.litle.com/schema}responseTime) inherited from {http://www.litle.com/schema}recurringTransactionResponseType

    _ElementMap = recurringTransactionResponseType._ElementMap.copy()
    _ElementMap.update({
        __planCode.name() : __planCode
    })
    _AttributeMap = recurringTransactionResponseType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_18_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_19_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_19_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_19_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_19_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_19_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_19_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_19_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __orderId.name() : __orderId,
        __giftCardResponse.name() : __giftCardResponse,
        __response.name() : __response,
        __litleTxnId.name() : __litleTxnId,
        __responseTime.name() : __responseTime,
        __message.name() : __message,
        __postDate.name() : __postDate
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}postDay uses Python identifier postDay
    __postDay = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDay'), 'postDay', '__httpwww_litle_comschema_CTD_ANON_20_httpwww_litle_comschemapostDay', False)

    
    postDay = property(__postDay.value, __postDay.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantId uses Python identifier merchantId
    __merchantId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantId'), 'merchantId', '__httpwww_litle_comschema_CTD_ANON_20_httpwww_litle_comschemamerchantId', False)

    
    merchantId = property(__merchantId.value, __merchantId.set, None, None)


    _ElementMap = {
        __postDay.name() : __postDay,
        __merchantId.name() : __merchantId
    }
    _AttributeMap = {
        
    }



# Complex type {http://www.litle.com/schema}updateCardValidationNumOnToken with content type ELEMENT_ONLY
class updateCardValidationNumOnToken_ (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'updateCardValidationNumOnToken')
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}cardValidationNum uses Python identifier cardValidationNum
    __cardValidationNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), 'cardValidationNum', '__httpwww_litle_comschema_updateCardValidationNumOnToken__httpwww_litle_comschemacardValidationNum', False)

    
    cardValidationNum = property(__cardValidationNum.value, __cardValidationNum.set, None, None)

    
    # Element {http://www.litle.com/schema}litleToken uses Python identifier litleToken
    __litleToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), 'litleToken', '__httpwww_litle_comschema_updateCardValidationNumOnToken__httpwww_litle_comschemalitleToken', False)

    
    litleToken = property(__litleToken.value, __litleToken.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_updateCardValidationNumOnToken__httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __cardValidationNum.name() : __cardValidationNum,
        __litleToken.name() : __litleToken,
        __orderId.name() : __orderId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'updateCardValidationNumOnToken', updateCardValidationNumOnToken_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}transaction uses Python identifier transaction
    __transaction = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'transaction'), 'transaction', '__httpwww_litle_comschema_CTD_ANON_21_httpwww_litle_comschematransaction', True)

    
    transaction = property(__transaction.value, __transaction.set, None, None)

    
    # Element {http://www.litle.com/schema}recurringTransaction uses Python identifier recurringTransaction
    __recurringTransaction = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recurringTransaction'), 'recurringTransaction', '__httpwww_litle_comschema_CTD_ANON_21_httpwww_litle_comschemarecurringTransaction', True)

    
    recurringTransaction = property(__recurringTransaction.value, __recurringTransaction.set, None, None)

    
    # Attribute numCaptures uses Python identifier numCaptures
    __numCaptures = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numCaptures'), 'numCaptures', '__httpwww_litle_comschema_CTD_ANON_21_numCaptures', pyxb.binding.datatypes.integer)
    
    numCaptures = property(__numCaptures.value, __numCaptures.set, None, None)

    
    # Attribute numEcheckVerification uses Python identifier numEcheckVerification
    __numEcheckVerification = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numEcheckVerification'), 'numEcheckVerification', '__httpwww_litle_comschema_CTD_ANON_21_numEcheckVerification', pyxb.binding.datatypes.integer)
    
    numEcheckVerification = property(__numEcheckVerification.value, __numEcheckVerification.set, None, None)

    
    # Attribute captureAmount uses Python identifier captureAmount
    __captureAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'captureAmount'), 'captureAmount', '__httpwww_litle_comschema_CTD_ANON_21_captureAmount', batchTotalAmountType)
    
    captureAmount = property(__captureAmount.value, __captureAmount.set, None, None)

    
    # Attribute numBalanceInquirys uses Python identifier numBalanceInquirys
    __numBalanceInquirys = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numBalanceInquirys'), 'numBalanceInquirys', '__httpwww_litle_comschema_CTD_ANON_21_numBalanceInquirys', pyxb.binding.datatypes.integer)
    
    numBalanceInquirys = property(__numBalanceInquirys.value, __numBalanceInquirys.set, None, None)

    
    # Attribute numExtCaptures uses Python identifier numExtCaptures
    __numExtCaptures = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numExtCaptures'), 'numExtCaptures', '__httpwww_litle_comschema_CTD_ANON_21_numExtCaptures', pyxb.binding.datatypes.integer)
    
    numExtCaptures = property(__numExtCaptures.value, __numExtCaptures.set, None, None)

    
    # Attribute merchantId uses Python identifier merchantId
    __merchantId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'merchantId'), 'merchantId', '__httpwww_litle_comschema_CTD_ANON_21_merchantId', merchantIdentificationType, required=True)
    
    merchantId = property(__merchantId.value, __merchantId.set, None, None)

    
    # Attribute captureGivenAuthAmount uses Python identifier captureGivenAuthAmount
    __captureGivenAuthAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'captureGivenAuthAmount'), 'captureGivenAuthAmount', '__httpwww_litle_comschema_CTD_ANON_21_captureGivenAuthAmount', batchTotalAmountType)
    
    captureGivenAuthAmount = property(__captureGivenAuthAmount.value, __captureGivenAuthAmount.set, None, None)

    
    # Attribute extCaptureAmount uses Python identifier extCaptureAmount
    __extCaptureAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'extCaptureAmount'), 'extCaptureAmount', '__httpwww_litle_comschema_CTD_ANON_21_extCaptureAmount', batchTotalAmountType)
    
    extCaptureAmount = property(__extCaptureAmount.value, __extCaptureAmount.set, None, None)

    
    # Attribute numAccountUpdates uses Python identifier numAccountUpdates
    __numAccountUpdates = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numAccountUpdates'), 'numAccountUpdates', '__httpwww_litle_comschema_CTD_ANON_21_numAccountUpdates', pyxb.binding.datatypes.integer)
    
    numAccountUpdates = property(__numAccountUpdates.value, __numAccountUpdates.set, None, None)

    
    # Attribute unloadAmount uses Python identifier unloadAmount
    __unloadAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unloadAmount'), 'unloadAmount', '__httpwww_litle_comschema_CTD_ANON_21_unloadAmount', batchTotalAmountType)
    
    unloadAmount = property(__unloadAmount.value, __unloadAmount.set, None, None)

    
    # Attribute numCredits uses Python identifier numCredits
    __numCredits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numCredits'), 'numCredits', '__httpwww_litle_comschema_CTD_ANON_21_numCredits', pyxb.binding.datatypes.integer)
    
    numCredits = property(__numCredits.value, __numCredits.set, None, None)

    
    # Attribute numTokenRegistrations uses Python identifier numTokenRegistrations
    __numTokenRegistrations = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numTokenRegistrations'), 'numTokenRegistrations', '__httpwww_litle_comschema_CTD_ANON_21_numTokenRegistrations', pyxb.binding.datatypes.integer)
    
    numTokenRegistrations = property(__numTokenRegistrations.value, __numTokenRegistrations.set, None, None)

    
    # Attribute numAuthReversals uses Python identifier numAuthReversals
    __numAuthReversals = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numAuthReversals'), 'numAuthReversals', '__httpwww_litle_comschema_CTD_ANON_21_numAuthReversals', pyxb.binding.datatypes.integer)
    
    numAuthReversals = property(__numAuthReversals.value, __numAuthReversals.set, None, None)

    
    # Attribute creditAmount uses Python identifier creditAmount
    __creditAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'creditAmount'), 'creditAmount', '__httpwww_litle_comschema_CTD_ANON_21_creditAmount', batchTotalAmountType)
    
    creditAmount = property(__creditAmount.value, __creditAmount.set, None, None)

    
    # Attribute numUpdateCardValidationNumOnTokens uses Python identifier numUpdateCardValidationNumOnTokens
    __numUpdateCardValidationNumOnTokens = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numUpdateCardValidationNumOnTokens'), 'numUpdateCardValidationNumOnTokens', '__httpwww_litle_comschema_CTD_ANON_21_numUpdateCardValidationNumOnTokens', pyxb.binding.datatypes.integer)
    
    numUpdateCardValidationNumOnTokens = property(__numUpdateCardValidationNumOnTokens.value, __numUpdateCardValidationNumOnTokens.set, None, None)

    
    # Attribute numForceCaptures uses Python identifier numForceCaptures
    __numForceCaptures = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numForceCaptures'), 'numForceCaptures', '__httpwww_litle_comschema_CTD_ANON_21_numForceCaptures', pyxb.binding.datatypes.integer)
    
    numForceCaptures = property(__numForceCaptures.value, __numForceCaptures.set, None, None)

    
    # Attribute numCancelSubscriptions uses Python identifier numCancelSubscriptions
    __numCancelSubscriptions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numCancelSubscriptions'), 'numCancelSubscriptions', '__httpwww_litle_comschema_CTD_ANON_21_numCancelSubscriptions', pyxb.binding.datatypes.integer)
    
    numCancelSubscriptions = property(__numCancelSubscriptions.value, __numCancelSubscriptions.set, None, None)

    
    # Attribute forceCaptureAmount uses Python identifier forceCaptureAmount
    __forceCaptureAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'forceCaptureAmount'), 'forceCaptureAmount', '__httpwww_litle_comschema_CTD_ANON_21_forceCaptureAmount', batchTotalAmountType)
    
    forceCaptureAmount = property(__forceCaptureAmount.value, __forceCaptureAmount.set, None, None)

    
    # Attribute numUpdateSubscriptions uses Python identifier numUpdateSubscriptions
    __numUpdateSubscriptions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numUpdateSubscriptions'), 'numUpdateSubscriptions', '__httpwww_litle_comschema_CTD_ANON_21_numUpdateSubscriptions', pyxb.binding.datatypes.integer)
    
    numUpdateSubscriptions = property(__numUpdateSubscriptions.value, __numUpdateSubscriptions.set, None, None)

    
    # Attribute numSales uses Python identifier numSales
    __numSales = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numSales'), 'numSales', '__httpwww_litle_comschema_CTD_ANON_21_numSales', pyxb.binding.datatypes.integer)
    
    numSales = property(__numSales.value, __numSales.set, None, None)

    
    # Attribute numCreatePlans uses Python identifier numCreatePlans
    __numCreatePlans = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numCreatePlans'), 'numCreatePlans', '__httpwww_litle_comschema_CTD_ANON_21_numCreatePlans', pyxb.binding.datatypes.integer)
    
    numCreatePlans = property(__numCreatePlans.value, __numCreatePlans.set, None, None)

    
    # Attribute numAuths uses Python identifier numAuths
    __numAuths = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numAuths'), 'numAuths', '__httpwww_litle_comschema_CTD_ANON_21_numAuths', pyxb.binding.datatypes.integer)
    
    numAuths = property(__numAuths.value, __numAuths.set, None, None)

    
    # Attribute saleAmount uses Python identifier saleAmount
    __saleAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'saleAmount'), 'saleAmount', '__httpwww_litle_comschema_CTD_ANON_21_saleAmount', batchTotalAmountType)
    
    saleAmount = property(__saleAmount.value, __saleAmount.set, None, None)

    
    # Attribute numUpdatePlans uses Python identifier numUpdatePlans
    __numUpdatePlans = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numUpdatePlans'), 'numUpdatePlans', '__httpwww_litle_comschema_CTD_ANON_21_numUpdatePlans', pyxb.binding.datatypes.integer)
    
    numUpdatePlans = property(__numUpdatePlans.value, __numUpdatePlans.set, None, None)

    
    # Attribute echeckVerificationAmount uses Python identifier echeckVerificationAmount
    __echeckVerificationAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'echeckVerificationAmount'), 'echeckVerificationAmount', '__httpwww_litle_comschema_CTD_ANON_21_echeckVerificationAmount', batchTotalAmountType)
    
    echeckVerificationAmount = property(__echeckVerificationAmount.value, __echeckVerificationAmount.set, None, None)

    
    # Attribute merchantSdk uses Python identifier merchantSdk
    __merchantSdk = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'merchantSdk'), 'merchantSdk', '__httpwww_litle_comschema_CTD_ANON_21_merchantSdk', pyxb.binding.datatypes.string)
    
    merchantSdk = property(__merchantSdk.value, __merchantSdk.set, None, None)

    
    # Attribute numActivates uses Python identifier numActivates
    __numActivates = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numActivates'), 'numActivates', '__httpwww_litle_comschema_CTD_ANON_21_numActivates', pyxb.binding.datatypes.integer)
    
    numActivates = property(__numActivates.value, __numActivates.set, None, None)

    
    # Attribute authReversalAmount uses Python identifier authReversalAmount
    __authReversalAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'authReversalAmount'), 'authReversalAmount', '__httpwww_litle_comschema_CTD_ANON_21_authReversalAmount', batchTotalAmountType)
    
    authReversalAmount = property(__authReversalAmount.value, __authReversalAmount.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_litle_comschema_CTD_ANON_21_id', string25Type)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute numDeactivates uses Python identifier numDeactivates
    __numDeactivates = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numDeactivates'), 'numDeactivates', '__httpwww_litle_comschema_CTD_ANON_21_numDeactivates', pyxb.binding.datatypes.integer)
    
    numDeactivates = property(__numDeactivates.value, __numDeactivates.set, None, None)

    
    # Attribute numEcheckSales uses Python identifier numEcheckSales
    __numEcheckSales = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numEcheckSales'), 'numEcheckSales', '__httpwww_litle_comschema_CTD_ANON_21_numEcheckSales', pyxb.binding.datatypes.integer)
    
    numEcheckSales = property(__numEcheckSales.value, __numEcheckSales.set, None, None)

    
    # Attribute activateAmount uses Python identifier activateAmount
    __activateAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'activateAmount'), 'activateAmount', '__httpwww_litle_comschema_CTD_ANON_21_activateAmount', batchTotalAmountType)
    
    activateAmount = property(__activateAmount.value, __activateAmount.set, None, None)

    
    # Attribute numCaptureGivenAuths uses Python identifier numCaptureGivenAuths
    __numCaptureGivenAuths = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numCaptureGivenAuths'), 'numCaptureGivenAuths', '__httpwww_litle_comschema_CTD_ANON_21_numCaptureGivenAuths', pyxb.binding.datatypes.integer)
    
    numCaptureGivenAuths = property(__numCaptureGivenAuths.value, __numCaptureGivenAuths.set, None, None)

    
    # Attribute authAmount uses Python identifier authAmount
    __authAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'authAmount'), 'authAmount', '__httpwww_litle_comschema_CTD_ANON_21_authAmount', batchTotalAmountType)
    
    authAmount = property(__authAmount.value, __authAmount.set, None, None)

    
    # Attribute numLoads uses Python identifier numLoads
    __numLoads = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numLoads'), 'numLoads', '__httpwww_litle_comschema_CTD_ANON_21_numLoads', pyxb.binding.datatypes.integer)
    
    numLoads = property(__numLoads.value, __numLoads.set, None, None)

    
    # Attribute numEcheckCredit uses Python identifier numEcheckCredit
    __numEcheckCredit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numEcheckCredit'), 'numEcheckCredit', '__httpwww_litle_comschema_CTD_ANON_21_numEcheckCredit', pyxb.binding.datatypes.integer)
    
    numEcheckCredit = property(__numEcheckCredit.value, __numEcheckCredit.set, None, None)

    
    # Attribute loadAmount uses Python identifier loadAmount
    __loadAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loadAmount'), 'loadAmount', '__httpwww_litle_comschema_CTD_ANON_21_loadAmount', batchTotalAmountType)
    
    loadAmount = property(__loadAmount.value, __loadAmount.set, None, None)

    
    # Attribute echeckSalesAmount uses Python identifier echeckSalesAmount
    __echeckSalesAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'echeckSalesAmount'), 'echeckSalesAmount', '__httpwww_litle_comschema_CTD_ANON_21_echeckSalesAmount', batchTotalAmountType)
    
    echeckSalesAmount = property(__echeckSalesAmount.value, __echeckSalesAmount.set, None, None)

    
    # Attribute echeckCreditAmount uses Python identifier echeckCreditAmount
    __echeckCreditAmount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'echeckCreditAmount'), 'echeckCreditAmount', '__httpwww_litle_comschema_CTD_ANON_21_echeckCreditAmount', batchTotalAmountType)
    
    echeckCreditAmount = property(__echeckCreditAmount.value, __echeckCreditAmount.set, None, None)

    
    # Attribute numUnloads uses Python identifier numUnloads
    __numUnloads = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numUnloads'), 'numUnloads', '__httpwww_litle_comschema_CTD_ANON_21_numUnloads', pyxb.binding.datatypes.integer)
    
    numUnloads = property(__numUnloads.value, __numUnloads.set, None, None)

    
    # Attribute numEcheckRedeposit uses Python identifier numEcheckRedeposit
    __numEcheckRedeposit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numEcheckRedeposit'), 'numEcheckRedeposit', '__httpwww_litle_comschema_CTD_ANON_21_numEcheckRedeposit', pyxb.binding.datatypes.integer)
    
    numEcheckRedeposit = property(__numEcheckRedeposit.value, __numEcheckRedeposit.set, None, None)


    _ElementMap = {
        __transaction.name() : __transaction,
        __recurringTransaction.name() : __recurringTransaction
    }
    _AttributeMap = {
        __numCaptures.name() : __numCaptures,
        __numEcheckVerification.name() : __numEcheckVerification,
        __captureAmount.name() : __captureAmount,
        __numBalanceInquirys.name() : __numBalanceInquirys,
        __numExtCaptures.name() : __numExtCaptures,
        __merchantId.name() : __merchantId,
        __captureGivenAuthAmount.name() : __captureGivenAuthAmount,
        __extCaptureAmount.name() : __extCaptureAmount,
        __numAccountUpdates.name() : __numAccountUpdates,
        __unloadAmount.name() : __unloadAmount,
        __numCredits.name() : __numCredits,
        __numTokenRegistrations.name() : __numTokenRegistrations,
        __numAuthReversals.name() : __numAuthReversals,
        __creditAmount.name() : __creditAmount,
        __numUpdateCardValidationNumOnTokens.name() : __numUpdateCardValidationNumOnTokens,
        __numForceCaptures.name() : __numForceCaptures,
        __numCancelSubscriptions.name() : __numCancelSubscriptions,
        __forceCaptureAmount.name() : __forceCaptureAmount,
        __numUpdateSubscriptions.name() : __numUpdateSubscriptions,
        __numSales.name() : __numSales,
        __numCreatePlans.name() : __numCreatePlans,
        __numAuths.name() : __numAuths,
        __saleAmount.name() : __saleAmount,
        __numUpdatePlans.name() : __numUpdatePlans,
        __echeckVerificationAmount.name() : __echeckVerificationAmount,
        __merchantSdk.name() : __merchantSdk,
        __numActivates.name() : __numActivates,
        __authReversalAmount.name() : __authReversalAmount,
        __id.name() : __id,
        __numDeactivates.name() : __numDeactivates,
        __numEcheckSales.name() : __numEcheckSales,
        __activateAmount.name() : __activateAmount,
        __numCaptureGivenAuths.name() : __numCaptureGivenAuths,
        __authAmount.name() : __authAmount,
        __numLoads.name() : __numLoads,
        __numEcheckCredit.name() : __numEcheckCredit,
        __loadAmount.name() : __loadAmount,
        __echeckSalesAmount.name() : __echeckSalesAmount,
        __echeckCreditAmount.name() : __echeckCreditAmount,
        __numUnloads.name() : __numUnloads,
        __numEcheckRedeposit.name() : __numEcheckRedeposit
    }



# Complex type {http://www.litle.com/schema}virtualGiftCardType with content type ELEMENT_ONLY
class virtualGiftCardType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualGiftCardType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}giftCardBin uses Python identifier giftCardBin
    __giftCardBin = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardBin'), 'giftCardBin', '__httpwww_litle_comschema_virtualGiftCardType_httpwww_litle_comschemagiftCardBin', False)

    
    giftCardBin = property(__giftCardBin.value, __giftCardBin.set, None, None)

    
    # Element {http://www.litle.com/schema}accountNumberLength uses Python identifier accountNumberLength
    __accountNumberLength = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountNumberLength'), 'accountNumberLength', '__httpwww_litle_comschema_virtualGiftCardType_httpwww_litle_comschemaaccountNumberLength', False)

    
    accountNumberLength = property(__accountNumberLength.value, __accountNumberLength.set, None, None)


    _ElementMap = {
        __giftCardBin.name() : __giftCardBin,
        __accountNumberLength.name() : __accountNumberLength
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'virtualGiftCardType', virtualGiftCardType)


# Complex type {http://www.litle.com/schema}tokenResponseType with content type ELEMENT_ONLY
class tokenResponseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'tokenResponseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}type uses Python identifier type
    __type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_litle_comschema_tokenResponseType_httpwww_litle_comschematype', False)

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponseCode uses Python identifier tokenResponseCode
    __tokenResponseCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponseCode'), 'tokenResponseCode', '__httpwww_litle_comschema_tokenResponseType_httpwww_litle_comschematokenResponseCode', False)

    
    tokenResponseCode = property(__tokenResponseCode.value, __tokenResponseCode.set, None, None)

    
    # Element {http://www.litle.com/schema}bin uses Python identifier bin
    __bin = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bin'), 'bin', '__httpwww_litle_comschema_tokenResponseType_httpwww_litle_comschemabin', False)

    
    bin = property(__bin.value, __bin.set, None, None)

    
    # Element {http://www.litle.com/schema}eCheckAccountSuffix uses Python identifier eCheckAccountSuffix
    __eCheckAccountSuffix = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'eCheckAccountSuffix'), 'eCheckAccountSuffix', '__httpwww_litle_comschema_tokenResponseType_httpwww_litle_comschemaeCheckAccountSuffix', False)

    
    eCheckAccountSuffix = property(__eCheckAccountSuffix.value, __eCheckAccountSuffix.set, None, None)

    
    # Element {http://www.litle.com/schema}litleToken uses Python identifier litleToken
    __litleToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), 'litleToken', '__httpwww_litle_comschema_tokenResponseType_httpwww_litle_comschemalitleToken', False)

    
    litleToken = property(__litleToken.value, __litleToken.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenMessage uses Python identifier tokenMessage
    __tokenMessage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenMessage'), 'tokenMessage', '__httpwww_litle_comschema_tokenResponseType_httpwww_litle_comschematokenMessage', False)

    
    tokenMessage = property(__tokenMessage.value, __tokenMessage.set, None, None)


    _ElementMap = {
        __type.name() : __type,
        __tokenResponseCode.name() : __tokenResponseCode,
        __bin.name() : __bin,
        __eCheckAccountSuffix.name() : __eCheckAccountSuffix,
        __litleToken.name() : __litleToken,
        __tokenMessage.name() : __tokenMessage
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'tokenResponseType', tokenResponseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (recurringTransactionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is recurringTransactionType
    
    # Element {http://www.litle.com/schema}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpwww_litle_comschema_CTD_ANON_22_httpwww_litle_comschemadescription', False)

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://www.litle.com/schema}planCode uses Python identifier planCode
    __planCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'planCode'), 'planCode', '__httpwww_litle_comschema_CTD_ANON_22_httpwww_litle_comschemaplanCode', False)

    
    planCode = property(__planCode.value, __planCode.set, None, None)

    
    # Element {http://www.litle.com/schema}active uses Python identifier active
    __active = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpwww_litle_comschema_CTD_ANON_22_httpwww_litle_comschemaactive', False)

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://www.litle.com/schema}trialNumberOfIntervals uses Python identifier trialNumberOfIntervals
    __trialNumberOfIntervals = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'trialNumberOfIntervals'), 'trialNumberOfIntervals', '__httpwww_litle_comschema_CTD_ANON_22_httpwww_litle_comschematrialNumberOfIntervals', False)

    
    trialNumberOfIntervals = property(__trialNumberOfIntervals.value, __trialNumberOfIntervals.set, None, None)

    
    # Element {http://www.litle.com/schema}intervalType uses Python identifier intervalType
    __intervalType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'intervalType'), 'intervalType', '__httpwww_litle_comschema_CTD_ANON_22_httpwww_litle_comschemaintervalType', False)

    
    intervalType = property(__intervalType.value, __intervalType.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_22_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}numberOfPayments uses Python identifier numberOfPayments
    __numberOfPayments = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numberOfPayments'), 'numberOfPayments', '__httpwww_litle_comschema_CTD_ANON_22_httpwww_litle_comschemanumberOfPayments', False)

    
    numberOfPayments = property(__numberOfPayments.value, __numberOfPayments.set, None, None)

    
    # Element {http://www.litle.com/schema}trialIntervalType uses Python identifier trialIntervalType
    __trialIntervalType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'trialIntervalType'), 'trialIntervalType', '__httpwww_litle_comschema_CTD_ANON_22_httpwww_litle_comschematrialIntervalType', False)

    
    trialIntervalType = property(__trialIntervalType.value, __trialIntervalType.set, None, None)

    
    # Element {http://www.litle.com/schema}name uses Python identifier name
    __name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_litle_comschema_CTD_ANON_22_httpwww_litle_comschemaname', False)

    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = recurringTransactionType._ElementMap.copy()
    _ElementMap.update({
        __description.name() : __description,
        __planCode.name() : __planCode,
        __active.name() : __active,
        __trialNumberOfIntervals.name() : __trialNumberOfIntervals,
        __intervalType.name() : __intervalType,
        __amount.name() : __amount,
        __numberOfPayments.name() : __numberOfPayments,
        __trialIntervalType.name() : __trialIntervalType,
        __name.name() : __name
    })
    _AttributeMap = recurringTransactionType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}contact with content type ELEMENT_ONLY
class contact (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'contact')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}email uses Python identifier email
    __email = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'email'), 'email', '__httpwww_litle_comschema_contact_httpwww_litle_comschemaemail', False)

    
    email = property(__email.value, __email.set, None, None)

    
    # Element {http://www.litle.com/schema}addressLine1 uses Python identifier addressLine1
    __addressLine1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addressLine1'), 'addressLine1', '__httpwww_litle_comschema_contact_httpwww_litle_comschemaaddressLine1', False)

    
    addressLine1 = property(__addressLine1.value, __addressLine1.set, None, None)

    
    # Element {http://www.litle.com/schema}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'firstName'), 'firstName', '__httpwww_litle_comschema_contact_httpwww_litle_comschemafirstName', False)

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://www.litle.com/schema}state uses Python identifier state
    __state = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'state'), 'state', '__httpwww_litle_comschema_contact_httpwww_litle_comschemastate', False)

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {http://www.litle.com/schema}middleInitial uses Python identifier middleInitial
    __middleInitial = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'middleInitial'), 'middleInitial', '__httpwww_litle_comschema_contact_httpwww_litle_comschemamiddleInitial', False)

    
    middleInitial = property(__middleInitial.value, __middleInitial.set, None, None)

    
    # Element {http://www.litle.com/schema}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'phone'), 'phone', '__httpwww_litle_comschema_contact_httpwww_litle_comschemaphone', False)

    
    phone = property(__phone.value, __phone.set, None, None)

    
    # Element {http://www.litle.com/schema}zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'zip'), 'zip', '__httpwww_litle_comschema_contact_httpwww_litle_comschemazip', False)

    
    zip = property(__zip.value, __zip.set, None, None)

    
    # Element {http://www.litle.com/schema}companyName uses Python identifier companyName
    __companyName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'companyName'), 'companyName', '__httpwww_litle_comschema_contact_httpwww_litle_comschemacompanyName', False)

    
    companyName = property(__companyName.value, __companyName.set, None, None)

    
    # Element {http://www.litle.com/schema}addressLine2 uses Python identifier addressLine2
    __addressLine2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addressLine2'), 'addressLine2', '__httpwww_litle_comschema_contact_httpwww_litle_comschemaaddressLine2', False)

    
    addressLine2 = property(__addressLine2.value, __addressLine2.set, None, None)

    
    # Element {http://www.litle.com/schema}addressLine3 uses Python identifier addressLine3
    __addressLine3 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addressLine3'), 'addressLine3', '__httpwww_litle_comschema_contact_httpwww_litle_comschemaaddressLine3', False)

    
    addressLine3 = property(__addressLine3.value, __addressLine3.set, None, None)

    
    # Element {http://www.litle.com/schema}country uses Python identifier country
    __country = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'country'), 'country', '__httpwww_litle_comschema_contact_httpwww_litle_comschemacountry', False)

    
    country = property(__country.value, __country.set, None, None)

    
    # Element {http://www.litle.com/schema}name uses Python identifier name
    __name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_litle_comschema_contact_httpwww_litle_comschemaname', False)

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.litle.com/schema}city uses Python identifier city
    __city = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httpwww_litle_comschema_contact_httpwww_litle_comschemacity', False)

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://www.litle.com/schema}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lastName'), 'lastName', '__httpwww_litle_comschema_contact_httpwww_litle_comschemalastName', False)

    
    lastName = property(__lastName.value, __lastName.set, None, None)


    _ElementMap = {
        __email.name() : __email,
        __addressLine1.name() : __addressLine1,
        __firstName.name() : __firstName,
        __state.name() : __state,
        __middleInitial.name() : __middleInitial,
        __phone.name() : __phone,
        __zip.name() : __zip,
        __companyName.name() : __companyName,
        __addressLine2.name() : __addressLine2,
        __addressLine3.name() : __addressLine3,
        __country.name() : __country,
        __name.name() : __name,
        __city.name() : __city,
        __lastName.name() : __lastName
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'contact', contact)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}password uses Python identifier password
    __password = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'password'), 'password', '__httpwww_litle_comschema_CTD_ANON_23_httpwww_litle_comschemapassword', False)

    
    password = property(__password.value, __password.set, None, None)

    
    # Element {http://www.litle.com/schema}user uses Python identifier user
    __user = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'user'), 'user', '__httpwww_litle_comschema_CTD_ANON_23_httpwww_litle_comschemauser', False)

    
    user = property(__user.value, __user.set, None, None)


    _ElementMap = {
        __password.name() : __password,
        __user.name() : __user
    }
    _AttributeMap = {
        
    }



# Complex type {http://www.litle.com/schema}mposType with content type ELEMENT_ONLY
class mposType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'mposType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}encryptedTrack uses Python identifier encryptedTrack
    __encryptedTrack = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'encryptedTrack'), 'encryptedTrack', '__httpwww_litle_comschema_mposType_httpwww_litle_comschemaencryptedTrack', False)

    
    encryptedTrack = property(__encryptedTrack.value, __encryptedTrack.set, None, None)

    
    # Element {http://www.litle.com/schema}ksn uses Python identifier ksn
    __ksn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ksn'), 'ksn', '__httpwww_litle_comschema_mposType_httpwww_litle_comschemaksn', False)

    
    ksn = property(__ksn.value, __ksn.set, None, None)

    
    # Element {http://www.litle.com/schema}track2Status uses Python identifier track2Status
    __track2Status = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'track2Status'), 'track2Status', '__httpwww_litle_comschema_mposType_httpwww_litle_comschematrack2Status', False)

    
    track2Status = property(__track2Status.value, __track2Status.set, None, None)

    
    # Element {http://www.litle.com/schema}track1Status uses Python identifier track1Status
    __track1Status = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'track1Status'), 'track1Status', '__httpwww_litle_comschema_mposType_httpwww_litle_comschematrack1Status', False)

    
    track1Status = property(__track1Status.value, __track1Status.set, None, None)

    
    # Element {http://www.litle.com/schema}formatId uses Python identifier formatId
    __formatId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'formatId'), 'formatId', '__httpwww_litle_comschema_mposType_httpwww_litle_comschemaformatId', False)

    
    formatId = property(__formatId.value, __formatId.set, None, None)


    _ElementMap = {
        __encryptedTrack.name() : __encryptedTrack,
        __ksn.name() : __ksn,
        __track2Status.name() : __track2Status,
        __track1Status.name() : __track1Status,
        __formatId.name() : __formatId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'mposType', mposType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}quantity uses Python identifier quantity
    __quantity = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'quantity'), 'quantity', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemaquantity', False)

    
    quantity = property(__quantity.value, __quantity.set, None, None)

    
    # Element {http://www.litle.com/schema}lineItemTotalWithTax uses Python identifier lineItemTotalWithTax
    __lineItemTotalWithTax = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lineItemTotalWithTax'), 'lineItemTotalWithTax', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemalineItemTotalWithTax', False)

    
    lineItemTotalWithTax = property(__lineItemTotalWithTax.value, __lineItemTotalWithTax.set, None, None)

    
    # Element {http://www.litle.com/schema}itemDescription uses Python identifier itemDescription
    __itemDescription = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'itemDescription'), 'itemDescription', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemaitemDescription', False)

    
    itemDescription = property(__itemDescription.value, __itemDescription.set, None, None)

    
    # Element {http://www.litle.com/schema}itemSequenceNumber uses Python identifier itemSequenceNumber
    __itemSequenceNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'itemSequenceNumber'), 'itemSequenceNumber', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemaitemSequenceNumber', False)

    
    itemSequenceNumber = property(__itemSequenceNumber.value, __itemSequenceNumber.set, None, None)

    
    # Element {http://www.litle.com/schema}itemDiscountAmount uses Python identifier itemDiscountAmount
    __itemDiscountAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'itemDiscountAmount'), 'itemDiscountAmount', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemaitemDiscountAmount', False)

    
    itemDiscountAmount = property(__itemDiscountAmount.value, __itemDiscountAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}taxAmount uses Python identifier taxAmount
    __taxAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxAmount'), 'taxAmount', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemataxAmount', False)

    
    taxAmount = property(__taxAmount.value, __taxAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}lineItemTotal uses Python identifier lineItemTotal
    __lineItemTotal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lineItemTotal'), 'lineItemTotal', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemalineItemTotal', False)

    
    lineItemTotal = property(__lineItemTotal.value, __lineItemTotal.set, None, None)

    
    # Element {http://www.litle.com/schema}commodityCode uses Python identifier commodityCode
    __commodityCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'commodityCode'), 'commodityCode', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemacommodityCode', False)

    
    commodityCode = property(__commodityCode.value, __commodityCode.set, None, None)

    
    # Element {http://www.litle.com/schema}detailTax uses Python identifier detailTax
    __detailTax = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'detailTax'), 'detailTax', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemadetailTax', True)

    
    detailTax = property(__detailTax.value, __detailTax.set, None, None)

    
    # Element {http://www.litle.com/schema}unitOfMeasure uses Python identifier unitOfMeasure
    __unitOfMeasure = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'unitOfMeasure'), 'unitOfMeasure', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemaunitOfMeasure', False)

    
    unitOfMeasure = property(__unitOfMeasure.value, __unitOfMeasure.set, None, None)

    
    # Element {http://www.litle.com/schema}productCode uses Python identifier productCode
    __productCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'productCode'), 'productCode', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemaproductCode', False)

    
    productCode = property(__productCode.value, __productCode.set, None, None)

    
    # Element {http://www.litle.com/schema}unitCost uses Python identifier unitCost
    __unitCost = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'unitCost'), 'unitCost', '__httpwww_litle_comschema_CTD_ANON_24_httpwww_litle_comschemaunitCost', False)

    
    unitCost = property(__unitCost.value, __unitCost.set, None, None)


    _ElementMap = {
        __quantity.name() : __quantity,
        __lineItemTotalWithTax.name() : __lineItemTotalWithTax,
        __itemDescription.name() : __itemDescription,
        __itemSequenceNumber.name() : __itemSequenceNumber,
        __itemDiscountAmount.name() : __itemDiscountAmount,
        __taxAmount.name() : __taxAmount,
        __lineItemTotal.name() : __lineItemTotal,
        __commodityCode.name() : __commodityCode,
        __detailTax.name() : __detailTax,
        __unitOfMeasure.name() : __unitOfMeasure,
        __productCode.name() : __productCode,
        __unitCost.name() : __unitCost
    }
    _AttributeMap = {
        
    }



# Complex type {http://www.litle.com/schema}accountInfoType with content type ELEMENT_ONLY
class accountInfoType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accountInfoType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}number uses Python identifier number
    __number = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'number'), 'number', '__httpwww_litle_comschema_accountInfoType_httpwww_litle_comschemanumber', False)

    
    number = property(__number.value, __number.set, None, None)

    
    # Element {http://www.litle.com/schema}type uses Python identifier type
    __type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_litle_comschema_accountInfoType_httpwww_litle_comschematype', False)

    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        __number.name() : __number,
        __type.name() : __type
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'accountInfoType', accountInfoType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_25_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_25_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_25_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_25_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_25_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_25_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_25_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __response.name() : __response,
        __responseTime.name() : __responseTime,
        __orderId.name() : __orderId,
        __giftCardResponse.name() : __giftCardResponse,
        __litleTxnId.name() : __litleTxnId,
        __message.name() : __message,
        __postDate.name() : __postDate
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_26_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}recyclingType with content type ELEMENT_ONLY
class recyclingType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recyclingType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}recycleEngineActive uses Python identifier recycleEngineActive
    __recycleEngineActive = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recycleEngineActive'), 'recycleEngineActive', '__httpwww_litle_comschema_recyclingType_httpwww_litle_comschemarecycleEngineActive', False)

    
    recycleEngineActive = property(__recycleEngineActive.value, __recycleEngineActive.set, None, None)

    
    # Element {http://www.litle.com/schema}recycleAdvice uses Python identifier recycleAdvice
    __recycleAdvice = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recycleAdvice'), 'recycleAdvice', '__httpwww_litle_comschema_recyclingType_httpwww_litle_comschemarecycleAdvice', False)

    
    recycleAdvice = property(__recycleAdvice.value, __recycleAdvice.set, None, None)


    _ElementMap = {
        __recycleEngineActive.name() : __recycleEngineActive,
        __recycleAdvice.name() : __recycleAdvice
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'recyclingType', recyclingType)


# Complex type {http://www.litle.com/schema}recurringResponseType with content type ELEMENT_ONLY
class recurringResponseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recurringResponseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}recurringTxnId uses Python identifier recurringTxnId
    __recurringTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recurringTxnId'), 'recurringTxnId', '__httpwww_litle_comschema_recurringResponseType_httpwww_litle_comschemarecurringTxnId', False)

    
    recurringTxnId = property(__recurringTxnId.value, __recurringTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}responseMessage uses Python identifier responseMessage
    __responseMessage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseMessage'), 'responseMessage', '__httpwww_litle_comschema_recurringResponseType_httpwww_litle_comschemaresponseMessage', False)

    
    responseMessage = property(__responseMessage.value, __responseMessage.set, None, None)

    
    # Element {http://www.litle.com/schema}subscriptionId uses Python identifier subscriptionId
    __subscriptionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), 'subscriptionId', '__httpwww_litle_comschema_recurringResponseType_httpwww_litle_comschemasubscriptionId', False)

    
    subscriptionId = property(__subscriptionId.value, __subscriptionId.set, None, None)

    
    # Element {http://www.litle.com/schema}responseCode uses Python identifier responseCode
    __responseCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseCode'), 'responseCode', '__httpwww_litle_comschema_recurringResponseType_httpwww_litle_comschemaresponseCode', False)

    
    responseCode = property(__responseCode.value, __responseCode.set, None, None)


    _ElementMap = {
        __recurringTxnId.name() : __recurringTxnId,
        __responseMessage.name() : __responseMessage,
        __subscriptionId.name() : __subscriptionId,
        __responseCode.name() : __responseCode
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'recurringResponseType', recurringResponseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_27_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_27_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_27_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_27_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_27_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponse uses Python identifier tokenResponse
    __tokenResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), 'tokenResponse', '__httpwww_litle_comschema_CTD_ANON_27_httpwww_litle_comschematokenResponse', False)

    
    tokenResponse = property(__tokenResponse.value, __tokenResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_27_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_27_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_27_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httpwww_litle_comschema_CTD_ANON_27_duplicate', pyxb.binding.datatypes.boolean)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __postDate.name() : __postDate,
        __litleTxnId.name() : __litleTxnId,
        __orderId.name() : __orderId,
        __message.name() : __message,
        __fraudResult.name() : __fraudResult,
        __tokenResponse.name() : __tokenResponse,
        __responseTime.name() : __responseTime,
        __giftCardResponse.name() : __giftCardResponse,
        __response.name() : __response
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_28_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}updatedCard uses Python identifier updatedCard
    __updatedCard = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'updatedCard'), 'updatedCard', '__httpwww_litle_comschema_CTD_ANON_28_httpwww_litle_comschemaupdatedCard', False)

    
    updatedCard = property(__updatedCard.value, __updatedCard.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_28_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}updatedToken uses Python identifier updatedToken
    __updatedToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'updatedToken'), 'updatedToken', '__httpwww_litle_comschema_CTD_ANON_28_httpwww_litle_comschemaupdatedToken', False)

    
    updatedToken = property(__updatedToken.value, __updatedToken.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_28_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}originalCard uses Python identifier originalCard
    __originalCard = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'originalCard'), 'originalCard', '__httpwww_litle_comschema_CTD_ANON_28_httpwww_litle_comschemaoriginalCard', False)

    
    originalCard = property(__originalCard.value, __originalCard.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_28_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_28_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}originalToken uses Python identifier originalToken
    __originalToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'originalToken'), 'originalToken', '__httpwww_litle_comschema_CTD_ANON_28_httpwww_litle_comschemaoriginalToken', False)

    
    originalToken = property(__originalToken.value, __originalToken.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __orderId.name() : __orderId,
        __updatedCard.name() : __updatedCard,
        __response.name() : __response,
        __updatedToken.name() : __updatedToken,
        __litleTxnId.name() : __litleTxnId,
        __originalCard.name() : __originalCard,
        __responseTime.name() : __responseTime,
        __message.name() : __message,
        __originalToken.name() : __originalToken
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}litleSessionId uses Python identifier litleSessionId
    __litleSessionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleSessionId'), 'litleSessionId', '__httpwww_litle_comschema_CTD_ANON_29_httpwww_litle_comschemalitleSessionId', False)

    
    litleSessionId = property(__litleSessionId.value, __litleSessionId.set, None, None)

    
    # Element {http://www.litle.com/schema}accountUpdateFileRequestData uses Python identifier accountUpdateFileRequestData
    __accountUpdateFileRequestData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUpdateFileRequestData'), 'accountUpdateFileRequestData', '__httpwww_litle_comschema_CTD_ANON_29_httpwww_litle_comschemaaccountUpdateFileRequestData', False)

    
    accountUpdateFileRequestData = property(__accountUpdateFileRequestData.value, __accountUpdateFileRequestData.set, None, None)


    _ElementMap = {
        __litleSessionId.name() : __litleSessionId,
        __accountUpdateFileRequestData.name() : __accountUpdateFileRequestData
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}IIASFlag uses Python identifier IIASFlag
    __IIASFlag = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IIASFlag'), 'IIASFlag', '__httpwww_litle_comschema_CTD_ANON_30_httpwww_litle_comschemaIIASFlag', False)

    
    IIASFlag = property(__IIASFlag.value, __IIASFlag.set, None, None)

    
    # Element {http://www.litle.com/schema}healthcareAmounts uses Python identifier healthcareAmounts
    __healthcareAmounts = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'healthcareAmounts'), 'healthcareAmounts', '__httpwww_litle_comschema_CTD_ANON_30_httpwww_litle_comschemahealthcareAmounts', False)

    
    healthcareAmounts = property(__healthcareAmounts.value, __healthcareAmounts.set, None, None)


    _ElementMap = {
        __IIASFlag.name() : __IIASFlag,
        __healthcareAmounts.name() : __healthcareAmounts
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}dentalAmount uses Python identifier dentalAmount
    __dentalAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dentalAmount'), 'dentalAmount', '__httpwww_litle_comschema_CTD_ANON_31_httpwww_litle_comschemadentalAmount', False)

    
    dentalAmount = property(__dentalAmount.value, __dentalAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}visionAmount uses Python identifier visionAmount
    __visionAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'visionAmount'), 'visionAmount', '__httpwww_litle_comschema_CTD_ANON_31_httpwww_litle_comschemavisionAmount', False)

    
    visionAmount = property(__visionAmount.value, __visionAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}RxAmount uses Python identifier RxAmount
    __RxAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RxAmount'), 'RxAmount', '__httpwww_litle_comschema_CTD_ANON_31_httpwww_litle_comschemaRxAmount', False)

    
    RxAmount = property(__RxAmount.value, __RxAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}totalHealthcareAmount uses Python identifier totalHealthcareAmount
    __totalHealthcareAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'totalHealthcareAmount'), 'totalHealthcareAmount', '__httpwww_litle_comschema_CTD_ANON_31_httpwww_litle_comschematotalHealthcareAmount', False)

    
    totalHealthcareAmount = property(__totalHealthcareAmount.value, __totalHealthcareAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}clinicOtherAmount uses Python identifier clinicOtherAmount
    __clinicOtherAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'clinicOtherAmount'), 'clinicOtherAmount', '__httpwww_litle_comschema_CTD_ANON_31_httpwww_litle_comschemaclinicOtherAmount', False)

    
    clinicOtherAmount = property(__clinicOtherAmount.value, __clinicOtherAmount.set, None, None)


    _ElementMap = {
        __dentalAmount.name() : __dentalAmount,
        __visionAmount.name() : __visionAmount,
        __RxAmount.name() : __RxAmount,
        __totalHealthcareAmount.name() : __totalHealthcareAmount,
        __clinicOtherAmount.name() : __clinicOtherAmount
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}virtualAccountNumber uses Python identifier virtualAccountNumber
    __virtualAccountNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualAccountNumber'), 'virtualAccountNumber', '__httpwww_litle_comschema_CTD_ANON_32_httpwww_litle_comschemavirtualAccountNumber', False)

    
    virtualAccountNumber = property(__virtualAccountNumber.value, __virtualAccountNumber.set, None, None)

    
    # Element {http://www.litle.com/schema}cardProductType uses Python identifier cardProductType
    __cardProductType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardProductType'), 'cardProductType', '__httpwww_litle_comschema_CTD_ANON_32_httpwww_litle_comschemacardProductType', False)

    
    cardProductType = property(__cardProductType.value, __cardProductType.set, None, None)

    
    # Element {http://www.litle.com/schema}affluence uses Python identifier affluence
    __affluence = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'affluence'), 'affluence', '__httpwww_litle_comschema_CTD_ANON_32_httpwww_litle_comschemaaffluence', False)

    
    affluence = property(__affluence.value, __affluence.set, None, None)

    
    # Element {http://www.litle.com/schema}issuerCountry uses Python identifier issuerCountry
    __issuerCountry = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'issuerCountry'), 'issuerCountry', '__httpwww_litle_comschema_CTD_ANON_32_httpwww_litle_comschemaissuerCountry', False)

    
    issuerCountry = property(__issuerCountry.value, __issuerCountry.set, None, None)

    
    # Element {http://www.litle.com/schema}fundingSource uses Python identifier fundingSource
    __fundingSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fundingSource'), 'fundingSource', '__httpwww_litle_comschema_CTD_ANON_32_httpwww_litle_comschemafundingSource', False)

    
    fundingSource = property(__fundingSource.value, __fundingSource.set, None, None)


    _ElementMap = {
        __virtualAccountNumber.name() : __virtualAccountNumber,
        __cardProductType.name() : __cardProductType,
        __affluence.name() : __affluence,
        __issuerCountry.name() : __issuerCountry,
        __fundingSource.name() : __fundingSource
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_33_message', messageType, required=True)
    
    message = property(__message.value, __message.set, None, None)

    
    # Attribute response uses Python identifier response
    __response = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_33_response', responseType, required=True)
    
    response = property(__response.value, __response.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __message.name() : __message,
        __response.name() : __response
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}billToAddress uses Python identifier billToAddress
    __billToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), 'billToAddress', '__httpwww_litle_comschema_CTD_ANON_34_httpwww_litle_comschemabillToAddress', False)

    
    billToAddress = property(__billToAddress.value, __billToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantData uses Python identifier merchantData
    __merchantData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), 'merchantData', '__httpwww_litle_comschema_CTD_ANON_34_httpwww_litle_comschemamerchantData', False)

    
    merchantData = property(__merchantData.value, __merchantData.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_34_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}echeckOrEcheckToken uses Python identifier echeckOrEcheckToken
    __echeckOrEcheckToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken'), 'echeckOrEcheckToken', '__httpwww_litle_comschema_CTD_ANON_34_httpwww_litle_comschemaecheckOrEcheckToken', False)

    
    echeckOrEcheckToken = property(__echeckOrEcheckToken.value, __echeckOrEcheckToken.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_34_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_34_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_34_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __billToAddress.name() : __billToAddress,
        __merchantData.name() : __merchantData,
        __amount.name() : __amount,
        __echeckOrEcheckToken.name() : __echeckOrEcheckToken,
        __orderSource.name() : __orderSource,
        __litleTxnId.name() : __litleTxnId,
        __orderId.name() : __orderId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}transactionResponse uses Python identifier transactionResponse
    __transactionResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'transactionResponse'), 'transactionResponse', '__httpwww_litle_comschema_CTD_ANON_35_httpwww_litle_comschematransactionResponse', True)

    
    transactionResponse = property(__transactionResponse.value, __transactionResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}recurringTransactionResponse uses Python identifier recurringTransactionResponse
    __recurringTransactionResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recurringTransactionResponse'), 'recurringTransactionResponse', '__httpwww_litle_comschema_CTD_ANON_35_httpwww_litle_comschemarecurringTransactionResponse', True)

    
    recurringTransactionResponse = property(__recurringTransactionResponse.value, __recurringTransactionResponse.set, None, None)

    
    # Attribute litleBatchId uses Python identifier litleBatchId
    __litleBatchId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'litleBatchId'), 'litleBatchId', '__httpwww_litle_comschema_CTD_ANON_35_litleBatchId', litleIdType, required=True)
    
    litleBatchId = property(__litleBatchId.value, __litleBatchId.set, None, None)

    
    # Attribute merchantId uses Python identifier merchantId
    __merchantId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'merchantId'), 'merchantId', '__httpwww_litle_comschema_CTD_ANON_35_merchantId', merchantIdentificationType, required=True)
    
    merchantId = property(__merchantId.value, __merchantId.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_litle_comschema_CTD_ANON_35_id', string25Type)
    
    id = property(__id.value, __id.set, None, None)


    _ElementMap = {
        __transactionResponse.name() : __transactionResponse,
        __recurringTransactionResponse.name() : __recurringTransactionResponse
    }
    _AttributeMap = {
        __litleBatchId.name() : __litleBatchId,
        __merchantId.name() : __merchantId,
        __id.name() : __id
    }



# Complex type {http://www.litle.com/schema}echeckTokenType with content type ELEMENT_ONLY
class echeckTokenType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'echeckTokenType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}checkNum uses Python identifier checkNum
    __checkNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'checkNum'), 'checkNum', '__httpwww_litle_comschema_echeckTokenType_httpwww_litle_comschemacheckNum', False)

    
    checkNum = property(__checkNum.value, __checkNum.set, None, None)

    
    # Element {http://www.litle.com/schema}accType uses Python identifier accType
    __accType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accType'), 'accType', '__httpwww_litle_comschema_echeckTokenType_httpwww_litle_comschemaaccType', False)

    
    accType = property(__accType.value, __accType.set, None, None)

    
    # Element {http://www.litle.com/schema}litleToken uses Python identifier litleToken
    __litleToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), 'litleToken', '__httpwww_litle_comschema_echeckTokenType_httpwww_litle_comschemalitleToken', False)

    
    litleToken = property(__litleToken.value, __litleToken.set, None, None)

    
    # Element {http://www.litle.com/schema}routingNum uses Python identifier routingNum
    __routingNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'routingNum'), 'routingNum', '__httpwww_litle_comschema_echeckTokenType_httpwww_litle_comschemaroutingNum', False)

    
    routingNum = property(__routingNum.value, __routingNum.set, None, None)


    _ElementMap = {
        __checkNum.name() : __checkNum,
        __accType.name() : __accType,
        __litleToken.name() : __litleToken,
        __routingNum.name() : __routingNum
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'echeckTokenType', echeckTokenType)


# Complex type {http://www.litle.com/schema}recyclingRequestType with content type ELEMENT_ONLY
class recyclingRequestType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recyclingRequestType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}recycleId uses Python identifier recycleId
    __recycleId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recycleId'), 'recycleId', '__httpwww_litle_comschema_recyclingRequestType_httpwww_litle_comschemarecycleId', False)

    
    recycleId = property(__recycleId.value, __recycleId.set, None, None)

    
    # Element {http://www.litle.com/schema}recycleBy uses Python identifier recycleBy
    __recycleBy = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recycleBy'), 'recycleBy', '__httpwww_litle_comschema_recyclingRequestType_httpwww_litle_comschemarecycleBy', False)

    
    recycleBy = property(__recycleBy.value, __recycleBy.set, None, None)


    _ElementMap = {
        __recycleId.name() : __recycleId,
        __recycleBy.name() : __recycleBy
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'recyclingRequestType', recyclingRequestType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}residenceStatus uses Python identifier residenceStatus
    __residenceStatus = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'residenceStatus'), 'residenceStatus', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemaresidenceStatus', False)

    
    residenceStatus = property(__residenceStatus.value, __residenceStatus.set, None, None)

    
    # Element {http://www.litle.com/schema}customerType uses Python identifier customerType
    __customerType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerType'), 'customerType', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemacustomerType', False)

    
    customerType = property(__customerType.value, __customerType.set, None, None)

    
    # Element {http://www.litle.com/schema}customerCheckingAccount uses Python identifier customerCheckingAccount
    __customerCheckingAccount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerCheckingAccount'), 'customerCheckingAccount', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemacustomerCheckingAccount', False)

    
    customerCheckingAccount = property(__customerCheckingAccount.value, __customerCheckingAccount.set, None, None)

    
    # Element {http://www.litle.com/schema}customerSavingAccount uses Python identifier customerSavingAccount
    __customerSavingAccount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerSavingAccount'), 'customerSavingAccount', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemacustomerSavingAccount', False)

    
    customerSavingAccount = property(__customerSavingAccount.value, __customerSavingAccount.set, None, None)

    
    # Element {http://www.litle.com/schema}yearsAtResidence uses Python identifier yearsAtResidence
    __yearsAtResidence = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'yearsAtResidence'), 'yearsAtResidence', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemayearsAtResidence', False)

    
    yearsAtResidence = property(__yearsAtResidence.value, __yearsAtResidence.set, None, None)

    
    # Element {http://www.litle.com/schema}incomeCurrency uses Python identifier incomeCurrency
    __incomeCurrency = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'incomeCurrency'), 'incomeCurrency', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemaincomeCurrency', False)

    
    incomeCurrency = property(__incomeCurrency.value, __incomeCurrency.set, None, None)

    
    # Element {http://www.litle.com/schema}customerWorkTelephone uses Python identifier customerWorkTelephone
    __customerWorkTelephone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerWorkTelephone'), 'customerWorkTelephone', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemacustomerWorkTelephone', False)

    
    customerWorkTelephone = property(__customerWorkTelephone.value, __customerWorkTelephone.set, None, None)

    
    # Element {http://www.litle.com/schema}employerName uses Python identifier employerName
    __employerName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'employerName'), 'employerName', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemaemployerName', False)

    
    employerName = property(__employerName.value, __employerName.set, None, None)

    
    # Element {http://www.litle.com/schema}dob uses Python identifier dob
    __dob = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dob'), 'dob', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemadob', False)

    
    dob = property(__dob.value, __dob.set, None, None)

    
    # Element {http://www.litle.com/schema}ssn uses Python identifier ssn
    __ssn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ssn'), 'ssn', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemassn', False)

    
    ssn = property(__ssn.value, __ssn.set, None, None)

    
    # Element {http://www.litle.com/schema}yearsAtEmployer uses Python identifier yearsAtEmployer
    __yearsAtEmployer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'yearsAtEmployer'), 'yearsAtEmployer', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemayearsAtEmployer', False)

    
    yearsAtEmployer = property(__yearsAtEmployer.value, __yearsAtEmployer.set, None, None)

    
    # Element {http://www.litle.com/schema}customerRegistrationDate uses Python identifier customerRegistrationDate
    __customerRegistrationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerRegistrationDate'), 'customerRegistrationDate', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemacustomerRegistrationDate', False)

    
    customerRegistrationDate = property(__customerRegistrationDate.value, __customerRegistrationDate.set, None, None)

    
    # Element {http://www.litle.com/schema}incomeAmount uses Python identifier incomeAmount
    __incomeAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'incomeAmount'), 'incomeAmount', '__httpwww_litle_comschema_CTD_ANON_36_httpwww_litle_comschemaincomeAmount', False)

    
    incomeAmount = property(__incomeAmount.value, __incomeAmount.set, None, None)


    _ElementMap = {
        __residenceStatus.name() : __residenceStatus,
        __customerType.name() : __customerType,
        __customerCheckingAccount.name() : __customerCheckingAccount,
        __customerSavingAccount.name() : __customerSavingAccount,
        __yearsAtResidence.name() : __yearsAtResidence,
        __incomeCurrency.name() : __incomeCurrency,
        __customerWorkTelephone.name() : __customerWorkTelephone,
        __employerName.name() : __employerName,
        __dob.name() : __dob,
        __ssn.name() : __ssn,
        __yearsAtEmployer.name() : __yearsAtEmployer,
        __customerRegistrationDate.name() : __customerRegistrationDate,
        __incomeAmount.name() : __incomeAmount
    }
    _AttributeMap = {
        
    }



# Complex type {http://www.litle.com/schema}extendedCardResponseType with content type ELEMENT_ONLY
class extendedCardResponseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'extendedCardResponseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}code uses Python identifier code
    __code = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'code'), 'code', '__httpwww_litle_comschema_extendedCardResponseType_httpwww_litle_comschemacode', False)

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_extendedCardResponseType_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)


    _ElementMap = {
        __code.name() : __code,
        __message.name() : __message
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'extendedCardResponseType', extendedCardResponseType)


# Complex type {http://www.litle.com/schema}recurringRequestType with content type ELEMENT_ONLY
class recurringRequestType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recurringRequestType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}subscription uses Python identifier subscription
    __subscription = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subscription'), 'subscription', '__httpwww_litle_comschema_recurringRequestType_httpwww_litle_comschemasubscription', False)

    
    subscription = property(__subscription.value, __subscription.set, None, None)


    _ElementMap = {
        __subscription.name() : __subscription
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'recurringRequestType', recurringRequestType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}advancedFraudResults uses Python identifier advancedFraudResults
    __advancedFraudResults = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudResults'), 'advancedFraudResults', '__httpwww_litle_comschema_CTD_ANON_37_httpwww_litle_comschemaadvancedFraudResults', False)

    
    advancedFraudResults = property(__advancedFraudResults.value, __advancedFraudResults.set, None, None)

    
    # Element {http://www.litle.com/schema}cardValidationResult uses Python identifier cardValidationResult
    __cardValidationResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardValidationResult'), 'cardValidationResult', '__httpwww_litle_comschema_CTD_ANON_37_httpwww_litle_comschemacardValidationResult', False)

    
    cardValidationResult = property(__cardValidationResult.value, __cardValidationResult.set, None, None)

    
    # Element {http://www.litle.com/schema}avsResult uses Python identifier avsResult
    __avsResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'avsResult'), 'avsResult', '__httpwww_litle_comschema_CTD_ANON_37_httpwww_litle_comschemaavsResult', False)

    
    avsResult = property(__avsResult.value, __avsResult.set, None, None)

    
    # Element {http://www.litle.com/schema}authenticationResult uses Python identifier authenticationResult
    __authenticationResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authenticationResult'), 'authenticationResult', '__httpwww_litle_comschema_CTD_ANON_37_httpwww_litle_comschemaauthenticationResult', False)

    
    authenticationResult = property(__authenticationResult.value, __authenticationResult.set, None, None)

    
    # Element {http://www.litle.com/schema}advancedAVSResult uses Python identifier advancedAVSResult
    __advancedAVSResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'advancedAVSResult'), 'advancedAVSResult', '__httpwww_litle_comschema_CTD_ANON_37_httpwww_litle_comschemaadvancedAVSResult', False)

    
    advancedAVSResult = property(__advancedAVSResult.value, __advancedAVSResult.set, None, None)


    _ElementMap = {
        __advancedFraudResults.name() : __advancedFraudResults,
        __cardValidationResult.name() : __cardValidationResult,
        __avsResult.name() : __avsResult,
        __authenticationResult.name() : __authenticationResult,
        __advancedAVSResult.name() : __advancedAVSResult
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}sellerMerchantCategoryCode uses Python identifier sellerMerchantCategoryCode
    __sellerMerchantCategoryCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sellerMerchantCategoryCode'), 'sellerMerchantCategoryCode', '__httpwww_litle_comschema_CTD_ANON_38_httpwww_litle_comschemasellerMerchantCategoryCode', False)

    
    sellerMerchantCategoryCode = property(__sellerMerchantCategoryCode.value, __sellerMerchantCategoryCode.set, None, None)

    
    # Element {http://www.litle.com/schema}sellerId uses Python identifier sellerId
    __sellerId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sellerId'), 'sellerId', '__httpwww_litle_comschema_CTD_ANON_38_httpwww_litle_comschemasellerId', False)

    
    sellerId = property(__sellerId.value, __sellerId.set, None, None)


    _ElementMap = {
        __sellerMerchantCategoryCode.name() : __sellerMerchantCategoryCode,
        __sellerId.name() : __sellerId
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}eCheckAccountSuffix uses Python identifier eCheckAccountSuffix
    __eCheckAccountSuffix = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'eCheckAccountSuffix'), 'eCheckAccountSuffix', '__httpwww_litle_comschema_CTD_ANON_39_httpwww_litle_comschemaeCheckAccountSuffix', False)

    
    eCheckAccountSuffix = property(__eCheckAccountSuffix.value, __eCheckAccountSuffix.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_39_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_39_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}litleToken uses Python identifier litleToken
    __litleToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), 'litleToken', '__httpwww_litle_comschema_CTD_ANON_39_httpwww_litle_comschemalitleToken', False)

    
    litleToken = property(__litleToken.value, __litleToken.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_39_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}bin uses Python identifier bin
    __bin = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bin'), 'bin', '__httpwww_litle_comschema_CTD_ANON_39_httpwww_litle_comschemabin', False)

    
    bin = property(__bin.value, __bin.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_39_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}type uses Python identifier type
    __type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_litle_comschema_CTD_ANON_39_httpwww_litle_comschematype', False)

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_39_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __eCheckAccountSuffix.name() : __eCheckAccountSuffix,
        __litleTxnId.name() : __litleTxnId,
        __responseTime.name() : __responseTime,
        __litleToken.name() : __litleToken,
        __response.name() : __response,
        __bin.name() : __bin,
        __message.name() : __message,
        __type.name() : __type,
        __orderId.name() : __orderId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}advancedFraudChecksType with content type ELEMENT_ONLY
class advancedFraudChecksType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'advancedFraudChecksType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}threatMetrixSessionId uses Python identifier threatMetrixSessionId
    __threatMetrixSessionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'threatMetrixSessionId'), 'threatMetrixSessionId', '__httpwww_litle_comschema_advancedFraudChecksType_httpwww_litle_comschemathreatMetrixSessionId', False)

    
    threatMetrixSessionId = property(__threatMetrixSessionId.value, __threatMetrixSessionId.set, None, None)


    _ElementMap = {
        __threatMetrixSessionId.name() : __threatMetrixSessionId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'advancedFraudChecksType', advancedFraudChecksType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_40 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}merchantData uses Python identifier merchantData
    __merchantData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), 'merchantData', '__httpwww_litle_comschema_CTD_ANON_40_httpwww_litle_comschemamerchantData', False)

    
    merchantData = property(__merchantData.value, __merchantData.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_40_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}echeckOrEcheckToken uses Python identifier echeckOrEcheckToken
    __echeckOrEcheckToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken'), 'echeckOrEcheckToken', '__httpwww_litle_comschema_CTD_ANON_40_httpwww_litle_comschemaecheckOrEcheckToken', False)

    
    echeckOrEcheckToken = property(__echeckOrEcheckToken.value, __echeckOrEcheckToken.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __merchantData.name() : __merchantData,
        __litleTxnId.name() : __litleTxnId,
        __echeckOrEcheckToken.name() : __echeckOrEcheckToken
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}taxTypeIdentifier uses Python identifier taxTypeIdentifier
    __taxTypeIdentifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxTypeIdentifier'), 'taxTypeIdentifier', '__httpwww_litle_comschema_CTD_ANON_41_httpwww_litle_comschemataxTypeIdentifier', False)

    
    taxTypeIdentifier = property(__taxTypeIdentifier.value, __taxTypeIdentifier.set, None, None)

    
    # Element {http://www.litle.com/schema}taxAmount uses Python identifier taxAmount
    __taxAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxAmount'), 'taxAmount', '__httpwww_litle_comschema_CTD_ANON_41_httpwww_litle_comschemataxAmount', False)

    
    taxAmount = property(__taxAmount.value, __taxAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}taxIncludedInTotal uses Python identifier taxIncludedInTotal
    __taxIncludedInTotal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxIncludedInTotal'), 'taxIncludedInTotal', '__httpwww_litle_comschema_CTD_ANON_41_httpwww_litle_comschemataxIncludedInTotal', False)

    
    taxIncludedInTotal = property(__taxIncludedInTotal.value, __taxIncludedInTotal.set, None, None)

    
    # Element {http://www.litle.com/schema}taxRate uses Python identifier taxRate
    __taxRate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxRate'), 'taxRate', '__httpwww_litle_comschema_CTD_ANON_41_httpwww_litle_comschemataxRate', False)

    
    taxRate = property(__taxRate.value, __taxRate.set, None, None)

    
    # Element {http://www.litle.com/schema}cardAcceptorTaxId uses Python identifier cardAcceptorTaxId
    __cardAcceptorTaxId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardAcceptorTaxId'), 'cardAcceptorTaxId', '__httpwww_litle_comschema_CTD_ANON_41_httpwww_litle_comschemacardAcceptorTaxId', False)

    
    cardAcceptorTaxId = property(__cardAcceptorTaxId.value, __cardAcceptorTaxId.set, None, None)


    _ElementMap = {
        __taxTypeIdentifier.name() : __taxTypeIdentifier,
        __taxAmount.name() : __taxAmount,
        __taxIncludedInTotal.name() : __taxIncludedInTotal,
        __taxRate.name() : __taxRate,
        __cardAcceptorTaxId.name() : __cardAcceptorTaxId
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_42 (recurringTransactionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is recurringTransactionType
    
    # Element {http://www.litle.com/schema}billingDate uses Python identifier billingDate
    __billingDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billingDate'), 'billingDate', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemabillingDate', False)

    
    billingDate = property(__billingDate.value, __billingDate.set, None, None)

    
    # Element {http://www.litle.com/schema}billToAddress uses Python identifier billToAddress
    __billToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), 'billToAddress', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemabillToAddress', False)

    
    billToAddress = property(__billToAddress.value, __billToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}paypage uses Python identifier paypage
    __paypage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypage'), 'paypage', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemapaypage', False)

    
    paypage = property(__paypage.value, __paypage.set, None, None)

    
    # Element {http://www.litle.com/schema}updateAddOn uses Python identifier updateAddOn
    __updateAddOn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'updateAddOn'), 'updateAddOn', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemaupdateAddOn', True)

    
    updateAddOn = property(__updateAddOn.value, __updateAddOn.set, None, None)

    
    # Element {http://www.litle.com/schema}token uses Python identifier token
    __token = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'token'), 'token', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschematoken', False)

    
    token = property(__token.value, __token.set, None, None)

    
    # Element {http://www.litle.com/schema}createDiscount uses Python identifier createDiscount
    __createDiscount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'createDiscount'), 'createDiscount', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemacreateDiscount', True)

    
    createDiscount = property(__createDiscount.value, __createDiscount.set, None, None)

    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Element {http://www.litle.com/schema}subscriptionId uses Python identifier subscriptionId
    __subscriptionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), 'subscriptionId', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemasubscriptionId', False)

    
    subscriptionId = property(__subscriptionId.value, __subscriptionId.set, None, None)

    
    # Element {http://www.litle.com/schema}updateDiscount uses Python identifier updateDiscount
    __updateDiscount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'updateDiscount'), 'updateDiscount', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemaupdateDiscount', True)

    
    updateDiscount = property(__updateDiscount.value, __updateDiscount.set, None, None)

    
    # Element {http://www.litle.com/schema}planCode uses Python identifier planCode
    __planCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'planCode'), 'planCode', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemaplanCode', False)

    
    planCode = property(__planCode.value, __planCode.set, None, None)

    
    # Element {http://www.litle.com/schema}deleteAddOn uses Python identifier deleteAddOn
    __deleteAddOn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'deleteAddOn'), 'deleteAddOn', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemadeleteAddOn', True)

    
    deleteAddOn = property(__deleteAddOn.value, __deleteAddOn.set, None, None)

    
    # Element {http://www.litle.com/schema}deleteDiscount uses Python identifier deleteDiscount
    __deleteDiscount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'deleteDiscount'), 'deleteDiscount', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemadeleteDiscount', True)

    
    deleteDiscount = property(__deleteDiscount.value, __deleteDiscount.set, None, None)

    
    # Element {http://www.litle.com/schema}createAddOn uses Python identifier createAddOn
    __createAddOn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'createAddOn'), 'createAddOn', '__httpwww_litle_comschema_CTD_ANON_42_httpwww_litle_comschemacreateAddOn', True)

    
    createAddOn = property(__createAddOn.value, __createAddOn.set, None, None)


    _ElementMap = recurringTransactionType._ElementMap.copy()
    _ElementMap.update({
        __billingDate.name() : __billingDate,
        __billToAddress.name() : __billToAddress,
        __paypage.name() : __paypage,
        __updateAddOn.name() : __updateAddOn,
        __token.name() : __token,
        __createDiscount.name() : __createDiscount,
        __card.name() : __card,
        __subscriptionId.name() : __subscriptionId,
        __updateDiscount.name() : __updateDiscount,
        __planCode.name() : __planCode,
        __deleteAddOn.name() : __deleteAddOn,
        __deleteDiscount.name() : __deleteDiscount,
        __createAddOn.name() : __createAddOn
    })
    _AttributeMap = recurringTransactionType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_43 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}echeckOrEcheckToken uses Python identifier echeckOrEcheckToken
    __echeckOrEcheckToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken'), 'echeckOrEcheckToken', '__httpwww_litle_comschema_CTD_ANON_43_httpwww_litle_comschemaecheckOrEcheckToken', False)

    
    echeckOrEcheckToken = property(__echeckOrEcheckToken.value, __echeckOrEcheckToken.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_43_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_43_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Element {http://www.litle.com/schema}customBilling uses Python identifier customBilling
    __customBilling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), 'customBilling', '__httpwww_litle_comschema_CTD_ANON_43_httpwww_litle_comschemacustomBilling', False)

    
    customBilling = property(__customBilling.value, __customBilling.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantData uses Python identifier merchantData
    __merchantData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), 'merchantData', '__httpwww_litle_comschema_CTD_ANON_43_httpwww_litle_comschemamerchantData', False)

    
    merchantData = property(__merchantData.value, __merchantData.set, None, None)

    
    # Element {http://www.litle.com/schema}billToAddress uses Python identifier billToAddress
    __billToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), 'billToAddress', '__httpwww_litle_comschema_CTD_ANON_43_httpwww_litle_comschemabillToAddress', False)

    
    billToAddress = property(__billToAddress.value, __billToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_43_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_43_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __echeckOrEcheckToken.name() : __echeckOrEcheckToken,
        __amount.name() : __amount,
        __orderSource.name() : __orderSource,
        __customBilling.name() : __customBilling,
        __merchantData.name() : __merchantData,
        __billToAddress.name() : __billToAddress,
        __orderId.name() : __orderId,
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_44 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_44_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponse uses Python identifier tokenResponse
    __tokenResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), 'tokenResponse', '__httpwww_litle_comschema_CTD_ANON_44_httpwww_litle_comschematokenResponse', False)

    
    tokenResponse = property(__tokenResponse.value, __tokenResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_44_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_44_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_44_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_44_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}accountUpdater uses Python identifier accountUpdater
    __accountUpdater = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), 'accountUpdater', '__httpwww_litle_comschema_CTD_ANON_44_httpwww_litle_comschemaaccountUpdater', False)

    
    accountUpdater = property(__accountUpdater.value, __accountUpdater.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __response.name() : __response,
        __tokenResponse.name() : __tokenResponse,
        __responseTime.name() : __responseTime,
        __message.name() : __message,
        __litleTxnId.name() : __litleTxnId,
        __postDate.name() : __postDate,
        __accountUpdater.name() : __accountUpdater
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_45 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}bmlMerchantId uses Python identifier bmlMerchantId
    __bmlMerchantId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bmlMerchantId'), 'bmlMerchantId', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemabmlMerchantId', False)

    
    bmlMerchantId = property(__bmlMerchantId.value, __bmlMerchantId.set, None, None)

    
    # Element {http://www.litle.com/schema}customerPhoneChanged uses Python identifier customerPhoneChanged
    __customerPhoneChanged = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerPhoneChanged'), 'customerPhoneChanged', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemacustomerPhoneChanged', False)

    
    customerPhoneChanged = property(__customerPhoneChanged.value, __customerPhoneChanged.set, None, None)

    
    # Element {http://www.litle.com/schema}customerPasswordChanged uses Python identifier customerPasswordChanged
    __customerPasswordChanged = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerPasswordChanged'), 'customerPasswordChanged', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemacustomerPasswordChanged', False)

    
    customerPasswordChanged = property(__customerPasswordChanged.value, __customerPasswordChanged.set, None, None)

    
    # Element {http://www.litle.com/schema}secretQuestionCode uses Python identifier secretQuestionCode
    __secretQuestionCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'secretQuestionCode'), 'secretQuestionCode', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemasecretQuestionCode', False)

    
    secretQuestionCode = property(__secretQuestionCode.value, __secretQuestionCode.set, None, None)

    
    # Element {http://www.litle.com/schema}virtualAuthenticationKeyPresenceIndicator uses Python identifier virtualAuthenticationKeyPresenceIndicator
    __virtualAuthenticationKeyPresenceIndicator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualAuthenticationKeyPresenceIndicator'), 'virtualAuthenticationKeyPresenceIndicator', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemavirtualAuthenticationKeyPresenceIndicator', False)

    
    virtualAuthenticationKeyPresenceIndicator = property(__virtualAuthenticationKeyPresenceIndicator.value, __virtualAuthenticationKeyPresenceIndicator.set, None, None)

    
    # Element {http://www.litle.com/schema}customerBillingAddressChanged uses Python identifier customerBillingAddressChanged
    __customerBillingAddressChanged = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerBillingAddressChanged'), 'customerBillingAddressChanged', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemacustomerBillingAddressChanged', False)

    
    customerBillingAddressChanged = property(__customerBillingAddressChanged.value, __customerBillingAddressChanged.set, None, None)

    
    # Element {http://www.litle.com/schema}customerEmailChanged uses Python identifier customerEmailChanged
    __customerEmailChanged = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerEmailChanged'), 'customerEmailChanged', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemacustomerEmailChanged', False)

    
    customerEmailChanged = property(__customerEmailChanged.value, __customerEmailChanged.set, None, None)

    
    # Element {http://www.litle.com/schema}preapprovalNumber uses Python identifier preapprovalNumber
    __preapprovalNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'preapprovalNumber'), 'preapprovalNumber', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemapreapprovalNumber', False)

    
    preapprovalNumber = property(__preapprovalNumber.value, __preapprovalNumber.set, None, None)

    
    # Element {http://www.litle.com/schema}termsAndConditions uses Python identifier termsAndConditions
    __termsAndConditions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'termsAndConditions'), 'termsAndConditions', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschematermsAndConditions', False)

    
    termsAndConditions = property(__termsAndConditions.value, __termsAndConditions.set, None, None)

    
    # Element {http://www.litle.com/schema}itemCategoryCode uses Python identifier itemCategoryCode
    __itemCategoryCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'itemCategoryCode'), 'itemCategoryCode', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemaitemCategoryCode', False)

    
    itemCategoryCode = property(__itemCategoryCode.value, __itemCategoryCode.set, None, None)

    
    # Element {http://www.litle.com/schema}authorizationSourcePlatform uses Python identifier authorizationSourcePlatform
    __authorizationSourcePlatform = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authorizationSourcePlatform'), 'authorizationSourcePlatform', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemaauthorizationSourcePlatform', False)

    
    authorizationSourcePlatform = property(__authorizationSourcePlatform.value, __authorizationSourcePlatform.set, None, None)

    
    # Element {http://www.litle.com/schema}secretQuestionAnswer uses Python identifier secretQuestionAnswer
    __secretQuestionAnswer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'secretQuestionAnswer'), 'secretQuestionAnswer', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemasecretQuestionAnswer', False)

    
    secretQuestionAnswer = property(__secretQuestionAnswer.value, __secretQuestionAnswer.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantPromotionalCode uses Python identifier merchantPromotionalCode
    __merchantPromotionalCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantPromotionalCode'), 'merchantPromotionalCode', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemamerchantPromotionalCode', False)

    
    merchantPromotionalCode = property(__merchantPromotionalCode.value, __merchantPromotionalCode.set, None, None)

    
    # Element {http://www.litle.com/schema}bmlProductType uses Python identifier bmlProductType
    __bmlProductType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bmlProductType'), 'bmlProductType', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemabmlProductType', False)

    
    bmlProductType = property(__bmlProductType.value, __bmlProductType.set, None, None)

    
    # Element {http://www.litle.com/schema}virtualAuthenticationKeyData uses Python identifier virtualAuthenticationKeyData
    __virtualAuthenticationKeyData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualAuthenticationKeyData'), 'virtualAuthenticationKeyData', '__httpwww_litle_comschema_CTD_ANON_45_httpwww_litle_comschemavirtualAuthenticationKeyData', False)

    
    virtualAuthenticationKeyData = property(__virtualAuthenticationKeyData.value, __virtualAuthenticationKeyData.set, None, None)


    _ElementMap = {
        __bmlMerchantId.name() : __bmlMerchantId,
        __customerPhoneChanged.name() : __customerPhoneChanged,
        __customerPasswordChanged.name() : __customerPasswordChanged,
        __secretQuestionCode.name() : __secretQuestionCode,
        __virtualAuthenticationKeyPresenceIndicator.name() : __virtualAuthenticationKeyPresenceIndicator,
        __customerBillingAddressChanged.name() : __customerBillingAddressChanged,
        __customerEmailChanged.name() : __customerEmailChanged,
        __preapprovalNumber.name() : __preapprovalNumber,
        __termsAndConditions.name() : __termsAndConditions,
        __itemCategoryCode.name() : __itemCategoryCode,
        __authorizationSourcePlatform.name() : __authorizationSourcePlatform,
        __secretQuestionAnswer.name() : __secretQuestionAnswer,
        __merchantPromotionalCode.name() : __merchantPromotionalCode,
        __bmlProductType.name() : __bmlProductType,
        __virtualAuthenticationKeyData.name() : __virtualAuthenticationKeyData
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_46 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}cardValidationNum uses Python identifier cardValidationNum
    __cardValidationNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), 'cardValidationNum', '__httpwww_litle_comschema_CTD_ANON_46_httpwww_litle_comschemacardValidationNum', False)

    
    cardValidationNum = property(__cardValidationNum.value, __cardValidationNum.set, None, None)

    
    # Element {http://www.litle.com/schema}accountNumber uses Python identifier accountNumber
    __accountNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountNumber'), 'accountNumber', '__httpwww_litle_comschema_CTD_ANON_46_httpwww_litle_comschemaaccountNumber', False)

    
    accountNumber = property(__accountNumber.value, __accountNumber.set, None, None)


    _ElementMap = {
        __cardValidationNum.name() : __cardValidationNum,
        __accountNumber.name() : __accountNumber
    }
    _AttributeMap = {
        
    }



# Complex type {http://www.litle.com/schema}echeckAccountInfoType with content type ELEMENT_ONLY
class echeckAccountInfoType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'echeckAccountInfoType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}routingNum uses Python identifier routingNum
    __routingNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'routingNum'), 'routingNum', '__httpwww_litle_comschema_echeckAccountInfoType_httpwww_litle_comschemaroutingNum', False)

    
    routingNum = property(__routingNum.value, __routingNum.set, None, None)

    
    # Element {http://www.litle.com/schema}accNum uses Python identifier accNum
    __accNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accNum'), 'accNum', '__httpwww_litle_comschema_echeckAccountInfoType_httpwww_litle_comschemaaccNum', False)

    
    accNum = property(__accNum.value, __accNum.set, None, None)

    
    # Element {http://www.litle.com/schema}accType uses Python identifier accType
    __accType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accType'), 'accType', '__httpwww_litle_comschema_echeckAccountInfoType_httpwww_litle_comschemaaccType', False)

    
    accType = property(__accType.value, __accType.set, None, None)


    _ElementMap = {
        __routingNum.name() : __routingNum,
        __accNum.name() : __accNum,
        __accType.name() : __accType
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'echeckAccountInfoType', echeckAccountInfoType)


# Complex type {http://www.litle.com/schema}cardPaypageType with content type ELEMENT_ONLY
class cardPaypageType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cardPaypageType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}paypageRegistrationId uses Python identifier paypageRegistrationId
    __paypageRegistrationId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypageRegistrationId'), 'paypageRegistrationId', '__httpwww_litle_comschema_cardPaypageType_httpwww_litle_comschemapaypageRegistrationId', False)

    
    paypageRegistrationId = property(__paypageRegistrationId.value, __paypageRegistrationId.set, None, None)

    
    # Element {http://www.litle.com/schema}type uses Python identifier type
    __type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_litle_comschema_cardPaypageType_httpwww_litle_comschematype', False)

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://www.litle.com/schema}expDate uses Python identifier expDate
    __expDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'expDate'), 'expDate', '__httpwww_litle_comschema_cardPaypageType_httpwww_litle_comschemaexpDate', False)

    
    expDate = property(__expDate.value, __expDate.set, None, None)

    
    # Element {http://www.litle.com/schema}cardValidationNum uses Python identifier cardValidationNum
    __cardValidationNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), 'cardValidationNum', '__httpwww_litle_comschema_cardPaypageType_httpwww_litle_comschemacardValidationNum', False)

    
    cardValidationNum = property(__cardValidationNum.value, __cardValidationNum.set, None, None)


    _ElementMap = {
        __paypageRegistrationId.name() : __paypageRegistrationId,
        __type.name() : __type,
        __expDate.name() : __expDate,
        __cardValidationNum.name() : __cardValidationNum
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cardPaypageType', cardPaypageType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_47 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}payerId uses Python identifier payerId
    __payerId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'payerId'), 'payerId', '__httpwww_litle_comschema_CTD_ANON_47_httpwww_litle_comschemapayerId', False)

    
    payerId = property(__payerId.value, __payerId.set, None, None)

    
    # Element {http://www.litle.com/schema}payerEmail uses Python identifier payerEmail
    __payerEmail = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'payerEmail'), 'payerEmail', '__httpwww_litle_comschema_CTD_ANON_47_httpwww_litle_comschemapayerEmail', False)

    
    payerEmail = property(__payerEmail.value, __payerEmail.set, None, None)


    _ElementMap = {
        __payerId.name() : __payerId,
        __payerEmail.name() : __payerEmail
    }
    _AttributeMap = {
        
    }



# Complex type {http://www.litle.com/schema}merchantDataType with content type ELEMENT_ONLY
class merchantDataType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'merchantDataType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}merchantGroupingId uses Python identifier merchantGroupingId
    __merchantGroupingId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantGroupingId'), 'merchantGroupingId', '__httpwww_litle_comschema_merchantDataType_httpwww_litle_comschemamerchantGroupingId', False)

    
    merchantGroupingId = property(__merchantGroupingId.value, __merchantGroupingId.set, None, None)

    
    # Element {http://www.litle.com/schema}affiliate uses Python identifier affiliate
    __affiliate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'affiliate'), 'affiliate', '__httpwww_litle_comschema_merchantDataType_httpwww_litle_comschemaaffiliate', False)

    
    affiliate = property(__affiliate.value, __affiliate.set, None, None)

    
    # Element {http://www.litle.com/schema}campaign uses Python identifier campaign
    __campaign = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'campaign'), 'campaign', '__httpwww_litle_comschema_merchantDataType_httpwww_litle_comschemacampaign', False)

    
    campaign = property(__campaign.value, __campaign.set, None, None)


    _ElementMap = {
        __merchantGroupingId.name() : __merchantGroupingId,
        __affiliate.name() : __affiliate,
        __campaign.name() : __campaign
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'merchantDataType', merchantDataType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_48 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_48_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_48_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_48_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_48_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_48_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_48_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_48_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __postDate.name() : __postDate,
        __litleTxnId.name() : __litleTxnId,
        __giftCardResponse.name() : __giftCardResponse,
        __orderId.name() : __orderId,
        __response.name() : __response,
        __message.name() : __message,
        __responseTime.name() : __responseTime
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_49 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_49_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_49_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_49_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}accountUpdater uses Python identifier accountUpdater
    __accountUpdater = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), 'accountUpdater', '__httpwww_litle_comschema_CTD_ANON_49_httpwww_litle_comschemaaccountUpdater', False)

    
    accountUpdater = property(__accountUpdater.value, __accountUpdater.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_49_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_49_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_49_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_49_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_49_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httpwww_litle_comschema_CTD_ANON_49_duplicate', pyxb.binding.datatypes.boolean)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __responseTime.name() : __responseTime,
        __litleTxnId.name() : __litleTxnId,
        __giftCardResponse.name() : __giftCardResponse,
        __accountUpdater.name() : __accountUpdater,
        __postDate.name() : __postDate,
        __message.name() : __message,
        __fraudResult.name() : __fraudResult,
        __response.name() : __response,
        __orderId.name() : __orderId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_50 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}prepaidCardType uses Python identifier prepaidCardType
    __prepaidCardType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'prepaidCardType'), 'prepaidCardType', '__httpwww_litle_comschema_CTD_ANON_50_httpwww_litle_comschemaprepaidCardType', False)

    
    prepaidCardType = property(__prepaidCardType.value, __prepaidCardType.set, None, None)

    
    # Element {http://www.litle.com/schema}type uses Python identifier type
    __type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_litle_comschema_CTD_ANON_50_httpwww_litle_comschematype', False)

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://www.litle.com/schema}availableBalance uses Python identifier availableBalance
    __availableBalance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'availableBalance'), 'availableBalance', '__httpwww_litle_comschema_CTD_ANON_50_httpwww_litle_comschemaavailableBalance', False)

    
    availableBalance = property(__availableBalance.value, __availableBalance.set, None, None)

    
    # Element {http://www.litle.com/schema}reloadable uses Python identifier reloadable
    __reloadable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'reloadable'), 'reloadable', '__httpwww_litle_comschema_CTD_ANON_50_httpwww_litle_comschemareloadable', False)

    
    reloadable = property(__reloadable.value, __reloadable.set, None, None)


    _ElementMap = {
        __prepaidCardType.name() : __prepaidCardType,
        __type.name() : __type,
        __availableBalance.name() : __availableBalance,
        __reloadable.name() : __reloadable
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_51 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_51_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}processingInstructions uses Python identifier processingInstructions
    __processingInstructions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), 'processingInstructions', '__httpwww_litle_comschema_CTD_ANON_51_httpwww_litle_comschemaprocessingInstructions', False)

    
    processingInstructions = property(__processingInstructions.value, __processingInstructions.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId,
        __processingInstructions.name() : __processingInstructions
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_52 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_52_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_52_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_52_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_52_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_52_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_52_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_52_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_52_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __orderId.name() : __orderId,
        __fraudResult.name() : __fraudResult,
        __message.name() : __message,
        __response.name() : __response,
        __giftCardResponse.name() : __giftCardResponse,
        __litleTxnId.name() : __litleTxnId,
        __postDate.name() : __postDate,
        __responseTime.name() : __responseTime
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}filteringType with content type ELEMENT_ONLY
class filteringType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'filteringType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}chargeback uses Python identifier chargeback
    __chargeback = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'chargeback'), 'chargeback', '__httpwww_litle_comschema_filteringType_httpwww_litle_comschemachargeback', False)

    
    chargeback = property(__chargeback.value, __chargeback.set, None, None)

    
    # Element {http://www.litle.com/schema}prepaid uses Python identifier prepaid
    __prepaid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'prepaid'), 'prepaid', '__httpwww_litle_comschema_filteringType_httpwww_litle_comschemaprepaid', False)

    
    prepaid = property(__prepaid.value, __prepaid.set, None, None)

    
    # Element {http://www.litle.com/schema}international uses Python identifier international
    __international = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'international'), 'international', '__httpwww_litle_comschema_filteringType_httpwww_litle_comschemainternational', False)

    
    international = property(__international.value, __international.set, None, None)


    _ElementMap = {
        __chargeback.name() : __chargeback,
        __prepaid.name() : __prepaid,
        __international.name() : __international
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'filteringType', filteringType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_53 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_53_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_53_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}recycling uses Python identifier recycling
    __recycling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recycling'), 'recycling', '__httpwww_litle_comschema_CTD_ANON_53_httpwww_litle_comschemarecycling', False)

    
    recycling = property(__recycling.value, __recycling.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_53_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_53_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_53_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httpwww_litle_comschema_CTD_ANON_53_duplicate', pyxb.binding.datatypes.boolean)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __responseTime.name() : __responseTime,
        __postDate.name() : __postDate,
        __recycling.name() : __recycling,
        __litleTxnId.name() : __litleTxnId,
        __response.name() : __response,
        __message.name() : __message
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })



# Complex type {http://www.litle.com/schema}cardAccountInfoType with content type ELEMENT_ONLY
class cardAccountInfoType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cardAccountInfoType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}expDate uses Python identifier expDate
    __expDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'expDate'), 'expDate', '__httpwww_litle_comschema_cardAccountInfoType_httpwww_litle_comschemaexpDate', False)

    
    expDate = property(__expDate.value, __expDate.set, None, None)

    
    # Element {http://www.litle.com/schema}number uses Python identifier number
    __number = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'number'), 'number', '__httpwww_litle_comschema_cardAccountInfoType_httpwww_litle_comschemanumber', False)

    
    number = property(__number.value, __number.set, None, None)

    
    # Element {http://www.litle.com/schema}type uses Python identifier type
    __type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_litle_comschema_cardAccountInfoType_httpwww_litle_comschematype', False)

    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        __expDate.name() : __expDate,
        __number.name() : __number,
        __type.name() : __type
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cardAccountInfoType', cardAccountInfoType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_54 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_54_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}cardTokenInfoType with content type ELEMENT_ONLY
class cardTokenInfoType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cardTokenInfoType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}expDate uses Python identifier expDate
    __expDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'expDate'), 'expDate', '__httpwww_litle_comschema_cardTokenInfoType_httpwww_litle_comschemaexpDate', False)

    
    expDate = property(__expDate.value, __expDate.set, None, None)

    
    # Element {http://www.litle.com/schema}type uses Python identifier type
    __type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_litle_comschema_cardTokenInfoType_httpwww_litle_comschematype', False)

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://www.litle.com/schema}bin uses Python identifier bin
    __bin = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bin'), 'bin', '__httpwww_litle_comschema_cardTokenInfoType_httpwww_litle_comschemabin', False)

    
    bin = property(__bin.value, __bin.set, None, None)

    
    # Element {http://www.litle.com/schema}litleToken uses Python identifier litleToken
    __litleToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), 'litleToken', '__httpwww_litle_comschema_cardTokenInfoType_httpwww_litle_comschemalitleToken', False)

    
    litleToken = property(__litleToken.value, __litleToken.set, None, None)


    _ElementMap = {
        __expDate.name() : __expDate,
        __type.name() : __type,
        __bin.name() : __bin,
        __litleToken.name() : __litleToken
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'cardTokenInfoType', cardTokenInfoType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_55 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_55_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_55_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_55_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponse uses Python identifier tokenResponse
    __tokenResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), 'tokenResponse', '__httpwww_litle_comschema_CTD_ANON_55_httpwww_litle_comschematokenResponse', False)

    
    tokenResponse = property(__tokenResponse.value, __tokenResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_55_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_55_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_55_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_55_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_55_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __fraudResult.name() : __fraudResult,
        __responseTime.name() : __responseTime,
        __giftCardResponse.name() : __giftCardResponse,
        __tokenResponse.name() : __tokenResponse,
        __postDate.name() : __postDate,
        __litleTxnId.name() : __litleTxnId,
        __message.name() : __message,
        __response.name() : __response,
        __orderId.name() : __orderId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_56 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}transactionResponse uses Python identifier transactionResponse
    __transactionResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'transactionResponse'), 'transactionResponse', '__httpwww_litle_comschema_CTD_ANON_56_httpwww_litle_comschematransactionResponse', False)

    
    transactionResponse = property(__transactionResponse.value, __transactionResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}recurringTransactionResponse uses Python identifier recurringTransactionResponse
    __recurringTransactionResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recurringTransactionResponse'), 'recurringTransactionResponse', '__httpwww_litle_comschema_CTD_ANON_56_httpwww_litle_comschemarecurringTransactionResponse', False)

    
    recurringTransactionResponse = property(__recurringTransactionResponse.value, __recurringTransactionResponse.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_litle_comschema_CTD_ANON_56_version', versionType, required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_56_message', messageType, required=True)
    
    message = property(__message.value, __message.set, None, None)

    
    # Attribute response uses Python identifier response
    __response = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_56_response', responseType, required=True)
    
    response = property(__response.value, __response.set, None, None)


    _ElementMap = {
        __transactionResponse.name() : __transactionResponse,
        __recurringTransactionResponse.name() : __recurringTransactionResponse
    }
    _AttributeMap = {
        __version.name() : __version,
        __message.name() : __message,
        __response.name() : __response
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_57 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}merchantData uses Python identifier merchantData
    __merchantData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), 'merchantData', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemamerchantData', False)

    
    merchantData = property(__merchantData.value, __merchantData.set, None, None)

    
    # Element {http://www.litle.com/schema}amexAggregatorData uses Python identifier amexAggregatorData
    __amexAggregatorData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), 'amexAggregatorData', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemaamexAggregatorData', False)

    
    amexAggregatorData = property(__amexAggregatorData.value, __amexAggregatorData.set, None, None)

    
    # Element {http://www.litle.com/schema}recyclingRequest uses Python identifier recyclingRequest
    __recyclingRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recyclingRequest'), 'recyclingRequest', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemarecyclingRequest', False)

    
    recyclingRequest = property(__recyclingRequest.value, __recyclingRequest.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudFilterOverride uses Python identifier fraudFilterOverride
    __fraudFilterOverride = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudFilterOverride'), 'fraudFilterOverride', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemafraudFilterOverride', False)

    
    fraudFilterOverride = property(__fraudFilterOverride.value, __fraudFilterOverride.set, None, None)

    
    # Element {http://www.litle.com/schema}healthcareIIAS uses Python identifier healthcareIIAS
    __healthcareIIAS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'healthcareIIAS'), 'healthcareIIAS', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemahealthcareIIAS', False)

    
    healthcareIIAS = property(__healthcareIIAS.value, __healthcareIIAS.set, None, None)

    
    # Element {http://www.litle.com/schema}billToAddress uses Python identifier billToAddress
    __billToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), 'billToAddress', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemabillToAddress', False)

    
    billToAddress = property(__billToAddress.value, __billToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}recurringRequest uses Python identifier recurringRequest
    __recurringRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recurringRequest'), 'recurringRequest', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemarecurringRequest', False)

    
    recurringRequest = property(__recurringRequest.value, __recurringRequest.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Element {http://www.litle.com/schema}enhancedData uses Python identifier enhancedData
    __enhancedData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), 'enhancedData', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemaenhancedData', False)

    
    enhancedData = property(__enhancedData.value, __enhancedData.set, None, None)

    
    # Element {http://www.litle.com/schema}debtRepayment uses Python identifier debtRepayment
    __debtRepayment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment'), 'debtRepayment', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemadebtRepayment', False)

    
    debtRepayment = property(__debtRepayment.value, __debtRepayment.set, None, None)

    
    # Element {http://www.litle.com/schema}allowPartialAuth uses Python identifier allowPartialAuth
    __allowPartialAuth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'allowPartialAuth'), 'allowPartialAuth', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemaallowPartialAuth', False)

    
    allowPartialAuth = property(__allowPartialAuth.value, __allowPartialAuth.set, None, None)

    
    # Element {http://www.litle.com/schema}billMeLaterRequest uses Python identifier billMeLaterRequest
    __billMeLaterRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest'), 'billMeLaterRequest', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemabillMeLaterRequest', False)

    
    billMeLaterRequest = property(__billMeLaterRequest.value, __billMeLaterRequest.set, None, None)

    
    # Element {http://www.litle.com/schema}advancedFraudChecks uses Python identifier advancedFraudChecks
    __advancedFraudChecks = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudChecks'), 'advancedFraudChecks', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemaadvancedFraudChecks', False)

    
    advancedFraudChecks = property(__advancedFraudChecks.value, __advancedFraudChecks.set, None, None)

    
    # Element {http://www.litle.com/schema}customerInfo uses Python identifier customerInfo
    __customerInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerInfo'), 'customerInfo', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemacustomerInfo', False)

    
    customerInfo = property(__customerInfo.value, __customerInfo.set, None, None)

    
    # Element {http://www.litle.com/schema}customBilling uses Python identifier customBilling
    __customBilling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), 'customBilling', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemacustomBilling', False)

    
    customBilling = property(__customBilling.value, __customBilling.set, None, None)

    
    # Element {http://www.litle.com/schema}token uses Python identifier token
    __token = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'token'), 'token', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschematoken', False)

    
    token = property(__token.value, __token.set, None, None)

    
    # Element {http://www.litle.com/schema}paypage uses Python identifier paypage
    __paypage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypage'), 'paypage', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemapaypage', False)

    
    paypage = property(__paypage.value, __paypage.set, None, None)

    
    # Element {http://www.litle.com/schema}mpos uses Python identifier mpos
    __mpos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'mpos'), 'mpos', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemampos', False)

    
    mpos = property(__mpos.value, __mpos.set, None, None)

    
    # Element {http://www.litle.com/schema}processingInstructions uses Python identifier processingInstructions
    __processingInstructions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), 'processingInstructions', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemaprocessingInstructions', False)

    
    processingInstructions = property(__processingInstructions.value, __processingInstructions.set, None, None)

    
    # Element {http://www.litle.com/schema}cardholderAuthentication uses Python identifier cardholderAuthentication
    __cardholderAuthentication = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardholderAuthentication'), 'cardholderAuthentication', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemacardholderAuthentication', False)

    
    cardholderAuthentication = property(__cardholderAuthentication.value, __cardholderAuthentication.set, None, None)

    
    # Element {http://www.litle.com/schema}shipToAddress uses Python identifier shipToAddress
    __shipToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress'), 'shipToAddress', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemashipToAddress', False)

    
    shipToAddress = property(__shipToAddress.value, __shipToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}paypal uses Python identifier paypal
    __paypal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypal'), 'paypal', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemapaypal', False)

    
    paypal = property(__paypal.value, __paypal.set, None, None)

    
    # Element {http://www.litle.com/schema}taxType uses Python identifier taxType
    __taxType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxType'), 'taxType', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemataxType', False)

    
    taxType = property(__taxType.value, __taxType.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Element {http://www.litle.com/schema}surchargeAmount uses Python identifier surchargeAmount
    __surchargeAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), 'surchargeAmount', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemasurchargeAmount', False)

    
    surchargeAmount = property(__surchargeAmount.value, __surchargeAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pos'), 'pos', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemapos', False)

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.litle.com/schema}filtering uses Python identifier filtering
    __filtering = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'filtering'), 'filtering', '__httpwww_litle_comschema_CTD_ANON_57_httpwww_litle_comschemafiltering', False)

    
    filtering = property(__filtering.value, __filtering.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __merchantData.name() : __merchantData,
        __amexAggregatorData.name() : __amexAggregatorData,
        __recyclingRequest.name() : __recyclingRequest,
        __fraudFilterOverride.name() : __fraudFilterOverride,
        __healthcareIIAS.name() : __healthcareIIAS,
        __billToAddress.name() : __billToAddress,
        __recurringRequest.name() : __recurringRequest,
        __orderSource.name() : __orderSource,
        __enhancedData.name() : __enhancedData,
        __debtRepayment.name() : __debtRepayment,
        __allowPartialAuth.name() : __allowPartialAuth,
        __billMeLaterRequest.name() : __billMeLaterRequest,
        __advancedFraudChecks.name() : __advancedFraudChecks,
        __customerInfo.name() : __customerInfo,
        __customBilling.name() : __customBilling,
        __token.name() : __token,
        __paypage.name() : __paypage,
        __mpos.name() : __mpos,
        __processingInstructions.name() : __processingInstructions,
        __cardholderAuthentication.name() : __cardholderAuthentication,
        __shipToAddress.name() : __shipToAddress,
        __litleTxnId.name() : __litleTxnId,
        __paypal.name() : __paypal,
        __taxType.name() : __taxType,
        __orderId.name() : __orderId,
        __amount.name() : __amount,
        __card.name() : __card,
        __surchargeAmount.name() : __surchargeAmount,
        __pos.name() : __pos,
        __filtering.name() : __filtering
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}createDiscountType with content type ELEMENT_ONLY
class createDiscountType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'createDiscountType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}discountCode uses Python identifier discountCode
    __discountCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'discountCode'), 'discountCode', '__httpwww_litle_comschema_createDiscountType_httpwww_litle_comschemadiscountCode', False)

    
    discountCode = property(__discountCode.value, __discountCode.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_createDiscountType_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}endDate uses Python identifier endDate
    __endDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'endDate'), 'endDate', '__httpwww_litle_comschema_createDiscountType_httpwww_litle_comschemaendDate', False)

    
    endDate = property(__endDate.value, __endDate.set, None, None)

    
    # Element {http://www.litle.com/schema}startDate uses Python identifier startDate
    __startDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'startDate'), 'startDate', '__httpwww_litle_comschema_createDiscountType_httpwww_litle_comschemastartDate', False)

    
    startDate = property(__startDate.value, __startDate.set, None, None)

    
    # Element {http://www.litle.com/schema}name uses Python identifier name
    __name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_litle_comschema_createDiscountType_httpwww_litle_comschemaname', False)

    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __discountCode.name() : __discountCode,
        __amount.name() : __amount,
        __endDate.name() : __endDate,
        __startDate.name() : __startDate,
        __name.name() : __name
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'createDiscountType', createDiscountType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_58 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_58_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_58_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_58_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_58_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_58_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httpwww_litle_comschema_CTD_ANON_58_duplicate', pyxb.binding.datatypes.boolean)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __message.name() : __message,
        __response.name() : __response,
        __postDate.name() : __postDate,
        __litleTxnId.name() : __litleTxnId,
        __responseTime.name() : __responseTime
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_59 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Element {http://www.litle.com/schema}payPalNotes uses Python identifier payPalNotes
    __payPalNotes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes'), 'payPalNotes', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemapayPalNotes', False)

    
    payPalNotes = property(__payPalNotes.value, __payPalNotes.set, None, None)

    
    # Element {http://www.litle.com/schema}shipToAddress uses Python identifier shipToAddress
    __shipToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress'), 'shipToAddress', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemashipToAddress', False)

    
    shipToAddress = property(__shipToAddress.value, __shipToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}enhancedData uses Python identifier enhancedData
    __enhancedData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), 'enhancedData', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemaenhancedData', False)

    
    enhancedData = property(__enhancedData.value, __enhancedData.set, None, None)

    
    # Element {http://www.litle.com/schema}paypal uses Python identifier paypal
    __paypal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypal'), 'paypal', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemapaypal', False)

    
    paypal = property(__paypal.value, __paypal.set, None, None)

    
    # Element {http://www.litle.com/schema}mpos uses Python identifier mpos
    __mpos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'mpos'), 'mpos', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemampos', False)

    
    mpos = property(__mpos.value, __mpos.set, None, None)

    
    # Element {http://www.litle.com/schema}allowPartialAuth uses Python identifier allowPartialAuth
    __allowPartialAuth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'allowPartialAuth'), 'allowPartialAuth', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemaallowPartialAuth', False)

    
    allowPartialAuth = property(__allowPartialAuth.value, __allowPartialAuth.set, None, None)

    
    # Element {http://www.litle.com/schema}billMeLaterRequest uses Python identifier billMeLaterRequest
    __billMeLaterRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest'), 'billMeLaterRequest', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemabillMeLaterRequest', False)

    
    billMeLaterRequest = property(__billMeLaterRequest.value, __billMeLaterRequest.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantData uses Python identifier merchantData
    __merchantData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), 'merchantData', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemamerchantData', False)

    
    merchantData = property(__merchantData.value, __merchantData.set, None, None)

    
    # Element {http://www.litle.com/schema}recyclingRequest uses Python identifier recyclingRequest
    __recyclingRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recyclingRequest'), 'recyclingRequest', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemarecyclingRequest', False)

    
    recyclingRequest = property(__recyclingRequest.value, __recyclingRequest.set, None, None)

    
    # Element {http://www.litle.com/schema}filtering uses Python identifier filtering
    __filtering = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'filtering'), 'filtering', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemafiltering', False)

    
    filtering = property(__filtering.value, __filtering.set, None, None)

    
    # Element {http://www.litle.com/schema}processingInstructions uses Python identifier processingInstructions
    __processingInstructions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), 'processingInstructions', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemaprocessingInstructions', False)

    
    processingInstructions = property(__processingInstructions.value, __processingInstructions.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudFilterOverride uses Python identifier fraudFilterOverride
    __fraudFilterOverride = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudFilterOverride'), 'fraudFilterOverride', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemafraudFilterOverride', False)

    
    fraudFilterOverride = property(__fraudFilterOverride.value, __fraudFilterOverride.set, None, None)

    
    # Element {http://www.litle.com/schema}customBilling uses Python identifier customBilling
    __customBilling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), 'customBilling', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemacustomBilling', False)

    
    customBilling = property(__customBilling.value, __customBilling.set, None, None)

    
    # Element {http://www.litle.com/schema}recurringRequest uses Python identifier recurringRequest
    __recurringRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recurringRequest'), 'recurringRequest', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemarecurringRequest', False)

    
    recurringRequest = property(__recurringRequest.value, __recurringRequest.set, None, None)

    
    # Element {http://www.litle.com/schema}billToAddress uses Python identifier billToAddress
    __billToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), 'billToAddress', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemabillToAddress', False)

    
    billToAddress = property(__billToAddress.value, __billToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}token uses Python identifier token
    __token = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'token'), 'token', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschematoken', False)

    
    token = property(__token.value, __token.set, None, None)

    
    # Element {http://www.litle.com/schema}litleInternalRecurringRequest uses Python identifier litleInternalRecurringRequest
    __litleInternalRecurringRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleInternalRecurringRequest'), 'litleInternalRecurringRequest', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemalitleInternalRecurringRequest', False)

    
    litleInternalRecurringRequest = property(__litleInternalRecurringRequest.value, __litleInternalRecurringRequest.set, None, None)

    
    # Element {http://www.litle.com/schema}amexAggregatorData uses Python identifier amexAggregatorData
    __amexAggregatorData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), 'amexAggregatorData', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemaamexAggregatorData', False)

    
    amexAggregatorData = property(__amexAggregatorData.value, __amexAggregatorData.set, None, None)

    
    # Element {http://www.litle.com/schema}debtRepayment uses Python identifier debtRepayment
    __debtRepayment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment'), 'debtRepayment', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemadebtRepayment', False)

    
    debtRepayment = property(__debtRepayment.value, __debtRepayment.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudCheck uses Python identifier fraudCheck
    __fraudCheck = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudCheck'), 'fraudCheck', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemafraudCheck', False)

    
    fraudCheck = property(__fraudCheck.value, __fraudCheck.set, None, None)

    
    # Element {http://www.litle.com/schema}advancedFraudChecks uses Python identifier advancedFraudChecks
    __advancedFraudChecks = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudChecks'), 'advancedFraudChecks', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemaadvancedFraudChecks', False)

    
    advancedFraudChecks = property(__advancedFraudChecks.value, __advancedFraudChecks.set, None, None)

    
    # Element {http://www.litle.com/schema}surchargeAmount uses Python identifier surchargeAmount
    __surchargeAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), 'surchargeAmount', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemasurchargeAmount', False)

    
    surchargeAmount = property(__surchargeAmount.value, __surchargeAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}cardholderAuthentication uses Python identifier cardholderAuthentication
    __cardholderAuthentication = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardholderAuthentication'), 'cardholderAuthentication', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemacardholderAuthentication', False)

    
    cardholderAuthentication = property(__cardholderAuthentication.value, __cardholderAuthentication.set, None, None)

    
    # Element {http://www.litle.com/schema}healthcareIIAS uses Python identifier healthcareIIAS
    __healthcareIIAS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'healthcareIIAS'), 'healthcareIIAS', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemahealthcareIIAS', False)

    
    healthcareIIAS = property(__healthcareIIAS.value, __healthcareIIAS.set, None, None)

    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}taxType uses Python identifier taxType
    __taxType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxType'), 'taxType', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemataxType', False)

    
    taxType = property(__taxType.value, __taxType.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}customerInfo uses Python identifier customerInfo
    __customerInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerInfo'), 'customerInfo', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemacustomerInfo', False)

    
    customerInfo = property(__customerInfo.value, __customerInfo.set, None, None)

    
    # Element {http://www.litle.com/schema}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pos'), 'pos', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemapos', False)

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}paypage uses Python identifier paypage
    __paypage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypage'), 'paypage', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemapaypage', False)

    
    paypage = property(__paypage.value, __paypage.set, None, None)

    
    # Element {http://www.litle.com/schema}payPalOrderComplete uses Python identifier payPalOrderComplete
    __payPalOrderComplete = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'payPalOrderComplete'), 'payPalOrderComplete', '__httpwww_litle_comschema_CTD_ANON_59_httpwww_litle_comschemapayPalOrderComplete', False)

    
    payPalOrderComplete = property(__payPalOrderComplete.value, __payPalOrderComplete.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __orderSource.name() : __orderSource,
        __payPalNotes.name() : __payPalNotes,
        __shipToAddress.name() : __shipToAddress,
        __enhancedData.name() : __enhancedData,
        __paypal.name() : __paypal,
        __mpos.name() : __mpos,
        __allowPartialAuth.name() : __allowPartialAuth,
        __billMeLaterRequest.name() : __billMeLaterRequest,
        __merchantData.name() : __merchantData,
        __recyclingRequest.name() : __recyclingRequest,
        __filtering.name() : __filtering,
        __processingInstructions.name() : __processingInstructions,
        __fraudFilterOverride.name() : __fraudFilterOverride,
        __customBilling.name() : __customBilling,
        __recurringRequest.name() : __recurringRequest,
        __billToAddress.name() : __billToAddress,
        __token.name() : __token,
        __litleInternalRecurringRequest.name() : __litleInternalRecurringRequest,
        __amexAggregatorData.name() : __amexAggregatorData,
        __debtRepayment.name() : __debtRepayment,
        __fraudCheck.name() : __fraudCheck,
        __advancedFraudChecks.name() : __advancedFraudChecks,
        __surchargeAmount.name() : __surchargeAmount,
        __cardholderAuthentication.name() : __cardholderAuthentication,
        __healthcareIIAS.name() : __healthcareIIAS,
        __card.name() : __card,
        __litleTxnId.name() : __litleTxnId,
        __taxType.name() : __taxType,
        __orderId.name() : __orderId,
        __customerInfo.name() : __customerInfo,
        __pos.name() : __pos,
        __amount.name() : __amount,
        __paypage.name() : __paypage,
        __payPalOrderComplete.name() : __payPalOrderComplete
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_60 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_60_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_60_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_60_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_60_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_60_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_60_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_60_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __response.name() : __response,
        __postDate.name() : __postDate,
        __responseTime.name() : __responseTime,
        __litleTxnId.name() : __litleTxnId,
        __message.name() : __message,
        __orderId.name() : __orderId,
        __giftCardResponse.name() : __giftCardResponse
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_61 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}accountUpdater uses Python identifier accountUpdater
    __accountUpdater = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), 'accountUpdater', '__httpwww_litle_comschema_CTD_ANON_61_httpwww_litle_comschemaaccountUpdater', False)

    
    accountUpdater = property(__accountUpdater.value, __accountUpdater.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_61_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponse uses Python identifier tokenResponse
    __tokenResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), 'tokenResponse', '__httpwww_litle_comschema_CTD_ANON_61_httpwww_litle_comschematokenResponse', False)

    
    tokenResponse = property(__tokenResponse.value, __tokenResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_61_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_61_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_61_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_61_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_61_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_61_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_61_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __accountUpdater.name() : __accountUpdater,
        __orderId.name() : __orderId,
        __tokenResponse.name() : __tokenResponse,
        __fraudResult.name() : __fraudResult,
        __message.name() : __message,
        __response.name() : __response,
        __responseTime.name() : __responseTime,
        __giftCardResponse.name() : __giftCardResponse,
        __litleTxnId.name() : __litleTxnId,
        __postDate.name() : __postDate
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}payPal with content type ELEMENT_ONLY
class payPal (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'payPal')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'transactionId'), 'transactionId', '__httpwww_litle_comschema_payPal_httpwww_litle_comschematransactionId', False)

    
    transactionId = property(__transactionId.value, __transactionId.set, None, None)

    
    # Element {http://www.litle.com/schema}payerId uses Python identifier payerId
    __payerId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'payerId'), 'payerId', '__httpwww_litle_comschema_payPal_httpwww_litle_comschemapayerId', False)

    
    payerId = property(__payerId.value, __payerId.set, None, None)

    
    # Element {http://www.litle.com/schema}token uses Python identifier token
    __token = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'token'), 'token', '__httpwww_litle_comschema_payPal_httpwww_litle_comschematoken', False)

    
    token = property(__token.value, __token.set, None, None)


    _ElementMap = {
        __transactionId.name() : __transactionId,
        __payerId.name() : __payerId,
        __token.name() : __token
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'payPal', payPal)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_62 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_62_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_62_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_62_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_62_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_62_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_62_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_62_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}approvedAmount uses Python identifier approvedAmount
    __approvedAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'approvedAmount'), 'approvedAmount', '__httpwww_litle_comschema_CTD_ANON_62_httpwww_litle_comschemaapprovedAmount', False)

    
    approvedAmount = property(__approvedAmount.value, __approvedAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_62_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId,
        __postDate.name() : __postDate,
        __orderId.name() : __orderId,
        __message.name() : __message,
        __response.name() : __response,
        __fraudResult.name() : __fraudResult,
        __giftCardResponse.name() : __giftCardResponse,
        __approvedAmount.name() : __approvedAmount,
        __responseTime.name() : __responseTime
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}transactionTypeOptionReportGroup with content type EMPTY
class transactionTypeOptionReportGroup (transactionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'transactionTypeOptionReportGroup')
    # Base type is transactionType
    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup uses Python identifier reportGroup
    __reportGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'reportGroup'), 'reportGroup', '__httpwww_litle_comschema_transactionTypeOptionReportGroup_reportGroup', reportGroupType)
    
    reportGroup = property(__reportGroup.value, __reportGroup.set, None, None)

    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionType._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = transactionType._AttributeMap.copy()
    _AttributeMap.update({
        __reportGroup.name() : __reportGroup
    })
Namespace.addCategoryObject('typeBinding', u'transactionTypeOptionReportGroup', transactionTypeOptionReportGroup)


# Complex type {http://www.litle.com/schema}fraudCheckType with content type ELEMENT_ONLY
class fraudCheckType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fraudCheckType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}authenticatedByMerchant uses Python identifier authenticatedByMerchant
    __authenticatedByMerchant = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authenticatedByMerchant'), 'authenticatedByMerchant', '__httpwww_litle_comschema_fraudCheckType_httpwww_litle_comschemaauthenticatedByMerchant', False)

    
    authenticatedByMerchant = property(__authenticatedByMerchant.value, __authenticatedByMerchant.set, None, None)

    
    # Element {http://www.litle.com/schema}authenticationTransactionId uses Python identifier authenticationTransactionId
    __authenticationTransactionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authenticationTransactionId'), 'authenticationTransactionId', '__httpwww_litle_comschema_fraudCheckType_httpwww_litle_comschemaauthenticationTransactionId', False)

    
    authenticationTransactionId = property(__authenticationTransactionId.value, __authenticationTransactionId.set, None, None)

    
    # Element {http://www.litle.com/schema}authenticationValue uses Python identifier authenticationValue
    __authenticationValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authenticationValue'), 'authenticationValue', '__httpwww_litle_comschema_fraudCheckType_httpwww_litle_comschemaauthenticationValue', False)

    
    authenticationValue = property(__authenticationValue.value, __authenticationValue.set, None, None)

    
    # Element {http://www.litle.com/schema}customerIpAddress uses Python identifier customerIpAddress
    __customerIpAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerIpAddress'), 'customerIpAddress', '__httpwww_litle_comschema_fraudCheckType_httpwww_litle_comschemacustomerIpAddress', False)

    
    customerIpAddress = property(__customerIpAddress.value, __customerIpAddress.set, None, None)


    _ElementMap = {
        __authenticatedByMerchant.name() : __authenticatedByMerchant,
        __authenticationTransactionId.name() : __authenticationTransactionId,
        __authenticationValue.name() : __authenticationValue,
        __customerIpAddress.name() : __customerIpAddress
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'fraudCheckType', fraudCheckType)


# Complex type {http://www.litle.com/schema}updateDiscountType with content type ELEMENT_ONLY
class updateDiscountType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'updateDiscountType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}endDate uses Python identifier endDate
    __endDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'endDate'), 'endDate', '__httpwww_litle_comschema_updateDiscountType_httpwww_litle_comschemaendDate', False)

    
    endDate = property(__endDate.value, __endDate.set, None, None)

    
    # Element {http://www.litle.com/schema}name uses Python identifier name
    __name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_litle_comschema_updateDiscountType_httpwww_litle_comschemaname', False)

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_updateDiscountType_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}startDate uses Python identifier startDate
    __startDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'startDate'), 'startDate', '__httpwww_litle_comschema_updateDiscountType_httpwww_litle_comschemastartDate', False)

    
    startDate = property(__startDate.value, __startDate.set, None, None)

    
    # Element {http://www.litle.com/schema}discountCode uses Python identifier discountCode
    __discountCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'discountCode'), 'discountCode', '__httpwww_litle_comschema_updateDiscountType_httpwww_litle_comschemadiscountCode', False)

    
    discountCode = property(__discountCode.value, __discountCode.set, None, None)


    _ElementMap = {
        __endDate.name() : __endDate,
        __name.name() : __name,
        __amount.name() : __amount,
        __startDate.name() : __startDate,
        __discountCode.name() : __discountCode
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'updateDiscountType', updateDiscountType)


# Complex type {http://www.litle.com/schema}echeckType with content type ELEMENT_ONLY
class echeckType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'echeckType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}accType uses Python identifier accType
    __accType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accType'), 'accType', '__httpwww_litle_comschema_echeckType_httpwww_litle_comschemaaccType', False)

    
    accType = property(__accType.value, __accType.set, None, None)

    
    # Element {http://www.litle.com/schema}checkNum uses Python identifier checkNum
    __checkNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'checkNum'), 'checkNum', '__httpwww_litle_comschema_echeckType_httpwww_litle_comschemacheckNum', False)

    
    checkNum = property(__checkNum.value, __checkNum.set, None, None)

    
    # Element {http://www.litle.com/schema}accNum uses Python identifier accNum
    __accNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accNum'), 'accNum', '__httpwww_litle_comschema_echeckType_httpwww_litle_comschemaaccNum', False)

    
    accNum = property(__accNum.value, __accNum.set, None, None)

    
    # Element {http://www.litle.com/schema}routingNum uses Python identifier routingNum
    __routingNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'routingNum'), 'routingNum', '__httpwww_litle_comschema_echeckType_httpwww_litle_comschemaroutingNum', False)

    
    routingNum = property(__routingNum.value, __routingNum.set, None, None)


    _ElementMap = {
        __accType.name() : __accType,
        __checkNum.name() : __checkNum,
        __accNum.name() : __accNum,
        __routingNum.name() : __routingNum
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'echeckType', echeckType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_63 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_63_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_63_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_63_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_63_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_63_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_63_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_63_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __orderId.name() : __orderId,
        __giftCardResponse.name() : __giftCardResponse,
        __message.name() : __message,
        __response.name() : __response,
        __responseTime.name() : __responseTime,
        __postDate.name() : __postDate,
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_64 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_64_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_65 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}advancedFraudChecks uses Python identifier advancedFraudChecks
    __advancedFraudChecks = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudChecks'), 'advancedFraudChecks', '__httpwww_litle_comschema_CTD_ANON_65_httpwww_litle_comschemaadvancedFraudChecks', False)

    
    advancedFraudChecks = property(__advancedFraudChecks.value, __advancedFraudChecks.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __advancedFraudChecks.name() : __advancedFraudChecks
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}driversLicenseInfo with content type ELEMENT_ONLY
class driversLicenseInfo (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'driversLicenseInfo')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}dateOfBirth uses Python identifier dateOfBirth
    __dateOfBirth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth'), 'dateOfBirth', '__httpwww_litle_comschema_driversLicenseInfo_httpwww_litle_comschemadateOfBirth', False)

    
    dateOfBirth = property(__dateOfBirth.value, __dateOfBirth.set, None, None)

    
    # Element {http://www.litle.com/schema}licenseNumber uses Python identifier licenseNumber
    __licenseNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'licenseNumber'), 'licenseNumber', '__httpwww_litle_comschema_driversLicenseInfo_httpwww_litle_comschemalicenseNumber', False)

    
    licenseNumber = property(__licenseNumber.value, __licenseNumber.set, None, None)

    
    # Element {http://www.litle.com/schema}state uses Python identifier state
    __state = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'state'), 'state', '__httpwww_litle_comschema_driversLicenseInfo_httpwww_litle_comschemastate', False)

    
    state = property(__state.value, __state.set, None, None)


    _ElementMap = {
        __dateOfBirth.name() : __dateOfBirth,
        __licenseNumber.name() : __licenseNumber,
        __state.name() : __state
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'driversLicenseInfo', driversLicenseInfo)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_66 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_66_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_66_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_66_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_66_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_66_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_66_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_66_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId,
        __message.name() : __message,
        __orderId.name() : __orderId,
        __giftCardResponse.name() : __giftCardResponse,
        __response.name() : __response,
        __responseTime.name() : __responseTime,
        __postDate.name() : __postDate
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_67 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}recycling uses Python identifier recycling
    __recycling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recycling'), 'recycling', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemarecycling', False)

    
    recycling = property(__recycling.value, __recycling.set, None, None)

    
    # Element {http://www.litle.com/schema}authCode uses Python identifier authCode
    __authCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authCode'), 'authCode', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemaauthCode', False)

    
    authCode = property(__authCode.value, __authCode.set, None, None)

    
    # Element {http://www.litle.com/schema}accountUpdater uses Python identifier accountUpdater
    __accountUpdater = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), 'accountUpdater', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemaaccountUpdater', False)

    
    accountUpdater = property(__accountUpdater.value, __accountUpdater.set, None, None)

    
    # Element {http://www.litle.com/schema}recurringResponse uses Python identifier recurringResponse
    __recurringResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recurringResponse'), 'recurringResponse', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemarecurringResponse', False)

    
    recurringResponse = property(__recurringResponse.value, __recurringResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponse uses Python identifier tokenResponse
    __tokenResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), 'tokenResponse', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschematokenResponse', False)

    
    tokenResponse = property(__tokenResponse.value, __tokenResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}cardProductId uses Python identifier cardProductId
    __cardProductId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardProductId'), 'cardProductId', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemacardProductId', False)

    
    cardProductId = property(__cardProductId.value, __cardProductId.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}approvedAmount uses Python identifier approvedAmount
    __approvedAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'approvedAmount'), 'approvedAmount', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemaapprovedAmount', False)

    
    approvedAmount = property(__approvedAmount.value, __approvedAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}enhancedAuthResponse uses Python identifier enhancedAuthResponse
    __enhancedAuthResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'enhancedAuthResponse'), 'enhancedAuthResponse', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemaenhancedAuthResponse', False)

    
    enhancedAuthResponse = property(__enhancedAuthResponse.value, __enhancedAuthResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}authorizationResponseSubCode uses Python identifier authorizationResponseSubCode
    __authorizationResponseSubCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authorizationResponseSubCode'), 'authorizationResponseSubCode', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemaauthorizationResponseSubCode', False)

    
    authorizationResponseSubCode = property(__authorizationResponseSubCode.value, __authorizationResponseSubCode.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}billMeLaterResponseData uses Python identifier billMeLaterResponseData
    __billMeLaterResponseData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterResponseData'), 'billMeLaterResponseData', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemabillMeLaterResponseData', False)

    
    billMeLaterResponseData = property(__billMeLaterResponseData.value, __billMeLaterResponseData.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}accountInformation uses Python identifier accountInformation
    __accountInformation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountInformation'), 'accountInformation', '__httpwww_litle_comschema_CTD_ANON_67_httpwww_litle_comschemaaccountInformation', False)

    
    accountInformation = property(__accountInformation.value, __accountInformation.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httpwww_litle_comschema_CTD_ANON_67_duplicate', pyxb.binding.datatypes.boolean)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __recycling.name() : __recycling,
        __authCode.name() : __authCode,
        __accountUpdater.name() : __accountUpdater,
        __recurringResponse.name() : __recurringResponse,
        __tokenResponse.name() : __tokenResponse,
        __cardProductId.name() : __cardProductId,
        __giftCardResponse.name() : __giftCardResponse,
        __responseTime.name() : __responseTime,
        __approvedAmount.name() : __approvedAmount,
        __orderId.name() : __orderId,
        __enhancedAuthResponse.name() : __enhancedAuthResponse,
        __fraudResult.name() : __fraudResult,
        __postDate.name() : __postDate,
        __authorizationResponseSubCode.name() : __authorizationResponseSubCode,
        __response.name() : __response,
        __billMeLaterResponseData.name() : __billMeLaterResponseData,
        __litleTxnId.name() : __litleTxnId,
        __message.name() : __message,
        __accountInformation.name() : __accountInformation
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_68 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_68_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_68_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_68_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_68_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_68_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_68_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_68_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_68_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httpwww_litle_comschema_CTD_ANON_68_duplicate', pyxb.binding.datatypes.boolean)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __giftCardResponse.name() : __giftCardResponse,
        __postDate.name() : __postDate,
        __litleTxnId.name() : __litleTxnId,
        __orderId.name() : __orderId,
        __message.name() : __message,
        __fraudResult.name() : __fraudResult,
        __response.name() : __response,
        __responseTime.name() : __responseTime
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_69 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_69_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}authAmount uses Python identifier authAmount
    __authAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authAmount'), 'authAmount', '__httpwww_litle_comschema_CTD_ANON_69_httpwww_litle_comschemaauthAmount', False)

    
    authAmount = property(__authAmount.value, __authAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}authDate uses Python identifier authDate
    __authDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authDate'), 'authDate', '__httpwww_litle_comschema_CTD_ANON_69_httpwww_litle_comschemaauthDate', False)

    
    authDate = property(__authDate.value, __authDate.set, None, None)

    
    # Element {http://www.litle.com/schema}authCode uses Python identifier authCode
    __authCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authCode'), 'authCode', '__httpwww_litle_comschema_CTD_ANON_69_httpwww_litle_comschemaauthCode', False)

    
    authCode = property(__authCode.value, __authCode.set, None, None)


    _ElementMap = {
        __fraudResult.name() : __fraudResult,
        __authAmount.name() : __authAmount,
        __authDate.name() : __authDate,
        __authCode.name() : __authCode
    }
    _AttributeMap = {
        
    }



# Complex type {http://www.litle.com/schema}recycleAdviceType with content type ELEMENT_ONLY
class recycleAdviceType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recycleAdviceType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}nextRecycleTime uses Python identifier nextRecycleTime
    __nextRecycleTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nextRecycleTime'), 'nextRecycleTime', '__httpwww_litle_comschema_recycleAdviceType_httpwww_litle_comschemanextRecycleTime', False)

    
    nextRecycleTime = property(__nextRecycleTime.value, __nextRecycleTime.set, None, None)

    
    # Element {http://www.litle.com/schema}recycleAdviceEnd uses Python identifier recycleAdviceEnd
    __recycleAdviceEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recycleAdviceEnd'), 'recycleAdviceEnd', '__httpwww_litle_comschema_recycleAdviceType_httpwww_litle_comschemarecycleAdviceEnd', False)

    
    recycleAdviceEnd = property(__recycleAdviceEnd.value, __recycleAdviceEnd.set, None, None)


    _ElementMap = {
        __nextRecycleTime.name() : __nextRecycleTime,
        __recycleAdviceEnd.name() : __recycleAdviceEnd
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'recycleAdviceType', recycleAdviceType)


# Complex type {http://www.litle.com/schema}litleInternalRecurringRequestType with content type ELEMENT_ONLY
class litleInternalRecurringRequestType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'litleInternalRecurringRequestType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}finalPayment uses Python identifier finalPayment
    __finalPayment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'finalPayment'), 'finalPayment', '__httpwww_litle_comschema_litleInternalRecurringRequestType_httpwww_litle_comschemafinalPayment', False)

    
    finalPayment = property(__finalPayment.value, __finalPayment.set, None, None)

    
    # Element {http://www.litle.com/schema}recurringTxnId uses Python identifier recurringTxnId
    __recurringTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recurringTxnId'), 'recurringTxnId', '__httpwww_litle_comschema_litleInternalRecurringRequestType_httpwww_litle_comschemarecurringTxnId', False)

    
    recurringTxnId = property(__recurringTxnId.value, __recurringTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}subscriptionId uses Python identifier subscriptionId
    __subscriptionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), 'subscriptionId', '__httpwww_litle_comschema_litleInternalRecurringRequestType_httpwww_litle_comschemasubscriptionId', False)

    
    subscriptionId = property(__subscriptionId.value, __subscriptionId.set, None, None)


    _ElementMap = {
        __finalPayment.name() : __finalPayment,
        __recurringTxnId.name() : __recurringTxnId,
        __subscriptionId.name() : __subscriptionId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'litleInternalRecurringRequestType', litleInternalRecurringRequestType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_70 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}cardOrToken uses Python identifier cardOrToken
    __cardOrToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardOrToken'), 'cardOrToken', '__httpwww_litle_comschema_CTD_ANON_70_httpwww_litle_comschemacardOrToken', False)

    
    cardOrToken = property(__cardOrToken.value, __cardOrToken.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_70_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __cardOrToken.name() : __cardOrToken,
        __orderId.name() : __orderId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}registerTokenRequestType with content type ELEMENT_ONLY
class registerTokenRequestType (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'registerTokenRequestType')
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}paypageRegistrationId uses Python identifier paypageRegistrationId
    __paypageRegistrationId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypageRegistrationId'), 'paypageRegistrationId', '__httpwww_litle_comschema_registerTokenRequestType_httpwww_litle_comschemapaypageRegistrationId', False)

    
    paypageRegistrationId = property(__paypageRegistrationId.value, __paypageRegistrationId.set, None, None)

    
    # Element {http://www.litle.com/schema}echeckForToken uses Python identifier echeckForToken
    __echeckForToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'echeckForToken'), 'echeckForToken', '__httpwww_litle_comschema_registerTokenRequestType_httpwww_litle_comschemaecheckForToken', False)

    
    echeckForToken = property(__echeckForToken.value, __echeckForToken.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_registerTokenRequestType_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}accountNumber uses Python identifier accountNumber
    __accountNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountNumber'), 'accountNumber', '__httpwww_litle_comschema_registerTokenRequestType_httpwww_litle_comschemaaccountNumber', False)

    
    accountNumber = property(__accountNumber.value, __accountNumber.set, None, None)

    
    # Element {http://www.litle.com/schema}cardValidationNum uses Python identifier cardValidationNum
    __cardValidationNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), 'cardValidationNum', '__httpwww_litle_comschema_registerTokenRequestType_httpwww_litle_comschemacardValidationNum', False)

    
    cardValidationNum = property(__cardValidationNum.value, __cardValidationNum.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __paypageRegistrationId.name() : __paypageRegistrationId,
        __echeckForToken.name() : __echeckForToken,
        __orderId.name() : __orderId,
        __accountNumber.name() : __accountNumber,
        __cardValidationNum.name() : __cardValidationNum
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'registerTokenRequestType', registerTokenRequestType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_71 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}enhancedAuthResponse uses Python identifier enhancedAuthResponse
    __enhancedAuthResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'enhancedAuthResponse'), 'enhancedAuthResponse', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemaenhancedAuthResponse', False)

    
    enhancedAuthResponse = property(__enhancedAuthResponse.value, __enhancedAuthResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponse uses Python identifier tokenResponse
    __tokenResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), 'tokenResponse', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschematokenResponse', False)

    
    tokenResponse = property(__tokenResponse.value, __tokenResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}authCode uses Python identifier authCode
    __authCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authCode'), 'authCode', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemaauthCode', False)

    
    authCode = property(__authCode.value, __authCode.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}accountUpdater uses Python identifier accountUpdater
    __accountUpdater = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), 'accountUpdater', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemaaccountUpdater', False)

    
    accountUpdater = property(__accountUpdater.value, __accountUpdater.set, None, None)

    
    # Element {http://www.litle.com/schema}accountInformation uses Python identifier accountInformation
    __accountInformation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountInformation'), 'accountInformation', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemaaccountInformation', False)

    
    accountInformation = property(__accountInformation.value, __accountInformation.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}authorizationResponseSubCode uses Python identifier authorizationResponseSubCode
    __authorizationResponseSubCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authorizationResponseSubCode'), 'authorizationResponseSubCode', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemaauthorizationResponseSubCode', False)

    
    authorizationResponseSubCode = property(__authorizationResponseSubCode.value, __authorizationResponseSubCode.set, None, None)

    
    # Element {http://www.litle.com/schema}recurringResponse uses Python identifier recurringResponse
    __recurringResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recurringResponse'), 'recurringResponse', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemarecurringResponse', False)

    
    recurringResponse = property(__recurringResponse.value, __recurringResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}recycling uses Python identifier recycling
    __recycling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recycling'), 'recycling', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemarecycling', False)

    
    recycling = property(__recycling.value, __recycling.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}cardProductId uses Python identifier cardProductId
    __cardProductId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cardProductId'), 'cardProductId', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemacardProductId', False)

    
    cardProductId = property(__cardProductId.value, __cardProductId.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}billMeLaterResponseData uses Python identifier billMeLaterResponseData
    __billMeLaterResponseData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterResponseData'), 'billMeLaterResponseData', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemabillMeLaterResponseData', False)

    
    billMeLaterResponseData = property(__billMeLaterResponseData.value, __billMeLaterResponseData.set, None, None)

    
    # Element {http://www.litle.com/schema}approvedAmount uses Python identifier approvedAmount
    __approvedAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'approvedAmount'), 'approvedAmount', '__httpwww_litle_comschema_CTD_ANON_71_httpwww_litle_comschemaapprovedAmount', False)

    
    approvedAmount = property(__approvedAmount.value, __approvedAmount.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __enhancedAuthResponse.name() : __enhancedAuthResponse,
        __tokenResponse.name() : __tokenResponse,
        __authCode.name() : __authCode,
        __postDate.name() : __postDate,
        __orderId.name() : __orderId,
        __response.name() : __response,
        __accountUpdater.name() : __accountUpdater,
        __accountInformation.name() : __accountInformation,
        __message.name() : __message,
        __responseTime.name() : __responseTime,
        __fraudResult.name() : __fraudResult,
        __authorizationResponseSubCode.name() : __authorizationResponseSubCode,
        __recurringResponse.name() : __recurringResponse,
        __recycling.name() : __recycling,
        __litleTxnId.name() : __litleTxnId,
        __cardProductId.name() : __cardProductId,
        __giftCardResponse.name() : __giftCardResponse,
        __billMeLaterResponseData.name() : __billMeLaterResponseData,
        __approvedAmount.name() : __approvedAmount
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}echeckTokenInfoType with content type ELEMENT_ONLY
class echeckTokenInfoType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'echeckTokenInfoType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}routingNum uses Python identifier routingNum
    __routingNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'routingNum'), 'routingNum', '__httpwww_litle_comschema_echeckTokenInfoType_httpwww_litle_comschemaroutingNum', False)

    
    routingNum = property(__routingNum.value, __routingNum.set, None, None)

    
    # Element {http://www.litle.com/schema}accType uses Python identifier accType
    __accType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accType'), 'accType', '__httpwww_litle_comschema_echeckTokenInfoType_httpwww_litle_comschemaaccType', False)

    
    accType = property(__accType.value, __accType.set, None, None)

    
    # Element {http://www.litle.com/schema}litleToken uses Python identifier litleToken
    __litleToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), 'litleToken', '__httpwww_litle_comschema_echeckTokenInfoType_httpwww_litle_comschemalitleToken', False)

    
    litleToken = property(__litleToken.value, __litleToken.set, None, None)


    _ElementMap = {
        __routingNum.name() : __routingNum,
        __accType.name() : __accType,
        __litleToken.name() : __litleToken
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'echeckTokenInfoType', echeckTokenInfoType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_72 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_72_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_72_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_72_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_72_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_72_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __responseTime.name() : __responseTime,
        __message.name() : __message,
        __orderId.name() : __orderId,
        __response.name() : __response,
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_73 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}actionReason uses Python identifier actionReason
    __actionReason = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'actionReason'), 'actionReason', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemaactionReason', False)

    
    actionReason = property(__actionReason.value, __actionReason.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}customBilling uses Python identifier customBilling
    __customBilling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), 'customBilling', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemacustomBilling', False)

    
    customBilling = property(__customBilling.value, __customBilling.set, None, None)

    
    # Element {http://www.litle.com/schema}paypage uses Python identifier paypage
    __paypage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypage'), 'paypage', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemapaypage', False)

    
    paypage = property(__paypage.value, __paypage.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantData uses Python identifier merchantData
    __merchantData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), 'merchantData', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemamerchantData', False)

    
    merchantData = property(__merchantData.value, __merchantData.set, None, None)

    
    # Element {http://www.litle.com/schema}billMeLaterRequest uses Python identifier billMeLaterRequest
    __billMeLaterRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest'), 'billMeLaterRequest', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemabillMeLaterRequest', False)

    
    billMeLaterRequest = property(__billMeLaterRequest.value, __billMeLaterRequest.set, None, None)

    
    # Element {http://www.litle.com/schema}amexAggregatorData uses Python identifier amexAggregatorData
    __amexAggregatorData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), 'amexAggregatorData', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemaamexAggregatorData', False)

    
    amexAggregatorData = property(__amexAggregatorData.value, __amexAggregatorData.set, None, None)

    
    # Element {http://www.litle.com/schema}billToAddress uses Python identifier billToAddress
    __billToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), 'billToAddress', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemabillToAddress', False)

    
    billToAddress = property(__billToAddress.value, __billToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}paypal uses Python identifier paypal
    __paypal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypal'), 'paypal', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemapaypal', False)

    
    paypal = property(__paypal.value, __paypal.set, None, None)

    
    # Element {http://www.litle.com/schema}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pos'), 'pos', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemapos', False)

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.litle.com/schema}surchargeAmount uses Python identifier surchargeAmount
    __surchargeAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), 'surchargeAmount', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemasurchargeAmount', False)

    
    surchargeAmount = property(__surchargeAmount.value, __surchargeAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}enhancedData uses Python identifier enhancedData
    __enhancedData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), 'enhancedData', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemaenhancedData', False)

    
    enhancedData = property(__enhancedData.value, __enhancedData.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Element {http://www.litle.com/schema}processingInstructions uses Python identifier processingInstructions
    __processingInstructions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), 'processingInstructions', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemaprocessingInstructions', False)

    
    processingInstructions = property(__processingInstructions.value, __processingInstructions.set, None, None)

    
    # Element {http://www.litle.com/schema}taxType uses Python identifier taxType
    __taxType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxType'), 'taxType', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemataxType', False)

    
    taxType = property(__taxType.value, __taxType.set, None, None)

    
    # Element {http://www.litle.com/schema}token uses Python identifier token
    __token = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'token'), 'token', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschematoken', False)

    
    token = property(__token.value, __token.set, None, None)

    
    # Element {http://www.litle.com/schema}mpos uses Python identifier mpos
    __mpos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'mpos'), 'mpos', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemampos', False)

    
    mpos = property(__mpos.value, __mpos.set, None, None)

    
    # Element {http://www.litle.com/schema}payPalNotes uses Python identifier payPalNotes
    __payPalNotes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes'), 'payPalNotes', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemapayPalNotes', False)

    
    payPalNotes = property(__payPalNotes.value, __payPalNotes.set, None, None)

    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_73_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __actionReason.name() : __actionReason,
        __orderId.name() : __orderId,
        __customBilling.name() : __customBilling,
        __paypage.name() : __paypage,
        __merchantData.name() : __merchantData,
        __billMeLaterRequest.name() : __billMeLaterRequest,
        __amexAggregatorData.name() : __amexAggregatorData,
        __billToAddress.name() : __billToAddress,
        __paypal.name() : __paypal,
        __pos.name() : __pos,
        __surchargeAmount.name() : __surchargeAmount,
        __enhancedData.name() : __enhancedData,
        __orderSource.name() : __orderSource,
        __processingInstructions.name() : __processingInstructions,
        __taxType.name() : __taxType,
        __token.name() : __token,
        __mpos.name() : __mpos,
        __payPalNotes.name() : __payPalNotes,
        __card.name() : __card,
        __litleTxnId.name() : __litleTxnId,
        __amount.name() : __amount
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}advancedFraudResultsType with content type ELEMENT_ONLY
class advancedFraudResultsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'advancedFraudResultsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}deviceReviewStatus uses Python identifier deviceReviewStatus
    __deviceReviewStatus = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'deviceReviewStatus'), 'deviceReviewStatus', '__httpwww_litle_comschema_advancedFraudResultsType_httpwww_litle_comschemadeviceReviewStatus', False)

    
    deviceReviewStatus = property(__deviceReviewStatus.value, __deviceReviewStatus.set, None, None)

    
    # Element {http://www.litle.com/schema}deviceReputationScore uses Python identifier deviceReputationScore
    __deviceReputationScore = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'deviceReputationScore'), 'deviceReputationScore', '__httpwww_litle_comschema_advancedFraudResultsType_httpwww_litle_comschemadeviceReputationScore', False)

    
    deviceReputationScore = property(__deviceReputationScore.value, __deviceReputationScore.set, None, None)

    
    # Element {http://www.litle.com/schema}triggeredRule uses Python identifier triggeredRule
    __triggeredRule = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'triggeredRule'), 'triggeredRule', '__httpwww_litle_comschema_advancedFraudResultsType_httpwww_litle_comschematriggeredRule', True)

    
    triggeredRule = property(__triggeredRule.value, __triggeredRule.set, None, None)


    _ElementMap = {
        __deviceReviewStatus.name() : __deviceReviewStatus,
        __deviceReputationScore.name() : __deviceReputationScore,
        __triggeredRule.name() : __triggeredRule
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'advancedFraudResultsType', advancedFraudResultsType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_74 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_74_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_74_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_74_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_74_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_74_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_74_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_74_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __responseTime.name() : __responseTime,
        __orderId.name() : __orderId,
        __postDate.name() : __postDate,
        __message.name() : __message,
        __giftCardResponse.name() : __giftCardResponse,
        __litleTxnId.name() : __litleTxnId,
        __response.name() : __response
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}recurringSubscriptionType with content type ELEMENT_ONLY
class recurringSubscriptionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recurringSubscriptionType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_recurringSubscriptionType_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}planCode uses Python identifier planCode
    __planCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'planCode'), 'planCode', '__httpwww_litle_comschema_recurringSubscriptionType_httpwww_litle_comschemaplanCode', False)

    
    planCode = property(__planCode.value, __planCode.set, None, None)

    
    # Element {http://www.litle.com/schema}createDiscount uses Python identifier createDiscount
    __createDiscount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'createDiscount'), 'createDiscount', '__httpwww_litle_comschema_recurringSubscriptionType_httpwww_litle_comschemacreateDiscount', True)

    
    createDiscount = property(__createDiscount.value, __createDiscount.set, None, None)

    
    # Element {http://www.litle.com/schema}numberOfPayments uses Python identifier numberOfPayments
    __numberOfPayments = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numberOfPayments'), 'numberOfPayments', '__httpwww_litle_comschema_recurringSubscriptionType_httpwww_litle_comschemanumberOfPayments', False)

    
    numberOfPayments = property(__numberOfPayments.value, __numberOfPayments.set, None, None)

    
    # Element {http://www.litle.com/schema}createAddOn uses Python identifier createAddOn
    __createAddOn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'createAddOn'), 'createAddOn', '__httpwww_litle_comschema_recurringSubscriptionType_httpwww_litle_comschemacreateAddOn', True)

    
    createAddOn = property(__createAddOn.value, __createAddOn.set, None, None)

    
    # Element {http://www.litle.com/schema}startDate uses Python identifier startDate
    __startDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'startDate'), 'startDate', '__httpwww_litle_comschema_recurringSubscriptionType_httpwww_litle_comschemastartDate', False)

    
    startDate = property(__startDate.value, __startDate.set, None, None)


    _ElementMap = {
        __amount.name() : __amount,
        __planCode.name() : __planCode,
        __createDiscount.name() : __createDiscount,
        __numberOfPayments.name() : __numberOfPayments,
        __createAddOn.name() : __createAddOn,
        __startDate.name() : __startDate
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'recurringSubscriptionType', recurringSubscriptionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_75 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_75_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_75_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_75_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}advancedFraudResults uses Python identifier advancedFraudResults
    __advancedFraudResults = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudResults'), 'advancedFraudResults', '__httpwww_litle_comschema_CTD_ANON_75_httpwww_litle_comschemaadvancedFraudResults', False)

    
    advancedFraudResults = property(__advancedFraudResults.value, __advancedFraudResults.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_75_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __message.name() : __message,
        __responseTime.name() : __responseTime,
        __litleTxnId.name() : __litleTxnId,
        __advancedFraudResults.name() : __advancedFraudResults,
        __response.name() : __response
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_76 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_76_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}payPalNotes uses Python identifier payPalNotes
    __payPalNotes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes'), 'payPalNotes', '__httpwww_litle_comschema_CTD_ANON_76_httpwww_litle_comschemapayPalNotes', False)

    
    payPalNotes = property(__payPalNotes.value, __payPalNotes.set, None, None)

    
    # Element {http://www.litle.com/schema}actionReason uses Python identifier actionReason
    __actionReason = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'actionReason'), 'actionReason', '__httpwww_litle_comschema_CTD_ANON_76_httpwww_litle_comschemaactionReason', False)

    
    actionReason = property(__actionReason.value, __actionReason.set, None, None)

    
    # Element {http://www.litle.com/schema}surchargeAmount uses Python identifier surchargeAmount
    __surchargeAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), 'surchargeAmount', '__httpwww_litle_comschema_CTD_ANON_76_httpwww_litle_comschemasurchargeAmount', False)

    
    surchargeAmount = property(__surchargeAmount.value, __surchargeAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_76_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __litleTxnId.name() : __litleTxnId,
        __payPalNotes.name() : __payPalNotes,
        __actionReason.name() : __actionReason,
        __surchargeAmount.name() : __surchargeAmount,
        __amount.name() : __amount
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}baseRequest with content type ELEMENT_ONLY
class baseRequest (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseRequest')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}recurringTransaction uses Python identifier recurringTransaction
    __recurringTransaction = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'recurringTransaction'), 'recurringTransaction', '__httpwww_litle_comschema_baseRequest_httpwww_litle_comschemarecurringTransaction', False)

    
    recurringTransaction = property(__recurringTransaction.value, __recurringTransaction.set, None, None)

    
    # Element {http://www.litle.com/schema}transaction uses Python identifier transaction
    __transaction = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'transaction'), 'transaction', '__httpwww_litle_comschema_baseRequest_httpwww_litle_comschematransaction', False)

    
    transaction = property(__transaction.value, __transaction.set, None, None)

    
    # Element {http://www.litle.com/schema}authentication uses Python identifier authentication
    __authentication = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authentication'), 'authentication', '__httpwww_litle_comschema_baseRequest_httpwww_litle_comschemaauthentication', False)

    
    authentication = property(__authentication.value, __authentication.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_litle_comschema_baseRequest_version', versionType, required=True)
    
    version = property(__version.value, __version.set, None, None)


    _ElementMap = {
        __recurringTransaction.name() : __recurringTransaction,
        __transaction.name() : __transaction,
        __authentication.name() : __authentication
    }
    _AttributeMap = {
        __version.name() : __version
    }
Namespace.addCategoryObject('typeBinding', u'baseRequest', baseRequest)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_77 (baseRequest):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is baseRequest
    
    # Element recurringTransaction ({http://www.litle.com/schema}recurringTransaction) inherited from {http://www.litle.com/schema}baseRequest
    
    # Element transaction ({http://www.litle.com/schema}transaction) inherited from {http://www.litle.com/schema}baseRequest
    
    # Element authentication ({http://www.litle.com/schema}authentication) inherited from {http://www.litle.com/schema}baseRequest
    
    # Attribute version inherited from {http://www.litle.com/schema}baseRequest
    
    # Attribute merchantSdk uses Python identifier merchantSdk
    __merchantSdk = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'merchantSdk'), 'merchantSdk', '__httpwww_litle_comschema_CTD_ANON_77_merchantSdk', pyxb.binding.datatypes.string)
    
    merchantSdk = property(__merchantSdk.value, __merchantSdk.set, None, None)

    
    # Attribute merchantId uses Python identifier merchantId
    __merchantId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'merchantId'), 'merchantId', '__httpwww_litle_comschema_CTD_ANON_77_merchantId', merchantIdentificationType, required=True)
    
    merchantId = property(__merchantId.value, __merchantId.set, None, None)

    
    # Attribute loggedInUser uses Python identifier loggedInUser
    __loggedInUser = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'loggedInUser'), 'loggedInUser', '__httpwww_litle_comschema_CTD_ANON_77_loggedInUser', pyxb.binding.datatypes.string)
    
    loggedInUser = property(__loggedInUser.value, __loggedInUser.set, None, None)


    _ElementMap = baseRequest._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = baseRequest._AttributeMap.copy()
    _AttributeMap.update({
        __merchantSdk.name() : __merchantSdk,
        __merchantId.name() : __merchantId,
        __loggedInUser.name() : __loggedInUser
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_78 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_78_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_78_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_78_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_78_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __card.name() : __card,
        __amount.name() : __amount,
        __orderId.name() : __orderId,
        __orderSource.name() : __orderSource
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}transactionTypeWithReportGroupAndPartial with content type EMPTY
class transactionTypeWithReportGroupAndPartial (transactionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'transactionTypeWithReportGroupAndPartial')
    # Base type is transactionType
    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute partial uses Python identifier partial
    __partial = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'partial'), 'partial', '__httpwww_litle_comschema_transactionTypeWithReportGroupAndPartial_partial', pyxb.binding.datatypes.boolean)
    
    partial = property(__partial.value, __partial.set, None, None)

    
    # Attribute reportGroup uses Python identifier reportGroup
    __reportGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'reportGroup'), 'reportGroup', '__httpwww_litle_comschema_transactionTypeWithReportGroupAndPartial_reportGroup', reportGroupType, required=True)
    
    reportGroup = property(__reportGroup.value, __reportGroup.set, None, None)


    _ElementMap = transactionType._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = transactionType._AttributeMap.copy()
    _AttributeMap.update({
        __partial.name() : __partial,
        __reportGroup.name() : __reportGroup
    })
Namespace.addCategoryObject('typeBinding', u'transactionTypeWithReportGroupAndPartial', transactionTypeWithReportGroupAndPartial)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_79 (transactionTypeWithReportGroupAndPartial):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroupAndPartial
    
    # Element {http://www.litle.com/schema}payPalOrderComplete uses Python identifier payPalOrderComplete
    __payPalOrderComplete = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'payPalOrderComplete'), 'payPalOrderComplete', '__httpwww_litle_comschema_CTD_ANON_79_httpwww_litle_comschemapayPalOrderComplete', False)

    
    payPalOrderComplete = property(__payPalOrderComplete.value, __payPalOrderComplete.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_79_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}payPalNotes uses Python identifier payPalNotes
    __payPalNotes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes'), 'payPalNotes', '__httpwww_litle_comschema_CTD_ANON_79_httpwww_litle_comschemapayPalNotes', False)

    
    payPalNotes = property(__payPalNotes.value, __payPalNotes.set, None, None)

    
    # Element {http://www.litle.com/schema}enhancedData uses Python identifier enhancedData
    __enhancedData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), 'enhancedData', '__httpwww_litle_comschema_CTD_ANON_79_httpwww_litle_comschemaenhancedData', False)

    
    enhancedData = property(__enhancedData.value, __enhancedData.set, None, None)

    
    # Element {http://www.litle.com/schema}surchargeAmount uses Python identifier surchargeAmount
    __surchargeAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), 'surchargeAmount', '__httpwww_litle_comschema_CTD_ANON_79_httpwww_litle_comschemasurchargeAmount', False)

    
    surchargeAmount = property(__surchargeAmount.value, __surchargeAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}processingInstructions uses Python identifier processingInstructions
    __processingInstructions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), 'processingInstructions', '__httpwww_litle_comschema_CTD_ANON_79_httpwww_litle_comschemaprocessingInstructions', False)

    
    processingInstructions = property(__processingInstructions.value, __processingInstructions.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_79_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute partial inherited from {http://www.litle.com/schema}transactionTypeWithReportGroupAndPartial
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroupAndPartial

    _ElementMap = transactionTypeWithReportGroupAndPartial._ElementMap.copy()
    _ElementMap.update({
        __payPalOrderComplete.name() : __payPalOrderComplete,
        __amount.name() : __amount,
        __payPalNotes.name() : __payPalNotes,
        __enhancedData.name() : __enhancedData,
        __surchargeAmount.name() : __surchargeAmount,
        __processingInstructions.name() : __processingInstructions,
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroupAndPartial._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_80 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}taxType uses Python identifier taxType
    __taxType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxType'), 'taxType', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemataxType', False)

    
    taxType = property(__taxType.value, __taxType.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}paypage uses Python identifier paypage
    __paypage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypage'), 'paypage', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemapaypage', False)

    
    paypage = property(__paypage.value, __paypage.set, None, None)

    
    # Element {http://www.litle.com/schema}billToAddress uses Python identifier billToAddress
    __billToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), 'billToAddress', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemabillToAddress', False)

    
    billToAddress = property(__billToAddress.value, __billToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantData uses Python identifier merchantData
    __merchantData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), 'merchantData', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemamerchantData', False)

    
    merchantData = property(__merchantData.value, __merchantData.set, None, None)

    
    # Element {http://www.litle.com/schema}mpos uses Python identifier mpos
    __mpos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'mpos'), 'mpos', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemampos', False)

    
    mpos = property(__mpos.value, __mpos.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}token uses Python identifier token
    __token = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'token'), 'token', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschematoken', False)

    
    token = property(__token.value, __token.set, None, None)

    
    # Element {http://www.litle.com/schema}debtRepayment uses Python identifier debtRepayment
    __debtRepayment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment'), 'debtRepayment', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemadebtRepayment', False)

    
    debtRepayment = property(__debtRepayment.value, __debtRepayment.set, None, None)

    
    # Element {http://www.litle.com/schema}amexAggregatorData uses Python identifier amexAggregatorData
    __amexAggregatorData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), 'amexAggregatorData', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemaamexAggregatorData', False)

    
    amexAggregatorData = property(__amexAggregatorData.value, __amexAggregatorData.set, None, None)

    
    # Element {http://www.litle.com/schema}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pos'), 'pos', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemapos', False)

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Element {http://www.litle.com/schema}processingInstructions uses Python identifier processingInstructions
    __processingInstructions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), 'processingInstructions', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemaprocessingInstructions', False)

    
    processingInstructions = property(__processingInstructions.value, __processingInstructions.set, None, None)

    
    # Element {http://www.litle.com/schema}customBilling uses Python identifier customBilling
    __customBilling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), 'customBilling', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemacustomBilling', False)

    
    customBilling = property(__customBilling.value, __customBilling.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Element {http://www.litle.com/schema}enhancedData uses Python identifier enhancedData
    __enhancedData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), 'enhancedData', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemaenhancedData', False)

    
    enhancedData = property(__enhancedData.value, __enhancedData.set, None, None)

    
    # Element {http://www.litle.com/schema}surchargeAmount uses Python identifier surchargeAmount
    __surchargeAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), 'surchargeAmount', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemasurchargeAmount', False)

    
    surchargeAmount = property(__surchargeAmount.value, __surchargeAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_80_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __taxType.name() : __taxType,
        __orderId.name() : __orderId,
        __paypage.name() : __paypage,
        __billToAddress.name() : __billToAddress,
        __merchantData.name() : __merchantData,
        __mpos.name() : __mpos,
        __amount.name() : __amount,
        __token.name() : __token,
        __debtRepayment.name() : __debtRepayment,
        __amexAggregatorData.name() : __amexAggregatorData,
        __pos.name() : __pos,
        __processingInstructions.name() : __processingInstructions,
        __customBilling.name() : __customBilling,
        __orderSource.name() : __orderSource,
        __enhancedData.name() : __enhancedData,
        __surchargeAmount.name() : __surchargeAmount,
        __card.name() : __card
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}deleteDiscountType with content type ELEMENT_ONLY
class deleteDiscountType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'deleteDiscountType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}discountCode uses Python identifier discountCode
    __discountCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'discountCode'), 'discountCode', '__httpwww_litle_comschema_deleteDiscountType_httpwww_litle_comschemadiscountCode', False)

    
    discountCode = property(__discountCode.value, __discountCode.set, None, None)


    _ElementMap = {
        __discountCode.name() : __discountCode
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'deleteDiscountType', deleteDiscountType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_81 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_81_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_81_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_81_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_81_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_81_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}virtualGiftCardResponse uses Python identifier virtualGiftCardResponse
    __virtualGiftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualGiftCardResponse'), 'virtualGiftCardResponse', '__httpwww_litle_comschema_CTD_ANON_81_httpwww_litle_comschemavirtualGiftCardResponse', False)

    
    virtualGiftCardResponse = property(__virtualGiftCardResponse.value, __virtualGiftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_81_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_81_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_81_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httpwww_litle_comschema_CTD_ANON_81_duplicate', pyxb.binding.datatypes.boolean)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __message.name() : __message,
        __fraudResult.name() : __fraudResult,
        __giftCardResponse.name() : __giftCardResponse,
        __orderId.name() : __orderId,
        __response.name() : __response,
        __virtualGiftCardResponse.name() : __virtualGiftCardResponse,
        __litleTxnId.name() : __litleTxnId,
        __postDate.name() : __postDate,
        __responseTime.name() : __responseTime
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_82 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_82_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_82_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}verificationCode uses Python identifier verificationCode
    __verificationCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'verificationCode'), 'verificationCode', '__httpwww_litle_comschema_CTD_ANON_82_httpwww_litle_comschemaverificationCode', False)

    
    verificationCode = property(__verificationCode.value, __verificationCode.set, None, None)

    
    # Element {http://www.litle.com/schema}accountUpdater uses Python identifier accountUpdater
    __accountUpdater = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), 'accountUpdater', '__httpwww_litle_comschema_CTD_ANON_82_httpwww_litle_comschemaaccountUpdater', False)

    
    accountUpdater = property(__accountUpdater.value, __accountUpdater.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_82_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_82_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_82_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponse uses Python identifier tokenResponse
    __tokenResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), 'tokenResponse', '__httpwww_litle_comschema_CTD_ANON_82_httpwww_litle_comschematokenResponse', False)

    
    tokenResponse = property(__tokenResponse.value, __tokenResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_82_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httpwww_litle_comschema_CTD_ANON_82_duplicate', pyxb.binding.datatypes.boolean)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __message.name() : __message,
        __response.name() : __response,
        __verificationCode.name() : __verificationCode,
        __accountUpdater.name() : __accountUpdater,
        __postDate.name() : __postDate,
        __orderId.name() : __orderId,
        __responseTime.name() : __responseTime,
        __tokenResponse.name() : __tokenResponse,
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_83 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_83_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_83_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_83_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_83_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_83_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponse uses Python identifier tokenResponse
    __tokenResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), 'tokenResponse', '__httpwww_litle_comschema_CTD_ANON_83_httpwww_litle_comschematokenResponse', False)

    
    tokenResponse = property(__tokenResponse.value, __tokenResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_83_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __responseTime.name() : __responseTime,
        __litleTxnId.name() : __litleTxnId,
        __orderId.name() : __orderId,
        __response.name() : __response,
        __postDate.name() : __postDate,
        __tokenResponse.name() : __tokenResponse,
        __message.name() : __message
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}echeckForTokenType with content type ELEMENT_ONLY
class echeckForTokenType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'echeckForTokenType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}routingNum uses Python identifier routingNum
    __routingNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'routingNum'), 'routingNum', '__httpwww_litle_comschema_echeckForTokenType_httpwww_litle_comschemaroutingNum', False)

    
    routingNum = property(__routingNum.value, __routingNum.set, None, None)

    
    # Element {http://www.litle.com/schema}accNum uses Python identifier accNum
    __accNum = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accNum'), 'accNum', '__httpwww_litle_comschema_echeckForTokenType_httpwww_litle_comschemaaccNum', False)

    
    accNum = property(__accNum.value, __accNum.set, None, None)


    _ElementMap = {
        __routingNum.name() : __routingNum,
        __accNum.name() : __accNum
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'echeckForTokenType', echeckForTokenType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_84 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_84_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_84_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_84_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}virtualGiftCard uses Python identifier virtualGiftCard
    __virtualGiftCard = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'virtualGiftCard'), 'virtualGiftCard', '__httpwww_litle_comschema_CTD_ANON_84_httpwww_litle_comschemavirtualGiftCard', False)

    
    virtualGiftCard = property(__virtualGiftCard.value, __virtualGiftCard.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_84_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __card.name() : __card,
        __amount.name() : __amount,
        __orderId.name() : __orderId,
        __virtualGiftCard.name() : __virtualGiftCard,
        __orderSource.name() : __orderSource
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_85 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}echeckOrEcheckToken uses Python identifier echeckOrEcheckToken
    __echeckOrEcheckToken = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken'), 'echeckOrEcheckToken', '__httpwww_litle_comschema_CTD_ANON_85_httpwww_litle_comschemaecheckOrEcheckToken', False)

    
    echeckOrEcheckToken = property(__echeckOrEcheckToken.value, __echeckOrEcheckToken.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_85_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}billToAddress uses Python identifier billToAddress
    __billToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), 'billToAddress', '__httpwww_litle_comschema_CTD_ANON_85_httpwww_litle_comschemabillToAddress', False)

    
    billToAddress = property(__billToAddress.value, __billToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_85_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Element {http://www.litle.com/schema}verify uses Python identifier verify
    __verify = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'verify'), 'verify', '__httpwww_litle_comschema_CTD_ANON_85_httpwww_litle_comschemaverify', False)

    
    verify = property(__verify.value, __verify.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_85_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantData uses Python identifier merchantData
    __merchantData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), 'merchantData', '__httpwww_litle_comschema_CTD_ANON_85_httpwww_litle_comschemamerchantData', False)

    
    merchantData = property(__merchantData.value, __merchantData.set, None, None)

    
    # Element {http://www.litle.com/schema}shipToAddress uses Python identifier shipToAddress
    __shipToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress'), 'shipToAddress', '__httpwww_litle_comschema_CTD_ANON_85_httpwww_litle_comschemashipToAddress', False)

    
    shipToAddress = property(__shipToAddress.value, __shipToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}customBilling uses Python identifier customBilling
    __customBilling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), 'customBilling', '__httpwww_litle_comschema_CTD_ANON_85_httpwww_litle_comschemacustomBilling', False)

    
    customBilling = property(__customBilling.value, __customBilling.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_85_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __echeckOrEcheckToken.name() : __echeckOrEcheckToken,
        __litleTxnId.name() : __litleTxnId,
        __billToAddress.name() : __billToAddress,
        __orderSource.name() : __orderSource,
        __verify.name() : __verify,
        __amount.name() : __amount,
        __merchantData.name() : __merchantData,
        __shipToAddress.name() : __shipToAddress,
        __customBilling.name() : __customBilling,
        __orderId.name() : __orderId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_86 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_86_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}tokenResponse uses Python identifier tokenResponse
    __tokenResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), 'tokenResponse', '__httpwww_litle_comschema_CTD_ANON_86_httpwww_litle_comschematokenResponse', False)

    
    tokenResponse = property(__tokenResponse.value, __tokenResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_86_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_86_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}accountUpdater uses Python identifier accountUpdater
    __accountUpdater = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), 'accountUpdater', '__httpwww_litle_comschema_CTD_ANON_86_httpwww_litle_comschemaaccountUpdater', False)

    
    accountUpdater = property(__accountUpdater.value, __accountUpdater.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_86_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_86_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_86_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httpwww_litle_comschema_CTD_ANON_86_duplicate', pyxb.binding.datatypes.boolean)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __postDate.name() : __postDate,
        __tokenResponse.name() : __tokenResponse,
        __response.name() : __response,
        __litleTxnId.name() : __litleTxnId,
        __accountUpdater.name() : __accountUpdater,
        __responseTime.name() : __responseTime,
        __message.name() : __message,
        __orderId.name() : __orderId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_87 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_87_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_87_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_87_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __card.name() : __card,
        __orderSource.name() : __orderSource,
        __orderId.name() : __orderId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type {http://www.litle.com/schema}updateAddOnType with content type ELEMENT_ONLY
class updateAddOnType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'updateAddOnType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}endDate uses Python identifier endDate
    __endDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'endDate'), 'endDate', '__httpwww_litle_comschema_updateAddOnType_httpwww_litle_comschemaendDate', False)

    
    endDate = property(__endDate.value, __endDate.set, None, None)

    
    # Element {http://www.litle.com/schema}name uses Python identifier name
    __name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpwww_litle_comschema_updateAddOnType_httpwww_litle_comschemaname', False)

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_updateAddOnType_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}addOnCode uses Python identifier addOnCode
    __addOnCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addOnCode'), 'addOnCode', '__httpwww_litle_comschema_updateAddOnType_httpwww_litle_comschemaaddOnCode', False)

    
    addOnCode = property(__addOnCode.value, __addOnCode.set, None, None)

    
    # Element {http://www.litle.com/schema}startDate uses Python identifier startDate
    __startDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'startDate'), 'startDate', '__httpwww_litle_comschema_updateAddOnType_httpwww_litle_comschemastartDate', False)

    
    startDate = property(__startDate.value, __startDate.set, None, None)


    _ElementMap = {
        __endDate.name() : __endDate,
        __name.name() : __name,
        __amount.name() : __amount,
        __addOnCode.name() : __addOnCode,
        __startDate.name() : __startDate
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'updateAddOnType', updateAddOnType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_88 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}authInformation uses Python identifier authInformation
    __authInformation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'authInformation'), 'authInformation', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemaauthInformation', False)

    
    authInformation = property(__authInformation.value, __authInformation.set, None, None)

    
    # Element {http://www.litle.com/schema}paypage uses Python identifier paypage
    __paypage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypage'), 'paypage', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemapaypage', False)

    
    paypage = property(__paypage.value, __paypage.set, None, None)

    
    # Element {http://www.litle.com/schema}token uses Python identifier token
    __token = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'token'), 'token', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschematoken', False)

    
    token = property(__token.value, __token.set, None, None)

    
    # Element {http://www.litle.com/schema}taxType uses Python identifier taxType
    __taxType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxType'), 'taxType', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemataxType', False)

    
    taxType = property(__taxType.value, __taxType.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantData uses Python identifier merchantData
    __merchantData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), 'merchantData', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemamerchantData', False)

    
    merchantData = property(__merchantData.value, __merchantData.set, None, None)

    
    # Element {http://www.litle.com/schema}billMeLaterRequest uses Python identifier billMeLaterRequest
    __billMeLaterRequest = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest'), 'billMeLaterRequest', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemabillMeLaterRequest', False)

    
    billMeLaterRequest = property(__billMeLaterRequest.value, __billMeLaterRequest.set, None, None)

    
    # Element {http://www.litle.com/schema}billToAddress uses Python identifier billToAddress
    __billToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), 'billToAddress', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemabillToAddress', False)

    
    billToAddress = property(__billToAddress.value, __billToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}surchargeAmount uses Python identifier surchargeAmount
    __surchargeAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), 'surchargeAmount', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemasurchargeAmount', False)

    
    surchargeAmount = property(__surchargeAmount.value, __surchargeAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}amexAggregatorData uses Python identifier amexAggregatorData
    __amexAggregatorData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), 'amexAggregatorData', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemaamexAggregatorData', False)

    
    amexAggregatorData = property(__amexAggregatorData.value, __amexAggregatorData.set, None, None)

    
    # Element {http://www.litle.com/schema}enhancedData uses Python identifier enhancedData
    __enhancedData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), 'enhancedData', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemaenhancedData', False)

    
    enhancedData = property(__enhancedData.value, __enhancedData.set, None, None)

    
    # Element {http://www.litle.com/schema}shipToAddress uses Python identifier shipToAddress
    __shipToAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress'), 'shipToAddress', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemashipToAddress', False)

    
    shipToAddress = property(__shipToAddress.value, __shipToAddress.set, None, None)

    
    # Element {http://www.litle.com/schema}customBilling uses Python identifier customBilling
    __customBilling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), 'customBilling', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemacustomBilling', False)

    
    customBilling = property(__customBilling.value, __customBilling.set, None, None)

    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}debtRepayment uses Python identifier debtRepayment
    __debtRepayment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment'), 'debtRepayment', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemadebtRepayment', False)

    
    debtRepayment = property(__debtRepayment.value, __debtRepayment.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}processingInstructions uses Python identifier processingInstructions
    __processingInstructions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), 'processingInstructions', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemaprocessingInstructions', False)

    
    processingInstructions = property(__processingInstructions.value, __processingInstructions.set, None, None)

    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Element {http://www.litle.com/schema}mpos uses Python identifier mpos
    __mpos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'mpos'), 'mpos', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemampos', False)

    
    mpos = property(__mpos.value, __mpos.set, None, None)

    
    # Element {http://www.litle.com/schema}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pos'), 'pos', '__httpwww_litle_comschema_CTD_ANON_88_httpwww_litle_comschemapos', False)

    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __authInformation.name() : __authInformation,
        __paypage.name() : __paypage,
        __token.name() : __token,
        __taxType.name() : __taxType,
        __merchantData.name() : __merchantData,
        __billMeLaterRequest.name() : __billMeLaterRequest,
        __billToAddress.name() : __billToAddress,
        __surchargeAmount.name() : __surchargeAmount,
        __amexAggregatorData.name() : __amexAggregatorData,
        __enhancedData.name() : __enhancedData,
        __shipToAddress.name() : __shipToAddress,
        __customBilling.name() : __customBilling,
        __card.name() : __card,
        __amount.name() : __amount,
        __debtRepayment.name() : __debtRepayment,
        __orderId.name() : __orderId,
        __processingInstructions.name() : __processingInstructions,
        __orderSource.name() : __orderSource,
        __mpos.name() : __mpos,
        __pos.name() : __pos
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_89 (recurringTransactionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is recurringTransactionType
    
    # Element {http://www.litle.com/schema}subscriptionId uses Python identifier subscriptionId
    __subscriptionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), 'subscriptionId', '__httpwww_litle_comschema_CTD_ANON_89_httpwww_litle_comschemasubscriptionId', False)

    
    subscriptionId = property(__subscriptionId.value, __subscriptionId.set, None, None)


    _ElementMap = recurringTransactionType._ElementMap.copy()
    _ElementMap.update({
        __subscriptionId.name() : __subscriptionId
    })
    _AttributeMap = recurringTransactionType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_90 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}postDate uses Python identifier postDate
    __postDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postDate'), 'postDate', '__httpwww_litle_comschema_CTD_ANON_90_httpwww_litle_comschemapostDate', False)

    
    postDate = property(__postDate.value, __postDate.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_90_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}giftCardResponse uses Python identifier giftCardResponse
    __giftCardResponse = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), 'giftCardResponse', '__httpwww_litle_comschema_CTD_ANON_90_httpwww_litle_comschemagiftCardResponse', False)

    
    giftCardResponse = property(__giftCardResponse.value, __giftCardResponse.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudResult uses Python identifier fraudResult
    __fraudResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), 'fraudResult', '__httpwww_litle_comschema_CTD_ANON_90_httpwww_litle_comschemafraudResult', False)

    
    fraudResult = property(__fraudResult.value, __fraudResult.set, None, None)

    
    # Element {http://www.litle.com/schema}response uses Python identifier response
    __response = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_90_httpwww_litle_comschemaresponse', False)

    
    response = property(__response.value, __response.set, None, None)

    
    # Element {http://www.litle.com/schema}message uses Python identifier message
    __message = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_90_httpwww_litle_comschemamessage', False)

    
    message = property(__message.value, __message.set, None, None)

    
    # Element {http://www.litle.com/schema}responseTime uses Python identifier responseTime
    __responseTime = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), 'responseTime', '__httpwww_litle_comschema_CTD_ANON_90_httpwww_litle_comschemaresponseTime', False)

    
    responseTime = property(__responseTime.value, __responseTime.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_CTD_ANON_90_httpwww_litle_comschemalitleTxnId', False)

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httpwww_litle_comschema_CTD_ANON_90_duplicate', pyxb.binding.datatypes.boolean)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __postDate.name() : __postDate,
        __orderId.name() : __orderId,
        __giftCardResponse.name() : __giftCardResponse,
        __fraudResult.name() : __fraudResult,
        __response.name() : __response,
        __message.name() : __message,
        __responseTime.name() : __responseTime,
        __litleTxnId.name() : __litleTxnId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_91 (transactionTypeWithReportGroup):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is transactionTypeWithReportGroup
    
    # Element {http://www.litle.com/schema}orderSource uses Python identifier orderSource
    __orderSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), 'orderSource', '__httpwww_litle_comschema_CTD_ANON_91_httpwww_litle_comschemaorderSource', False)

    
    orderSource = property(__orderSource.value, __orderSource.set, None, None)

    
    # Element {http://www.litle.com/schema}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpwww_litle_comschema_CTD_ANON_91_httpwww_litle_comschemaamount', False)

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://www.litle.com/schema}card uses Python identifier card
    __card = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'card'), 'card', '__httpwww_litle_comschema_CTD_ANON_91_httpwww_litle_comschemacard', False)

    
    card = property(__card.value, __card.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_CTD_ANON_91_httpwww_litle_comschemaorderId', False)

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Attribute id inherited from {http://www.litle.com/schema}transactionType
    
    # Attribute reportGroup inherited from {http://www.litle.com/schema}transactionTypeWithReportGroup
    
    # Attribute customerId inherited from {http://www.litle.com/schema}transactionType

    _ElementMap = transactionTypeWithReportGroup._ElementMap.copy()
    _ElementMap.update({
        __orderSource.name() : __orderSource,
        __amount.name() : __amount,
        __card.name() : __card,
        __orderId.name() : __orderId
    })
    _AttributeMap = transactionTypeWithReportGroup._AttributeMap.copy()
    _AttributeMap.update({
        
    })



refundReversal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'refundReversal'), CTD_ANON)
Namespace.addCategoryObject('elementBinding', refundReversal.name().localName(), refundReversal)

litleResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleResponse'), CTD_ANON_3)
Namespace.addCategoryObject('elementBinding', litleResponse.name().localName(), litleResponse)

billMeLaterResponseData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterResponseData'), CTD_ANON_)
Namespace.addCategoryObject('elementBinding', billMeLaterResponseData.name().localName(), billMeLaterResponseData)

loadReversal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadReversal'), CTD_ANON_5)
Namespace.addCategoryObject('elementBinding', loadReversal.name().localName(), loadReversal)

updatePlan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatePlan'), CTD_ANON_6)
Namespace.addCategoryObject('elementBinding', updatePlan.name().localName(), updatePlan)

unloadReversal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unloadReversal'), CTD_ANON_8)
Namespace.addCategoryObject('elementBinding', unloadReversal.name().localName(), unloadReversal)

cancelSubscriptionResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cancelSubscriptionResponse'), CTD_ANON_9)
Namespace.addCategoryObject('elementBinding', cancelSubscriptionResponse.name().localName(), cancelSubscriptionResponse)

litleRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleRequest'), CTD_ANON_10)
Namespace.addCategoryObject('elementBinding', litleRequest.name().localName(), litleRequest)

updateSubscriptionResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updateSubscriptionResponse'), CTD_ANON_11)
Namespace.addCategoryObject('elementBinding', updateSubscriptionResponse.name().localName(), updateSubscriptionResponse)

balanceInquiry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'balanceInquiry'), CTD_ANON_12)
Namespace.addCategoryObject('elementBinding', balanceInquiry.name().localName(), balanceInquiry)

createPlanResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'createPlanResponse'), CTD_ANON_14)
Namespace.addCategoryObject('elementBinding', createPlanResponse.name().localName(), createPlanResponse)

updatePlanResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatePlanResponse'), CTD_ANON_17)
Namespace.addCategoryObject('elementBinding', updatePlanResponse.name().localName(), updatePlanResponse)

activateReversal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'activateReversal'), CTD_ANON_18)
Namespace.addCategoryObject('elementBinding', activateReversal.name().localName(), activateReversal)

unloadReversalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unloadReversalResponse'), CTD_ANON_19)
Namespace.addCategoryObject('elementBinding', unloadReversalResponse.name().localName(), unloadReversalResponse)

updateCardValidationNumOnToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updateCardValidationNumOnToken'), updateCardValidationNumOnToken_)
Namespace.addCategoryObject('elementBinding', updateCardValidationNumOnToken.name().localName(), updateCardValidationNumOnToken)

createPlan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'createPlan'), CTD_ANON_22)
Namespace.addCategoryObject('elementBinding', createPlan.name().localName(), createPlan)

giftCardResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7)
Namespace.addCategoryObject('elementBinding', giftCardResponse.name().localName(), giftCardResponse)

lineItemData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lineItemData'), CTD_ANON_24)
Namespace.addCategoryObject('elementBinding', lineItemData.name().localName(), lineItemData)

deactivateReversalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'deactivateReversalResponse'), CTD_ANON_25)
Namespace.addCategoryObject('elementBinding', deactivateReversalResponse.name().localName(), deactivateReversalResponse)

deactivateReversal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'deactivateReversal'), CTD_ANON_26)
Namespace.addCategoryObject('elementBinding', deactivateReversal.name().localName(), deactivateReversal)

cardOrToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardOrToken'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', cardOrToken.name().localName(), cardOrToken)

customBilling = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), CTD_ANON_16)
Namespace.addCategoryObject('elementBinding', customBilling.name().localName(), customBilling)

batchRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'batchRequest'), CTD_ANON_21)
Namespace.addCategoryObject('elementBinding', batchRequest.name().localName(), batchRequest)

creditResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'creditResponse'), CTD_ANON_27)
Namespace.addCategoryObject('elementBinding', creditResponse.name().localName(), creditResponse)

accountUpdateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdateResponse'), CTD_ANON_28)
Namespace.addCategoryObject('elementBinding', accountUpdateResponse.name().localName(), accountUpdateResponse)

authentication = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authentication'), CTD_ANON_23)
Namespace.addCategoryObject('elementBinding', authentication.name().localName(), authentication)

healthcareAmounts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'healthcareAmounts'), CTD_ANON_31)
Namespace.addCategoryObject('elementBinding', healthcareAmounts.name().localName(), healthcareAmounts)

pos = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pos'), CTD_ANON_2)
Namespace.addCategoryObject('elementBinding', pos.name().localName(), pos)

accountUpdater = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), CTD_ANON_4)
Namespace.addCategoryObject('elementBinding', accountUpdater.name().localName(), accountUpdater)

RFRResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RFRResponse'), CTD_ANON_33)
Namespace.addCategoryObject('elementBinding', RFRResponse.name().localName(), RFRResponse)

echeckVerification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckVerification'), CTD_ANON_34)
Namespace.addCategoryObject('elementBinding', echeckVerification.name().localName(), echeckVerification)

echeckOrEcheckToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', echeckOrEcheckToken.name().localName(), echeckOrEcheckToken)

batchResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'batchResponse'), CTD_ANON_35)
Namespace.addCategoryObject('elementBinding', batchResponse.name().localName(), batchResponse)

recurringTransaction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringTransaction'), recurringTransactionType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', recurringTransaction.name().localName(), recurringTransaction)

echeckToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckToken'), echeckTokenType)
Namespace.addCategoryObject('elementBinding', echeckToken.name().localName(), echeckToken)

healthcareIIAS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'healthcareIIAS'), CTD_ANON_30)
Namespace.addCategoryObject('elementBinding', healthcareIIAS.name().localName(), healthcareIIAS)

registerTokenResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'registerTokenResponse'), CTD_ANON_39)
Namespace.addCategoryObject('elementBinding', registerTokenResponse.name().localName(), registerTokenResponse)

echeckRedeposit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckRedeposit'), CTD_ANON_40)
Namespace.addCategoryObject('elementBinding', echeckRedeposit.name().localName(), echeckRedeposit)

updateSubscription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updateSubscription'), CTD_ANON_42)
Namespace.addCategoryObject('elementBinding', updateSubscription.name().localName(), updateSubscription)

echeckCredit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckCredit'), CTD_ANON_43)
Namespace.addCategoryObject('elementBinding', echeckCredit.name().localName(), echeckCredit)

echeckRedepositResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckRedepositResponse'), CTD_ANON_44)
Namespace.addCategoryObject('elementBinding', echeckRedepositResponse.name().localName(), echeckRedepositResponse)

accountUpdateFileRequestData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdateFileRequestData'), CTD_ANON_20)
Namespace.addCategoryObject('elementBinding', accountUpdateFileRequestData.name().localName(), accountUpdateFileRequestData)

processingInstructions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), CTD_ANON_15)
Namespace.addCategoryObject('elementBinding', processingInstructions.name().localName(), processingInstructions)

authReversalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authReversalResponse'), CTD_ANON_48)
Namespace.addCategoryObject('elementBinding', authReversalResponse.name().localName(), authReversalResponse)

captureResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'captureResponse'), CTD_ANON_49)
Namespace.addCategoryObject('elementBinding', captureResponse.name().localName(), captureResponse)

customerInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerInfo'), CTD_ANON_36)
Namespace.addCategoryObject('elementBinding', customerInfo.name().localName(), customerInfo)

void = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'void'), CTD_ANON_51)
Namespace.addCategoryObject('elementBinding', void.name().localName(), void)

balanceInquiryResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'balanceInquiryResponse'), CTD_ANON_52)
Namespace.addCategoryObject('elementBinding', balanceInquiryResponse.name().localName(), balanceInquiryResponse)

voidResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'voidResponse'), CTD_ANON_53)
Namespace.addCategoryObject('elementBinding', voidResponse.name().localName(), voidResponse)

echeckVoid = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckVoid'), CTD_ANON_54)
Namespace.addCategoryObject('elementBinding', echeckVoid.name().localName(), echeckVoid)

bmlProductType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bmlProductType'), STD_ANON_)
Namespace.addCategoryObject('elementBinding', bmlProductType.name().localName(), bmlProductType)

captureGivenAuthResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'captureGivenAuthResponse'), CTD_ANON_55)
Namespace.addCategoryObject('elementBinding', captureGivenAuthResponse.name().localName(), captureGivenAuthResponse)

litleOnlineResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleOnlineResponse'), CTD_ANON_56)
Namespace.addCategoryObject('elementBinding', litleOnlineResponse.name().localName(), litleOnlineResponse)

authorization = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authorization'), CTD_ANON_57)
Namespace.addCategoryObject('elementBinding', authorization.name().localName(), authorization)

echeckVoidResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckVoidResponse'), CTD_ANON_58)
Namespace.addCategoryObject('elementBinding', echeckVoidResponse.name().localName(), echeckVoidResponse)

amexAggregatorData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), CTD_ANON_38)
Namespace.addCategoryObject('elementBinding', amexAggregatorData.name().localName(), amexAggregatorData)

sale = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sale'), CTD_ANON_59)
Namespace.addCategoryObject('elementBinding', sale.name().localName(), sale)

activateReversalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'activateReversalResponse'), CTD_ANON_60)
Namespace.addCategoryObject('elementBinding', activateReversalResponse.name().localName(), activateReversalResponse)

forceCaptureResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'forceCaptureResponse'), CTD_ANON_61)
Namespace.addCategoryObject('elementBinding', forceCaptureResponse.name().localName(), forceCaptureResponse)

virtualGiftCardResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualGiftCardResponse'), CTD_ANON_46)
Namespace.addCategoryObject('elementBinding', virtualGiftCardResponse.name().localName(), virtualGiftCardResponse)

deactivateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'deactivateResponse'), CTD_ANON_62)
Namespace.addCategoryObject('elementBinding', deactivateResponse.name().localName(), deactivateResponse)

recurringTransactionResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringTransactionResponse'), recurringTransactionResponseType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', recurringTransactionResponse.name().localName(), recurringTransactionResponse)

echeck = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeck'), echeckType)
Namespace.addCategoryObject('elementBinding', echeck.name().localName(), echeck)

loadReversalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadReversalResponse'), CTD_ANON_63)
Namespace.addCategoryObject('elementBinding', loadReversalResponse.name().localName(), loadReversalResponse)

detailTax = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'detailTax'), CTD_ANON_41)
Namespace.addCategoryObject('elementBinding', detailTax.name().localName(), detailTax)

billToAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), contact)
Namespace.addCategoryObject('elementBinding', billToAddress.name().localName(), billToAddress)

depositReversal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'depositReversal'), CTD_ANON_64)
Namespace.addCategoryObject('elementBinding', depositReversal.name().localName(), depositReversal)

fraudCheck = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudCheck'), CTD_ANON_65)
Namespace.addCategoryObject('elementBinding', fraudCheck.name().localName(), fraudCheck)

depositReversalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'depositReversalResponse'), CTD_ANON_66)
Namespace.addCategoryObject('elementBinding', depositReversalResponse.name().localName(), depositReversalResponse)

saleResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'saleResponse'), CTD_ANON_67)
Namespace.addCategoryObject('elementBinding', saleResponse.name().localName(), saleResponse)

loadResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loadResponse'), CTD_ANON_68)
Namespace.addCategoryObject('elementBinding', loadResponse.name().localName(), loadResponse)

card = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType)
Namespace.addCategoryObject('elementBinding', card.name().localName(), card)

accountUpdate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdate'), CTD_ANON_70)
Namespace.addCategoryObject('elementBinding', accountUpdate.name().localName(), accountUpdate)

registerTokenRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'registerTokenRequest'), registerTokenRequestType)
Namespace.addCategoryObject('elementBinding', registerTokenRequest.name().localName(), registerTokenRequest)

enhancedAuthResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enhancedAuthResponse'), CTD_ANON_32)
Namespace.addCategoryObject('elementBinding', enhancedAuthResponse.name().localName(), enhancedAuthResponse)

authorizationResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authorizationResponse'), CTD_ANON_71)
Namespace.addCategoryObject('elementBinding', authorizationResponse.name().localName(), authorizationResponse)

enhancedData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), CTD_ANON_13)
Namespace.addCategoryObject('elementBinding', enhancedData.name().localName(), enhancedData)

updateCardValidationNumOnTokenResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updateCardValidationNumOnTokenResponse'), CTD_ANON_72)
Namespace.addCategoryObject('elementBinding', updateCardValidationNumOnTokenResponse.name().localName(), updateCardValidationNumOnTokenResponse)

billMeLaterRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest'), CTD_ANON_45)
Namespace.addCategoryObject('elementBinding', billMeLaterRequest.name().localName(), billMeLaterRequest)

credit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit'), CTD_ANON_73)
Namespace.addCategoryObject('elementBinding', credit.name().localName(), credit)

transaction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transaction'), transactionType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', transaction.name().localName(), transaction)

refundReversalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'refundReversalResponse'), CTD_ANON_74)
Namespace.addCategoryObject('elementBinding', refundReversalResponse.name().localName(), refundReversalResponse)

token = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'token'), cardTokenType)
Namespace.addCategoryObject('elementBinding', token.name().localName(), token)

fraudCheckResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudCheckResponse'), CTD_ANON_75)
Namespace.addCategoryObject('elementBinding', fraudCheckResponse.name().localName(), fraudCheckResponse)

transactionResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transactionResponse'), transactionTypeWithReportGroup, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', transactionResponse.name().localName(), transactionResponse)

authReversal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authReversal'), CTD_ANON_76)
Namespace.addCategoryObject('elementBinding', authReversal.name().localName(), authReversal)

litleOnlineRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleOnlineRequest'), CTD_ANON_77)
Namespace.addCategoryObject('elementBinding', litleOnlineRequest.name().localName(), litleOnlineRequest)

load = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'load'), CTD_ANON_78)
Namespace.addCategoryObject('elementBinding', load.name().localName(), load)

capture = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'capture'), CTD_ANON_79)
Namespace.addCategoryObject('elementBinding', capture.name().localName(), capture)

fraudResult = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37)
Namespace.addCategoryObject('elementBinding', fraudResult.name().localName(), fraudResult)

forceCapture = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'forceCapture'), CTD_ANON_80)
Namespace.addCategoryObject('elementBinding', forceCapture.name().localName(), forceCapture)

activateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'activateResponse'), CTD_ANON_81)
Namespace.addCategoryObject('elementBinding', activateResponse.name().localName(), activateResponse)

authInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authInformation'), CTD_ANON_69)
Namespace.addCategoryObject('elementBinding', authInformation.name().localName(), authInformation)

echeckSalesResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckSalesResponse'), CTD_ANON_82)
Namespace.addCategoryObject('elementBinding', echeckSalesResponse.name().localName(), echeckSalesResponse)

echeckVerificationResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckVerificationResponse'), CTD_ANON_83)
Namespace.addCategoryObject('elementBinding', echeckVerificationResponse.name().localName(), echeckVerificationResponse)

activate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'activate'), CTD_ANON_84)
Namespace.addCategoryObject('elementBinding', activate.name().localName(), activate)

echeckSale = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckSale'), CTD_ANON_85)
Namespace.addCategoryObject('elementBinding', echeckSale.name().localName(), echeckSale)

echeckCreditResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckCreditResponse'), CTD_ANON_86)
Namespace.addCategoryObject('elementBinding', echeckCreditResponse.name().localName(), echeckCreditResponse)

deactivate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'deactivate'), CTD_ANON_87)
Namespace.addCategoryObject('elementBinding', deactivate.name().localName(), deactivate)

captureGivenAuth = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'captureGivenAuth'), CTD_ANON_88)
Namespace.addCategoryObject('elementBinding', captureGivenAuth.name().localName(), captureGivenAuth)

RFRRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RFRRequest'), CTD_ANON_29)
Namespace.addCategoryObject('elementBinding', RFRRequest.name().localName(), RFRRequest)

cancelSubscription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cancelSubscription'), CTD_ANON_89)
Namespace.addCategoryObject('elementBinding', cancelSubscription.name().localName(), cancelSubscription)

unloadResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unloadResponse'), CTD_ANON_90)
Namespace.addCategoryObject('elementBinding', unloadResponse.name().localName(), unloadResponse)

shipToAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress'), contact)
Namespace.addCategoryObject('elementBinding', shipToAddress.name().localName(), shipToAddress)

unload = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unload'), CTD_ANON_91)
Namespace.addCategoryObject('elementBinding', unload.name().localName(), unload)



voidRecyclingResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'creditLitleTxnId'), litleIdType, scope=voidRecyclingResponseType))
voidRecyclingResponseType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(voidRecyclingResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'creditLitleTxnId')), min_occurs=0L, max_occurs=1)
    )
voidRecyclingResponseType._ContentModel = pyxb.binding.content.ParticleModel(voidRecyclingResponseType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON))
CTD_ANON._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1)
    )
CTD_ANON._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'approvedTermsCode'), STD_ANON_10, scope=CTD_ANON_))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'riskEstimator'), riskEstimator, scope=CTD_ANON_))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'creditLine'), transactionAmountType, scope=CTD_ANON_))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'riskQueueAssignment'), riskQueueAssignment, scope=CTD_ANON_))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bmlMerchantId'), litleIdType, scope=CTD_ANON_))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressIndicator'), addressIndicator, scope=CTD_ANON_))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'promotionalOfferCode'), pyxb.binding.datatypes.string, scope=CTD_ANON_))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'loanToValueEstimator'), loanToValueEstimator, scope=CTD_ANON_))
CTD_ANON_._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bmlMerchantId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'promotionalOfferCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'approvedTermsCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'creditLine')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressIndicator')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'loanToValueEstimator')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'riskEstimator')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'riskQueueAssignment')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'catLevel'), posCatLevelEnum, scope=CTD_ANON_2))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardholderId'), posCardholderIdTypeEnum, scope=CTD_ANON_2))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'terminalId'), pyxb.binding.datatypes.string, scope=CTD_ANON_2))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'capability'), posCapabilityTypeEnum, scope=CTD_ANON_2))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entryMode'), posEntryModeTypeEnum, scope=CTD_ANON_2))
CTD_ANON_2._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'capability')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entryMode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardholderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'terminalId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'catLevel')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_2._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_2._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RFRResponse'), CTD_ANON_33, scope=CTD_ANON_3))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'batchResponse'), CTD_ANON_35, scope=CTD_ANON_3))
CTD_ANON_3._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'batchResponse')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RFRResponse')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_3._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_3._GroupModel_, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_3._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_3._GroupModel, min_occurs=0L, max_occurs=1)



cardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), methodOfPaymentTypeEnum, scope=cardType))

cardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), cvNumType, scope=cardType))

cardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'track'), trackDataType, scope=cardType))

cardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expDate'), expDateType, scope=cardType))

cardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'number'), ccAccountNumberType, scope=cardType))
cardType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'number')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expDate')), min_occurs=0L, max_occurs=1)
    )
cardType._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'track')), min_occurs=0L, max_occurs=1)
    )
cardType._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(cardType._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardType._GroupModel_3, min_occurs=0L, max_occurs=1)
    )
cardType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cardType._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum')), min_occurs=0L, max_occurs=1)
    )
cardType._ContentModel = pyxb.binding.content.ParticleModel(cardType._GroupModel, min_occurs=0L, max_occurs=1)



recurringTransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=recurringTransactionResponseType))

recurringTransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, scope=recurringTransactionResponseType))

recurringTransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=recurringTransactionResponseType))

recurringTransactionResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=recurringTransactionResponseType))
recurringTransactionResponseType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(recurringTransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(recurringTransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recurringTransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recurringTransactionResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1)
    )
recurringTransactionResponseType._ContentModel = pyxb.binding.content.ParticleModel(recurringTransactionResponseType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originalTokenInfo'), echeckTokenInfoType, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'newCardInfo'), cardAccountInfoType, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'newTokenInfo'), echeckTokenInfoType, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extendedCardResponse'), extendedCardResponseType, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'newAccountInfo'), echeckAccountInfoType, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originalAccountInfo'), echeckAccountInfoType, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originalCardInfo'), cardAccountInfoType, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originalCardTokenInfo'), cardTokenInfoType, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'newCardTokenInfo'), cardTokenInfoType, scope=CTD_ANON_4))
CTD_ANON_4._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originalAccountInfo')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'newAccountInfo')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_4._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originalTokenInfo')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'newTokenInfo')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_4._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originalCardInfo')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'newCardInfo')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extendedCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_4._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originalCardTokenInfo')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'newCardTokenInfo')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extendedCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_4._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_4._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._GroupModel_2, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._GroupModel_3, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._GroupModel_4, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extendedCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_4._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_4._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_5))
CTD_ANON_5._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_5._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_5._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_6))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'planCode'), string25Type, scope=CTD_ANON_6))
CTD_ANON_6._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'planCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_6._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_6._GroupModel, min_occurs=0L, max_occurs=1)



cardTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expDate'), expDateType, scope=cardTokenType))

cardTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), cvNumType, scope=cardTokenType))

cardTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), ccAccountNumberType, scope=cardTokenType))

cardTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), methodOfPaymentTypeEnum, scope=cardTokenType))
cardTokenType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cardTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), min_occurs=0L, max_occurs=1)
    )
cardTokenType._ContentModel = pyxb.binding.content.ParticleModel(cardTokenType._GroupModel, min_occurs=0L, max_occurs=1)



cardTokenTypeAU._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bin'), pyxb.binding.datatypes.string, scope=cardTokenTypeAU))
cardTokenTypeAU._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cardTokenTypeAU._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardTokenTypeAU._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardTokenTypeAU._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardTokenTypeAU._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), min_occurs=0L, max_occurs=1)
    )
cardTokenTypeAU._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cardTokenTypeAU._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bin')), min_occurs=0L, max_occurs=1)
    )
cardTokenTypeAU._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cardTokenTypeAU._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardTokenTypeAU._GroupModel_2, min_occurs=0L, max_occurs=1)
    )
cardTokenTypeAU._ContentModel = pyxb.binding.content.ParticleModel(cardTokenTypeAU._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'beginningBalance'), string20Type, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cashBackAmount'), string20Type, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'availableBalance'), string20Type, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endingBalance'), string20Type, scope=CTD_ANON_7))
CTD_ANON_7._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'availableBalance')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'beginningBalance')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'endingBalance')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cashBackAmount')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_7._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_7._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_8))
CTD_ANON_8._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_8._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_8._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), litleIdType, scope=CTD_ANON_9))
CTD_ANON_9._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_9._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_9._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_9._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_9._GroupModel_2, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_9._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_9._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'batchRequest'), CTD_ANON_21, scope=CTD_ANON_10))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authentication'), CTD_ANON_23, scope=CTD_ANON_10))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RFRRequest'), CTD_ANON_29, scope=CTD_ANON_10))
CTD_ANON_10._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'batchRequest')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RFRRequest')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_10._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authentication')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_10._GroupModel_, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_10._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_10._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), litleIdType, scope=CTD_ANON_11))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), tokenResponseType, scope=CTD_ANON_11))
CTD_ANON_11._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_11._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_11._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_11._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._GroupModel_2, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_11._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_11._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_12))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_12))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_12))
CTD_ANON_12._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_12._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_12._GroupModel, min_occurs=0L, max_occurs=1)



deleteAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addOnCode'), string25Type, scope=deleteAddOnType))
deleteAddOnType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(deleteAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addOnCode')), min_occurs=0L, max_occurs=1)
    )
deleteAddOnType._ContentModel = pyxb.binding.content.ParticleModel(deleteAddOnType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shippingAmount'), transactionAmountType, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'deliveryType'), STD_ANON_3, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dutyAmount'), transactionAmountType, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'destinationPostalCode'), zipType, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoiceReferenceNumber'), invoiceReferenceNumberType, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lineItemData'), CTD_ANON_24, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerReference'), customerReferenceType, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'salesTax'), transactionAmountType, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'discountAmount'), transactionAmountType, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxExempt'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shipFromPostalCode'), zipType, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'destinationCountryCode'), countryTypeEnum, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'detailTax'), CTD_ANON_41, scope=CTD_ANON_13))
CTD_ANON_13._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerReference')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'salesTax')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'deliveryType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxExempt')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'discountAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shippingAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dutyAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shipFromPostalCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'destinationPostalCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'destinationCountryCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invoiceReferenceNumber')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'detailTax')), min_occurs=0L, max_occurs=6L),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lineItemData')), min_occurs=0L, max_occurs=99L)
    )
CTD_ANON_13._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_13._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'planCode'), string25Type, scope=CTD_ANON_14))
CTD_ANON_14._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_14._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'planCode')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_14._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_14._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._GroupModel_2, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_14._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_14._GroupModel, min_occurs=0L, max_occurs=1)



createAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endDate'), pyxb.binding.datatypes.date, scope=createAddOnType))

createAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startDate'), pyxb.binding.datatypes.date, scope=createAddOnType))

createAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addOnCode'), string25Type, scope=createAddOnType))

createAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), nameType, scope=createAddOnType))

createAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=createAddOnType))
createAddOnType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(createAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addOnCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(createAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(createAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(createAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'startDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(createAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'endDate')), min_occurs=0L, max_occurs=1)
    )
createAddOnType._ContentModel = pyxb.binding.content.ParticleModel(createAddOnType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bypassVelocityCheck'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_15))
CTD_ANON_15._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bypassVelocityCheck')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_15._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_15._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), customBillingCityType, scope=CTD_ANON_16))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'url'), customBillingUrlType, scope=CTD_ANON_16))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'descriptor'), descriptorType, scope=CTD_ANON_16))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phone'), customBillingPhoneType, scope=CTD_ANON_16))
CTD_ANON_16._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phone')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'url')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_16._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_16._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'descriptor')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_16._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_16._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'planCode'), string25Type, scope=CTD_ANON_17))
CTD_ANON_17._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_17._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'planCode')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_17._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_17._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._GroupModel_2, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_17._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_17._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_18))
CTD_ANON_18._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_18._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_18._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_19))
CTD_ANON_19._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_19._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_19._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDay'), pyxb.binding.datatypes.date, scope=CTD_ANON_20))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantId'), merchantIdentificationType, scope=CTD_ANON_20))
CTD_ANON_20._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDay')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_20._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_20._GroupModel, min_occurs=0L, max_occurs=1)



updateCardValidationNumOnToken_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), cvNumType, scope=updateCardValidationNumOnToken_))

updateCardValidationNumOnToken_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), ccAccountNumberType, scope=updateCardValidationNumOnToken_))

updateCardValidationNumOnToken_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=updateCardValidationNumOnToken_))
updateCardValidationNumOnToken_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(updateCardValidationNumOnToken_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(updateCardValidationNumOnToken_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(updateCardValidationNumOnToken_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum')), min_occurs=0L, max_occurs=1)
    )
updateCardValidationNumOnToken_._ContentModel = pyxb.binding.content.ParticleModel(updateCardValidationNumOnToken_._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transaction'), transactionType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_21))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringTransaction'), recurringTransactionType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_21))
CTD_ANON_21._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transaction')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringTransaction')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_21._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_21._GroupModel, min_occurs=0L, max_occurs=1)



virtualGiftCardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardBin'), pyxb.binding.datatypes.string, scope=virtualGiftCardType))

virtualGiftCardType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountNumberLength'), pyxb.binding.datatypes.integer, scope=virtualGiftCardType))
virtualGiftCardType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(virtualGiftCardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountNumberLength')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(virtualGiftCardType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardBin')), min_occurs=0L, max_occurs=1)
    )
virtualGiftCardType._ContentModel = pyxb.binding.content.ParticleModel(virtualGiftCardType._GroupModel, min_occurs=0L, max_occurs=1)



tokenResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), methodOfPaymentTypeEnum, scope=tokenResponseType))

tokenResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponseCode'), responseType, scope=tokenResponseType))

tokenResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bin'), pyxb.binding.datatypes.string, scope=tokenResponseType))

tokenResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eCheckAccountSuffix'), pyxb.binding.datatypes.string, scope=tokenResponseType))

tokenResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), ccAccountNumberType, scope=tokenResponseType))

tokenResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenMessage'), pyxb.binding.datatypes.string, scope=tokenResponseType))
tokenResponseType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(tokenResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(tokenResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponseCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(tokenResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenMessage')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(tokenResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(tokenResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bin')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(tokenResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eCheckAccountSuffix')), min_occurs=0L, max_occurs=1)
    )
tokenResponseType._ContentModel = pyxb.binding.content.ParticleModel(tokenResponseType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), nameType, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'planCode'), string25Type, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trialNumberOfIntervals'), numberOfPaymentsType, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'intervalType'), intervalTypeEnum, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numberOfPayments'), numberOfPaymentsType, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trialIntervalType'), trialIntervalTypeEnum, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), nameType, scope=CTD_ANON_22))
CTD_ANON_22._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'planCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'intervalType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numberOfPayments')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trialNumberOfIntervals')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trialIntervalType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_22._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_22._GroupModel, min_occurs=0L, max_occurs=1)



contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'email'), STD_ANON_8, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressLine1'), addressLineType, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstName'), firstNameType, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), stateType, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'middleInitial'), middleInitialType, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phone'), phoneType, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zip'), zipType, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'companyName'), companyName, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressLine2'), addressLineType, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressLine3'), addressLineType, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), countryTypeEnum, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), nameType, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), cityType, scope=contact))

contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lastName'), lastNameType, scope=contact))
contact._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'middleInitial')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lastName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'companyName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressLine1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressLine2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressLine3')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zip')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'email')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phone')), min_occurs=0L, max_occurs=1)
    )
contact._ContentModel = pyxb.binding.content.ParticleModel(contact._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'password'), string20Type, scope=CTD_ANON_23))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'user'), string20Type, scope=CTD_ANON_23))
CTD_ANON_23._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'user')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'password')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_23._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_23._GroupModel, min_occurs=0L, max_occurs=1)



mposType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'encryptedTrack'), encryptedTrackType, scope=mposType))

mposType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ksn'), ksnType, scope=mposType))

mposType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'track2Status'), trackStatusType, scope=mposType))

mposType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'track1Status'), trackStatusType, scope=mposType))

mposType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'formatId'), formatIdType, scope=mposType))
mposType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(mposType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ksn')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(mposType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'formatId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(mposType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'encryptedTrack')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(mposType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'track1Status')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(mposType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'track2Status')), min_occurs=0L, max_occurs=1)
    )
mposType._ContentModel = pyxb.binding.content.ParticleModel(mposType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'quantity'), quantityType, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lineItemTotalWithTax'), transactionAmountType, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'itemDescription'), itemDescriptionType, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'itemSequenceNumber'), itemSequenceNumberType, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'itemDiscountAmount'), transactionAmountType, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxAmount'), transactionAmountType, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lineItemTotal'), transactionAmountType, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'commodityCode'), commodityCodeType, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'detailTax'), CTD_ANON_41, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unitOfMeasure'), unitOfMeasureType, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'productCode'), productCodeType, scope=CTD_ANON_24))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unitCost'), unitCostType, scope=CTD_ANON_24))
CTD_ANON_24._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'itemSequenceNumber')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'itemDescription')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'productCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'quantity')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'unitOfMeasure')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lineItemTotal')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lineItemTotalWithTax')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'itemDiscountAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'commodityCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'unitCost')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'detailTax')), min_occurs=0L, max_occurs=6L)
    )
CTD_ANON_24._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_24._GroupModel, min_occurs=0L, max_occurs=1)



accountInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'number'), ccAccountNumberType, scope=accountInfoType))

accountInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), methodOfPaymentTypeEnum, scope=accountInfoType))
accountInfoType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(accountInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(accountInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'number')), min_occurs=0L, max_occurs=1)
    )
accountInfoType._ContentModel = pyxb.binding.content.ParticleModel(accountInfoType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_25))
CTD_ANON_25._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_25._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_25._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_26))
CTD_ANON_26._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_26._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_26._GroupModel, min_occurs=0L, max_occurs=1)



recyclingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recycleEngineActive'), pyxb.binding.datatypes.boolean, scope=recyclingType))

recyclingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recycleAdvice'), recycleAdviceType, scope=recyclingType))
recyclingType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(recyclingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recycleAdvice')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recyclingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recycleEngineActive')), min_occurs=0L, max_occurs=1)
    )
recyclingType._ContentModel = pyxb.binding.content.ParticleModel(recyclingType._GroupModel, min_occurs=0L, max_occurs=1)



recurringResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringTxnId'), litleIdType, scope=recurringResponseType))

recurringResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseMessage'), messageType, scope=recurringResponseType))

recurringResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), litleIdType, scope=recurringResponseType))

recurringResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseCode'), responseType, scope=recurringResponseType))
recurringResponseType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(recurringResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recurringResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recurringResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseMessage')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recurringResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringTxnId')), min_occurs=0L, max_occurs=1)
    )
recurringResponseType._ContentModel = pyxb.binding.content.ParticleModel(recurringResponseType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), tokenResponseType, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_27))
CTD_ANON_27._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_27._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_27._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedCard'), cardType, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updatedToken'), cardTokenTypeAU, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originalCard'), cardType, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originalToken'), cardTokenTypeAU, scope=CTD_ANON_28))
CTD_ANON_28._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedCard')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originalCard')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updatedToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originalToken')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_28._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_28._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleSessionId'), litleIdType, scope=CTD_ANON_29))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdateFileRequestData'), CTD_ANON_20, scope=CTD_ANON_29))
CTD_ANON_29._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleSessionId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUpdateFileRequestData')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_29._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_29._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IIASFlag'), IIASFlagType, scope=CTD_ANON_30))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'healthcareAmounts'), CTD_ANON_31, scope=CTD_ANON_30))
CTD_ANON_30._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'healthcareAmounts')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IIASFlag')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_30._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_30._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dentalAmount'), transactionAmountType, scope=CTD_ANON_31))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'visionAmount'), transactionAmountType, scope=CTD_ANON_31))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RxAmount'), transactionAmountType, scope=CTD_ANON_31))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'totalHealthcareAmount'), transactionAmountType, scope=CTD_ANON_31))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'clinicOtherAmount'), transactionAmountType, scope=CTD_ANON_31))
CTD_ANON_31._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'totalHealthcareAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RxAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'visionAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'clinicOtherAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dentalAmount')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_31._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_31._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualAccountNumber'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_32))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardProductType'), cardProductTypeEnum, scope=CTD_ANON_32))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'affluence'), affluenceTypeEnum, scope=CTD_ANON_32))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'issuerCountry'), string3Type, scope=CTD_ANON_32))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fundingSource'), CTD_ANON_50, scope=CTD_ANON_32))
CTD_ANON_32._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fundingSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'affluence')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'issuerCountry')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardProductType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualAccountNumber')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_32._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_32._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), contact, scope=CTD_ANON_34))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), merchantDataType, scope=CTD_ANON_34))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_34))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_34))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_34))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_34))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_34))
CTD_ANON_34._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantData')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_34._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_34._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transactionResponse'), transactionTypeWithReportGroup, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_35))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringTransactionResponse'), recurringTransactionResponseType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_35))
CTD_ANON_35._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transactionResponse')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringTransactionResponse')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_35._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_35._GroupModel, min_occurs=0L, max_occurs=1)



echeckTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'checkNum'), checkNumberType, scope=echeckTokenType))

echeckTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accType'), echeckAccountTypeEnum, scope=echeckTokenType))

echeckTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), ccAccountNumberType, scope=echeckTokenType))

echeckTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'routingNum'), routingNumberType, scope=echeckTokenType))
echeckTokenType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(echeckTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'routingNum')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'checkNum')), min_occurs=0L, max_occurs=1L)
    )
echeckTokenType._ContentModel = pyxb.binding.content.ParticleModel(echeckTokenType._GroupModel, min_occurs=0L, max_occurs=1)



recyclingRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recycleId'), string25Type, scope=recyclingRequestType))

recyclingRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recycleBy'), recycleByTypeEnum, scope=recyclingRequestType))
recyclingRequestType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(recyclingRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recycleBy')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recyclingRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recycleId')), min_occurs=0L, max_occurs=1)
    )
recyclingRequestType._ContentModel = pyxb.binding.content.ParticleModel(recyclingRequestType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'residenceStatus'), STD_ANON_5, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerType'), STD_ANON_4, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerCheckingAccount'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerSavingAccount'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'yearsAtResidence'), STD_ANON_9, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'incomeCurrency'), currencyCodeEnum, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerWorkTelephone'), phoneType, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'employerName'), string20Type, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dob'), pyxb.binding.datatypes.date, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ssn'), STD_ANON_2, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'yearsAtEmployer'), STD_ANON_11, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerRegistrationDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_36))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'incomeAmount'), pyxb.binding.datatypes.long, scope=CTD_ANON_36))
CTD_ANON_36._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ssn')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dob')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerRegistrationDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'incomeAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'incomeCurrency')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerCheckingAccount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerSavingAccount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'employerName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerWorkTelephone')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'residenceStatus')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'yearsAtResidence')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'yearsAtEmployer')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_36._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_36._GroupModel, min_occurs=0L, max_occurs=1)



extendedCardResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), responseType, scope=extendedCardResponseType))

extendedCardResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=extendedCardResponseType))
extendedCardResponseType._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(extendedCardResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(extendedCardResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code')), min_occurs=0L, max_occurs=1)
    )
extendedCardResponseType._ContentModel = pyxb.binding.content.ParticleModel(extendedCardResponseType._GroupModel, min_occurs=0L, max_occurs=1)



recurringRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subscription'), recurringSubscriptionType, scope=recurringRequestType))
recurringRequestType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(recurringRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subscription')), min_occurs=0L, max_occurs=1)
    )
recurringRequestType._ContentModel = pyxb.binding.content.ParticleModel(recurringRequestType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudResults'), advancedFraudResultsType, scope=CTD_ANON_37))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardValidationResult'), pyxb.binding.datatypes.string, scope=CTD_ANON_37))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'avsResult'), string2Type, scope=CTD_ANON_37))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authenticationResult'), authenticationResultType, scope=CTD_ANON_37))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'advancedAVSResult'), string3Type, scope=CTD_ANON_37))
CTD_ANON_37._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'avsResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardValidationResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authenticationResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'advancedAVSResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudResults')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_37._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_37._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sellerMerchantCategoryCode'), merchantCategoryCodeType, scope=CTD_ANON_38))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sellerId'), sellerIdType, scope=CTD_ANON_38))
CTD_ANON_38._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sellerId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sellerMerchantCategoryCode')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_38._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_38._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eCheckAccountSuffix'), pyxb.binding.datatypes.string, scope=CTD_ANON_39))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_39))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_39))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), ccAccountNumberType, scope=CTD_ANON_39))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_39))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bin'), pyxb.binding.datatypes.string, scope=CTD_ANON_39))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, scope=CTD_ANON_39))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), methodOfPaymentTypeEnum, scope=CTD_ANON_39))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_39))
CTD_ANON_39._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bin')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eCheckAccountSuffix')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_39._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_39._GroupModel, min_occurs=0L, max_occurs=1)



advancedFraudChecksType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'threatMetrixSessionId'), threatMetrixSessionIdType, scope=advancedFraudChecksType))
advancedFraudChecksType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(advancedFraudChecksType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'threatMetrixSessionId')), min_occurs=0L, max_occurs=1)
    )
advancedFraudChecksType._ContentModel = pyxb.binding.content.ParticleModel(advancedFraudChecksType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), merchantDataType, scope=CTD_ANON_40))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_40))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_40))
CTD_ANON_40._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantData')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_40._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_40._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxTypeIdentifier'), taxTypeIdentifierEnum, scope=CTD_ANON_41))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxAmount'), transactionAmountType, scope=CTD_ANON_41))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxIncludedInTotal'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_41))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxRate'), taxRateType, scope=CTD_ANON_41))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardAcceptorTaxId'), cardAcceptorTaxIdType, scope=CTD_ANON_41))
CTD_ANON_41._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxIncludedInTotal')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxRate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxTypeIdentifier')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardAcceptorTaxId')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_41._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_41._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billingDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), contact, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypage'), cardPaypageType, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updateAddOn'), updateAddOnType, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'token'), cardTokenType, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'createDiscount'), createDiscountType, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), litleIdType, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updateDiscount'), updateDiscountType, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'planCode'), string25Type, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'deleteAddOn'), deleteAddOnType, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'deleteDiscount'), deleteDiscountType, scope=CTD_ANON_42))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'createAddOn'), createAddOnType, scope=CTD_ANON_42))
CTD_ANON_42._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'token')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypage')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_42._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'planCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billingDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'createDiscount')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updateDiscount')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'deleteDiscount')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'createAddOn')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updateAddOn')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'deleteAddOn')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_42._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_42._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_43))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_43))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_43))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), CTD_ANON_16, scope=CTD_ANON_43))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), merchantDataType, scope=CTD_ANON_43))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), contact, scope=CTD_ANON_43))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_43))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_43))
CTD_ANON_43._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customBilling')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_43._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customBilling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantData')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_43._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_43._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_43._GroupModel_3, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_43._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_43._GroupModel_, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_43._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_43._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_44))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), tokenResponseType, scope=CTD_ANON_44))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_44))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_44))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_44))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_44))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), CTD_ANON_4, scope=CTD_ANON_44))
CTD_ANON_44._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_44._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_44._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bmlMerchantId'), litleIdType, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerPhoneChanged'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerPasswordChanged'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'secretQuestionCode'), string2Type, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualAuthenticationKeyPresenceIndicator'), virtualAuthenticationKeyPresenceIndicator, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerBillingAddressChanged'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerEmailChanged'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'preapprovalNumber'), ccAccountNumberType, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'termsAndConditions'), STD_ANON_7, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'itemCategoryCode'), STD_ANON, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authorizationSourcePlatform'), pyxb.binding.datatypes.string, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'secretQuestionAnswer'), string25Type, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantPromotionalCode'), STD_ANON_6, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bmlProductType'), STD_ANON_, scope=CTD_ANON_45))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualAuthenticationKeyData'), virtualAuthenticationKeyData, scope=CTD_ANON_45))
CTD_ANON_45._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bmlMerchantId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bmlProductType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'termsAndConditions')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'preapprovalNumber')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantPromotionalCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerPasswordChanged')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerBillingAddressChanged')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerEmailChanged')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerPhoneChanged')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'secretQuestionCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'secretQuestionAnswer')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualAuthenticationKeyPresenceIndicator')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualAuthenticationKeyData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'itemCategoryCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authorizationSourcePlatform')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_45._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_45._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), pyxb.binding.datatypes.string, scope=CTD_ANON_46))

CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountNumber'), ccAccountNumberType, scope=CTD_ANON_46))
CTD_ANON_46._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountNumber')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_46._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_46._GroupModel, min_occurs=0L, max_occurs=1)



echeckAccountInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'routingNum'), routingNumberType, scope=echeckAccountInfoType))

echeckAccountInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accNum'), echeckAccountNumberType, scope=echeckAccountInfoType))

echeckAccountInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accType'), echeckAccountTypeEnum, scope=echeckAccountInfoType))
echeckAccountInfoType._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(echeckAccountInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckAccountInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accNum')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckAccountInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'routingNum')), min_occurs=0L, max_occurs=1)
    )
echeckAccountInfoType._ContentModel = pyxb.binding.content.ParticleModel(echeckAccountInfoType._GroupModel, min_occurs=0L, max_occurs=1)



cardPaypageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypageRegistrationId'), string512Type, scope=cardPaypageType))

cardPaypageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), methodOfPaymentTypeEnum, scope=cardPaypageType))

cardPaypageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expDate'), expDateType, scope=cardPaypageType))

cardPaypageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), cvNumType, scope=cardPaypageType))
cardPaypageType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(cardPaypageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypageRegistrationId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardPaypageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardPaypageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardPaypageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), min_occurs=0L, max_occurs=1)
    )
cardPaypageType._ContentModel = pyxb.binding.content.ParticleModel(cardPaypageType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payerId'), STD_ANON_13, scope=CTD_ANON_47))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payerEmail'), STD_ANON_12, scope=CTD_ANON_47))
CTD_ANON_47._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payerId')), min_occurs=1L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payerEmail')), min_occurs=1L, max_occurs=1)
    )
CTD_ANON_47._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_47._GroupModel, min_occurs=0L, max_occurs=1)



merchantDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantGroupingId'), merchantGroupingIdType, scope=merchantDataType))

merchantDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'affiliate'), affiliateType, scope=merchantDataType))

merchantDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'campaign'), campaignType, scope=merchantDataType))
merchantDataType._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(merchantDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'campaign')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(merchantDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'affiliate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(merchantDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantGroupingId')), min_occurs=0L, max_occurs=1)
    )
merchantDataType._ContentModel = pyxb.binding.content.ParticleModel(merchantDataType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_48))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_48))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_48))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_48))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_48))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_48))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_48))
CTD_ANON_48._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_48._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_48._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_49))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_49))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_49))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), CTD_ANON_4, scope=CTD_ANON_49))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_49))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_49))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_49))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_49))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_49))
CTD_ANON_49._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_49._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_49._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'prepaidCardType'), string50Type, scope=CTD_ANON_50))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), fundingSourceTypeEnum, scope=CTD_ANON_50))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'availableBalance'), string20Type, scope=CTD_ANON_50))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reloadable'), string50Type, scope=CTD_ANON_50))
CTD_ANON_50._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'availableBalance')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reloadable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'prepaidCardType')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_50._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_50._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_51))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), CTD_ANON_15, scope=CTD_ANON_51))
CTD_ANON_51._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_51._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_51._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_52))

CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_52))

CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_52))

CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_52))

CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_52))

CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_52))

CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_52))

CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_52))
CTD_ANON_52._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_52._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_52._GroupModel, min_occurs=0L, max_occurs=1)



filteringType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'chargeback'), pyxb.binding.datatypes.boolean, scope=filteringType))

filteringType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'prepaid'), pyxb.binding.datatypes.boolean, scope=filteringType))

filteringType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'international'), pyxb.binding.datatypes.boolean, scope=filteringType))
filteringType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(filteringType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'prepaid')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(filteringType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'international')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(filteringType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'chargeback')), min_occurs=0L, max_occurs=1)
    )
filteringType._ContentModel = pyxb.binding.content.ParticleModel(filteringType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_53))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_53))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recycling'), voidRecyclingResponseType, scope=CTD_ANON_53))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_53))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_53))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_53))
CTD_ANON_53._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recycling')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_53._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_53._GroupModel, min_occurs=0L, max_occurs=1)



cardAccountInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expDate'), expDateType, scope=cardAccountInfoType))

cardAccountInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'number'), ccAccountNumberType, scope=cardAccountInfoType))

cardAccountInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), methodOfPaymentTypeEnum, scope=cardAccountInfoType))
cardAccountInfoType._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(cardAccountInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardAccountInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'number')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardAccountInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expDate')), min_occurs=0L, max_occurs=1)
    )
cardAccountInfoType._ContentModel = pyxb.binding.content.ParticleModel(cardAccountInfoType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_54))
CTD_ANON_54._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_54._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_54._GroupModel, min_occurs=0L, max_occurs=1)



cardTokenInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expDate'), expDateType, scope=cardTokenInfoType))

cardTokenInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), methodOfPaymentTypeEnum, scope=cardTokenInfoType))

cardTokenInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bin'), pyxb.binding.datatypes.string, scope=cardTokenInfoType))

cardTokenInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), ccAccountNumberType, scope=cardTokenInfoType))
cardTokenInfoType._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(cardTokenInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardTokenInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardTokenInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(cardTokenInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bin')), min_occurs=0L, max_occurs=1)
    )
cardTokenInfoType._ContentModel = pyxb.binding.content.ParticleModel(cardTokenInfoType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_55))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_55))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_55))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), tokenResponseType, scope=CTD_ANON_55))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_55))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_55))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_55))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_55))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_55))
CTD_ANON_55._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_55._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_55._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transactionResponse'), transactionTypeWithReportGroup, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_56))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringTransactionResponse'), recurringTransactionResponseType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_56))
CTD_ANON_56._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transactionResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringTransactionResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_56._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_56._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), merchantDataType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), CTD_ANON_38, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recyclingRequest'), recyclingRequestType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudFilterOverride'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'healthcareIIAS'), CTD_ANON_30, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), contact, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringRequest'), recurringRequestType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), CTD_ANON_13, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'allowPartialAuth'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest'), CTD_ANON_45, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudChecks'), advancedFraudChecksType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerInfo'), CTD_ANON_36, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), CTD_ANON_16, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'token'), cardTokenType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypage'), cardPaypageType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mpos'), mposType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), CTD_ANON_15, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardholderAuthentication'), fraudCheckType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress'), contact, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal'), payPal, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxType'), govtTaxTypeEnum, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), transactionAmountType, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pos'), CTD_ANON_2, scope=CTD_ANON_57))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'filtering'), filteringType, scope=CTD_ANON_57))
CTD_ANON_57._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_57._GroupModel_3 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mpos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypal')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'token')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypage')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_57._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerInfo')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._GroupModel_3, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardholderAuthentication')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pos')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customBilling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enhancedData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'allowPartialAuth')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'healthcareIIAS')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'filtering')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recyclingRequest')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudFilterOverride')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringRequest')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudChecks')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_57._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_57._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_57._GroupModel_2, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_57._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_57._GroupModel, min_occurs=1, max_occurs=1)



createDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'discountCode'), string25Type, scope=createDiscountType))

createDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=createDiscountType))

createDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endDate'), pyxb.binding.datatypes.date, scope=createDiscountType))

createDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startDate'), pyxb.binding.datatypes.date, scope=createDiscountType))

createDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), nameType, scope=createDiscountType))
createDiscountType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(createDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'discountCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(createDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(createDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(createDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'startDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(createDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'endDate')), min_occurs=0L, max_occurs=1)
    )
createDiscountType._ContentModel = pyxb.binding.content.ParticleModel(createDiscountType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_58))

CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_58))

CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_58))

CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_58))

CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_58))
CTD_ANON_58._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_58._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_58._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes'), payPalNotesType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress'), contact, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), CTD_ANON_13, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal'), payPal, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mpos'), mposType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'allowPartialAuth'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest'), CTD_ANON_45, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), merchantDataType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recyclingRequest'), recyclingRequestType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'filtering'), filteringType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), CTD_ANON_15, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudFilterOverride'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), CTD_ANON_16, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringRequest'), recurringRequestType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), contact, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'token'), cardTokenType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleInternalRecurringRequest'), litleInternalRecurringRequestType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), CTD_ANON_38, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudCheck'), fraudCheckType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudChecks'), advancedFraudChecksType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), transactionAmountType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardholderAuthentication'), fraudCheckType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'healthcareIIAS'), CTD_ANON_30, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxType'), govtTaxTypeEnum, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerInfo'), CTD_ANON_36, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pos'), CTD_ANON_2, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypage'), cardPaypageType, scope=CTD_ANON_59))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payPalOrderComplete'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_59))
CTD_ANON_59._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mpos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypal')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'token')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypage')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_59._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudCheck')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardholderAuthentication')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_59._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerInfo')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._GroupModel_2, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customBilling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enhancedData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pos')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payPalOrderComplete')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'allowPartialAuth')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'healthcareIIAS')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'filtering')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recyclingRequest')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudFilterOverride')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringRequest')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleInternalRecurringRequest')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudChecks')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_59._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_59._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_60))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_60))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_60))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_60))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_60))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_60))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_60))
CTD_ANON_60._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_60._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_60._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), CTD_ANON_4, scope=CTD_ANON_61))

CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_61))

CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), tokenResponseType, scope=CTD_ANON_61))

CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_61))

CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_61))

CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_61))

CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_61))

CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_61))

CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_61))

CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_61))
CTD_ANON_61._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_61._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_61._GroupModel, min_occurs=0L, max_occurs=1)



payPal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transactionId'), pyxb.binding.datatypes.string, scope=payPal))

payPal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payerId'), pyxb.binding.datatypes.string, scope=payPal))

payPal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'token'), pyxb.binding.datatypes.string, scope=payPal))
payPal._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(payPal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payerId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(payPal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'token')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(payPal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transactionId')), min_occurs=0L, max_occurs=1)
    )
payPal._ContentModel = pyxb.binding.content.ParticleModel(payPal._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_62))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_62))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_62))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_62))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_62))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_62))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_62))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'approvedAmount'), transactionAmountType, scope=CTD_ANON_62))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_62))
CTD_ANON_62._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'approvedAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_62._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_62._GroupModel, min_occurs=0L, max_occurs=1)



fraudCheckType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authenticatedByMerchant'), pyxb.binding.datatypes.boolean, scope=fraudCheckType))

fraudCheckType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authenticationTransactionId'), authenticationTransactionIdType, scope=fraudCheckType))

fraudCheckType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authenticationValue'), authenticationValueType, scope=fraudCheckType))

fraudCheckType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerIpAddress'), ipAddress, scope=fraudCheckType))
fraudCheckType._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(fraudCheckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authenticationValue')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(fraudCheckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authenticationTransactionId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(fraudCheckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerIpAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(fraudCheckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authenticatedByMerchant')), min_occurs=0L, max_occurs=1)
    )
fraudCheckType._ContentModel = pyxb.binding.content.ParticleModel(fraudCheckType._GroupModel, min_occurs=0L, max_occurs=1)



updateDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endDate'), pyxb.binding.datatypes.date, scope=updateDiscountType))

updateDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), nameType, scope=updateDiscountType))

updateDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=updateDiscountType))

updateDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startDate'), pyxb.binding.datatypes.date, scope=updateDiscountType))

updateDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'discountCode'), string25Type, scope=updateDiscountType))
updateDiscountType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(updateDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'discountCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(updateDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(updateDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(updateDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'startDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(updateDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'endDate')), min_occurs=0L, max_occurs=1)
    )
updateDiscountType._ContentModel = pyxb.binding.content.ParticleModel(updateDiscountType._GroupModel, min_occurs=0L, max_occurs=1)



echeckType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accType'), echeckAccountTypeEnum, scope=echeckType))

echeckType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'checkNum'), checkNumberType, scope=echeckType))

echeckType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accNum'), echeckAccountNumberType, scope=echeckType))

echeckType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'routingNum'), routingNumberType, scope=echeckType))
echeckType._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(echeckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accNum')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'routingNum')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'checkNum')), min_occurs=0L, max_occurs=1)
    )
echeckType._ContentModel = pyxb.binding.content.ParticleModel(echeckType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_63))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_63))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_63))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_63))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_63))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_63))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_63))
CTD_ANON_63._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_63._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_63._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_64._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_64))
CTD_ANON_64._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_64._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_64._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_64._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_65._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudChecks'), advancedFraudChecksType, scope=CTD_ANON_65))
CTD_ANON_65._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_65._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudChecks')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_65._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_65._GroupModel, min_occurs=0L, max_occurs=1)



driversLicenseInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth'), dateOfBirthType, scope=driversLicenseInfo))

driversLicenseInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'licenseNumber'), driversLicenseType, scope=driversLicenseInfo))

driversLicenseInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), stateCodeType, scope=driversLicenseInfo))
driversLicenseInfo._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(driversLicenseInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'licenseNumber')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(driversLicenseInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(driversLicenseInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth')), min_occurs=0L, max_occurs=1)
    )
driversLicenseInfo._ContentModel = pyxb.binding.content.ParticleModel(driversLicenseInfo._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_66))

CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_66))

CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_66))

CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_66))

CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_66))

CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_66))

CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_66))
CTD_ANON_66._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_66._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_66._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recycling'), recyclingType, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authCode'), authCodeType, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), CTD_ANON_4, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringResponse'), recurringResponseType, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), tokenResponseType, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardProductId'), pyxb.binding.datatypes.string, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'approvedAmount'), transactionAmountType, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enhancedAuthResponse'), CTD_ANON_32, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authorizationResponseSubCode'), pyxb.binding.datatypes.string, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterResponseData'), CTD_ANON_, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_67))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountInformation'), accountInfoType, scope=CTD_ANON_67))
CTD_ANON_67._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardProductId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authorizationResponseSubCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'approvedAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountInformation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterResponseData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enhancedAuthResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recycling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_67._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_67._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_68._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_68))

CTD_ANON_68._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_68))

CTD_ANON_68._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_68))

CTD_ANON_68._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_68))

CTD_ANON_68._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_68))

CTD_ANON_68._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_68))

CTD_ANON_68._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_68))

CTD_ANON_68._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_68))
CTD_ANON_68._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_68._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_68._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_68._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_68._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_68._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_68._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_68._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_68._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_68._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_68._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_69._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_69))

CTD_ANON_69._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authAmount'), transactionAmountType, scope=CTD_ANON_69))

CTD_ANON_69._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_69))

CTD_ANON_69._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authCode'), authCodeType, scope=CTD_ANON_69))
CTD_ANON_69._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_69._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_69._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_69._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_69._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authAmount')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_69._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_69._GroupModel, min_occurs=0L, max_occurs=1)



recycleAdviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nextRecycleTime'), pyxb.binding.datatypes.dateTime, scope=recycleAdviceType))

recycleAdviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recycleAdviceEnd'), string20Type, scope=recycleAdviceType))
recycleAdviceType._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(recycleAdviceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nextRecycleTime')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(recycleAdviceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recycleAdviceEnd')), min_occurs=1, max_occurs=1)
    )
recycleAdviceType._ContentModel = pyxb.binding.content.ParticleModel(recycleAdviceType._GroupModel, min_occurs=0L, max_occurs=1)



litleInternalRecurringRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'finalPayment'), pyxb.binding.datatypes.boolean, scope=litleInternalRecurringRequestType))

litleInternalRecurringRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringTxnId'), litleIdType, scope=litleInternalRecurringRequestType))

litleInternalRecurringRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), litleIdType, scope=litleInternalRecurringRequestType))
litleInternalRecurringRequestType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(litleInternalRecurringRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(litleInternalRecurringRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringTxnId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(litleInternalRecurringRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'finalPayment')), min_occurs=0L, max_occurs=1)
    )
litleInternalRecurringRequestType._ContentModel = pyxb.binding.content.ParticleModel(litleInternalRecurringRequestType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardOrToken'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_70))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_70))
CTD_ANON_70._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardOrToken')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_70._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_70._GroupModel, min_occurs=0L, max_occurs=1)



registerTokenRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypageRegistrationId'), string512Type, scope=registerTokenRequestType))

registerTokenRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckForToken'), echeckForTokenType, scope=registerTokenRequestType))

registerTokenRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=registerTokenRequestType))

registerTokenRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountNumber'), ccAccountNumberType, scope=registerTokenRequestType))

registerTokenRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum'), cvNumType, scope=registerTokenRequestType))
registerTokenRequestType._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(registerTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(registerTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'echeckForToken')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(registerTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypageRegistrationId')), min_occurs=1, max_occurs=1)
    )
registerTokenRequestType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(registerTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(registerTokenRequestType._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(registerTokenRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardValidationNum')), min_occurs=0L, max_occurs=1)
    )
registerTokenRequestType._ContentModel = pyxb.binding.content.ParticleModel(registerTokenRequestType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enhancedAuthResponse'), CTD_ANON_32, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), tokenResponseType, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authCode'), authCodeType, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), CTD_ANON_4, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountInformation'), accountInfoType, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authorizationResponseSubCode'), pyxb.binding.datatypes.string, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringResponse'), recurringResponseType, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recycling'), recyclingType, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardProductId'), pyxb.binding.datatypes.string, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterResponseData'), CTD_ANON_, scope=CTD_ANON_71))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'approvedAmount'), transactionAmountType, scope=CTD_ANON_71))
CTD_ANON_71._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardProductId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authorizationResponseSubCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'approvedAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountInformation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterResponseData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enhancedAuthResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recycling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_71._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_71._GroupModel, min_occurs=0L, max_occurs=1)



echeckTokenInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'routingNum'), routingNumberType, scope=echeckTokenInfoType))

echeckTokenInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accType'), echeckAccountTypeEnum, scope=echeckTokenInfoType))

echeckTokenInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleToken'), ccAccountNumberType, scope=echeckTokenInfoType))
echeckTokenInfoType._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(echeckTokenInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckTokenInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckTokenInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'routingNum')), min_occurs=0L, max_occurs=1)
    )
echeckTokenInfoType._ContentModel = pyxb.binding.content.ParticleModel(echeckTokenInfoType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_72._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_72))

CTD_ANON_72._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, scope=CTD_ANON_72))

CTD_ANON_72._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_72))

CTD_ANON_72._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_72))

CTD_ANON_72._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_72))
CTD_ANON_72._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_72._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_72._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_72._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_72._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_72._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_72._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_72._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'actionReason'), actionReasonType, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), CTD_ANON_16, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypage'), cardPaypageType, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), merchantDataType, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest'), CTD_ANON_45, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), CTD_ANON_38, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), contact, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal'), payPal, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pos'), CTD_ANON_2, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), transactionAmountType, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), CTD_ANON_13, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), CTD_ANON_15, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxType'), govtTaxTypeEnum, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'token'), cardTokenType, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mpos'), mposType, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes'), payPalNotesType, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_73))

CTD_ANON_73._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_73))
CTD_ANON_73._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customBilling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enhancedData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pos')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_73._GroupModel_4 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mpos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'token')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypage')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypal')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_73._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._GroupModel_4, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customBilling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enhancedData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pos')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantData')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_73._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_73._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._GroupModel_3, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_73._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_73._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'actionReason')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_73._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_73._GroupModel, min_occurs=0L, max_occurs=1)



advancedFraudResultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'deviceReviewStatus'), pyxb.binding.datatypes.string, scope=advancedFraudResultsType))

advancedFraudResultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'deviceReputationScore'), pyxb.binding.datatypes.int, scope=advancedFraudResultsType))

advancedFraudResultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'triggeredRule'), pyxb.binding.datatypes.string, scope=advancedFraudResultsType))
advancedFraudResultsType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(advancedFraudResultsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'deviceReviewStatus')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(advancedFraudResultsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'deviceReputationScore')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(advancedFraudResultsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'triggeredRule')), min_occurs=0L, max_occurs=None)
    )
advancedFraudResultsType._ContentModel = pyxb.binding.content.ParticleModel(advancedFraudResultsType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_74._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_74))

CTD_ANON_74._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_74))

CTD_ANON_74._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_74))

CTD_ANON_74._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_74))

CTD_ANON_74._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_74))

CTD_ANON_74._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_74))

CTD_ANON_74._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_74))
CTD_ANON_74._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_74._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_74._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_74._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_74._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_74._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_74._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_74._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_74._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_74._GroupModel, min_occurs=0L, max_occurs=1)



recurringSubscriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=recurringSubscriptionType))

recurringSubscriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'planCode'), string25Type, scope=recurringSubscriptionType))

recurringSubscriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'createDiscount'), createDiscountType, scope=recurringSubscriptionType))

recurringSubscriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numberOfPayments'), numberOfPaymentsType, scope=recurringSubscriptionType))

recurringSubscriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'createAddOn'), createAddOnType, scope=recurringSubscriptionType))

recurringSubscriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startDate'), pyxb.binding.datatypes.date, scope=recurringSubscriptionType))
recurringSubscriptionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(recurringSubscriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'planCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recurringSubscriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numberOfPayments')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recurringSubscriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'startDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recurringSubscriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(recurringSubscriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'createDiscount')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(recurringSubscriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'createAddOn')), min_occurs=0L, max_occurs=None)
    )
recurringSubscriptionType._ContentModel = pyxb.binding.content.ParticleModel(recurringSubscriptionType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), pyxb.binding.datatypes.string, scope=CTD_ANON_75))

CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_75))

CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_75))

CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudResults'), advancedFraudResultsType, scope=CTD_ANON_75))

CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_75))
CTD_ANON_75._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'advancedFraudResults')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_75._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_75._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_76._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_76))

CTD_ANON_76._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes'), payPalNotesType, scope=CTD_ANON_76))

CTD_ANON_76._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'actionReason'), actionReasonType, scope=CTD_ANON_76))

CTD_ANON_76._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), transactionAmountType, scope=CTD_ANON_76))

CTD_ANON_76._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_76))
CTD_ANON_76._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'actionReason')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_76._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_76._GroupModel, min_occurs=0L, max_occurs=1)



baseRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recurringTransaction'), recurringTransactionType, abstract=pyxb.binding.datatypes.boolean(1), scope=baseRequest))

baseRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transaction'), transactionType, abstract=pyxb.binding.datatypes.boolean(1), scope=baseRequest))

baseRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authentication'), CTD_ANON_23, scope=baseRequest))
baseRequest._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(baseRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transaction')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringTransaction')), min_occurs=1, max_occurs=1)
    )
baseRequest._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(baseRequest._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authentication')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(baseRequest._GroupModel_, min_occurs=0L, max_occurs=1)
    )
baseRequest._ContentModel = pyxb.binding.content.ParticleModel(baseRequest._GroupModel, min_occurs=0L, max_occurs=1)


CTD_ANON_77._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_77._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transaction')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_77._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recurringTransaction')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_77._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_77._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authentication')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_77._GroupModel_, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_77._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_77._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_78._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_78))

CTD_ANON_78._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_78))

CTD_ANON_78._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_78))

CTD_ANON_78._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_78))
CTD_ANON_78._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_78._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_78._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payPalOrderComplete'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_79))

CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_79))

CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes'), payPalNotesType, scope=CTD_ANON_79))

CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), CTD_ANON_13, scope=CTD_ANON_79))

CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), transactionAmountType, scope=CTD_ANON_79))

CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), CTD_ANON_15, scope=CTD_ANON_79))

CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_79))
CTD_ANON_79._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enhancedData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payPalOrderComplete')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payPalNotes')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_79._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_79._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxType'), govtTaxTypeEnum, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypage'), cardPaypageType, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), contact, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), merchantDataType, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mpos'), mposType, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'token'), cardTokenType, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), CTD_ANON_38, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pos'), CTD_ANON_2, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), CTD_ANON_15, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), CTD_ANON_16, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), CTD_ANON_13, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), transactionAmountType, scope=CTD_ANON_80))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_80))
CTD_ANON_80._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mpos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'token')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypage')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_80._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customBilling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enhancedData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pos')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_80._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_80._GroupModel, min_occurs=0L, max_occurs=1)



deleteDiscountType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'discountCode'), string25Type, scope=deleteDiscountType))
deleteDiscountType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(deleteDiscountType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'discountCode')), min_occurs=0L, max_occurs=1)
    )
deleteDiscountType._ContentModel = pyxb.binding.content.ParticleModel(deleteDiscountType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_81))

CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_81))

CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_81))

CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_81))

CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_81))

CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualGiftCardResponse'), CTD_ANON_46, scope=CTD_ANON_81))

CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_81))

CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_81))

CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_81))
CTD_ANON_81._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualGiftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_81._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_81._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_82))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_82))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'verificationCode'), authCodeType, scope=CTD_ANON_82))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), CTD_ANON_4, scope=CTD_ANON_82))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_82))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_82))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_82))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), tokenResponseType, scope=CTD_ANON_82))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_82))
CTD_ANON_82._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'verificationCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_82._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_82._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_83._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_83))

CTD_ANON_83._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_83))

CTD_ANON_83._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_83))

CTD_ANON_83._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_83))

CTD_ANON_83._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_83))

CTD_ANON_83._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), tokenResponseType, scope=CTD_ANON_83))

CTD_ANON_83._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_83))
CTD_ANON_83._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_83._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_83._GroupModel, min_occurs=0L, max_occurs=1)



echeckForTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'routingNum'), routingNumberType, scope=echeckForTokenType))

echeckForTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accNum'), echeckAccountNumberType, scope=echeckForTokenType))
echeckForTokenType._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(echeckForTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accNum')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(echeckForTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'routingNum')), min_occurs=0L, max_occurs=1)
    )
echeckForTokenType._ContentModel = pyxb.binding.content.ParticleModel(echeckForTokenType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_84._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_84))

CTD_ANON_84._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_84))

CTD_ANON_84._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_84))

CTD_ANON_84._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'virtualGiftCard'), virtualGiftCardType, scope=CTD_ANON_84))

CTD_ANON_84._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_84))
CTD_ANON_84._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_84._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_84._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'virtualGiftCard')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_84._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_84._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_84._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_84._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_84._GroupModel_, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_84._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_84._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_85))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_85))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), contact, scope=CTD_ANON_85))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_85))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'verify'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_85))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_85))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), merchantDataType, scope=CTD_ANON_85))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress'), contact, scope=CTD_ANON_85))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), CTD_ANON_16, scope=CTD_ANON_85))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_85))
CTD_ANON_85._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customBilling')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_85._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'verify')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'echeckOrEcheckToken')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customBilling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantData')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_85._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_85._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_85._GroupModel_2, min_occurs=0L, max_occurs=1)
    )
CTD_ANON_85._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_85._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_86._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_86))

CTD_ANON_86._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse'), tokenResponseType, scope=CTD_ANON_86))

CTD_ANON_86._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_86))

CTD_ANON_86._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_86))

CTD_ANON_86._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater'), CTD_ANON_4, scope=CTD_ANON_86))

CTD_ANON_86._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_86))

CTD_ANON_86._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_86))

CTD_ANON_86._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_86))
CTD_ANON_86._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_86._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_86._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_86._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_86._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_86._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_86._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_86._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountUpdater')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_86._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tokenResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_86._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_86._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_87._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_87))

CTD_ANON_87._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_87))

CTD_ANON_87._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_87))
CTD_ANON_87._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_87._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_87._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_87._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_87._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_87._GroupModel, min_occurs=0L, max_occurs=1)



updateAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'endDate'), pyxb.binding.datatypes.date, scope=updateAddOnType))

updateAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), nameType, scope=updateAddOnType))

updateAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=updateAddOnType))

updateAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addOnCode'), string25Type, scope=updateAddOnType))

updateAddOnType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'startDate'), pyxb.binding.datatypes.date, scope=updateAddOnType))
updateAddOnType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(updateAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addOnCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(updateAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(updateAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(updateAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'startDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(updateAddOnType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'endDate')), min_occurs=0L, max_occurs=1)
    )
updateAddOnType._ContentModel = pyxb.binding.content.ParticleModel(updateAddOnType._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authInformation'), CTD_ANON_69, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypage'), cardPaypageType, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'token'), cardTokenType, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxType'), govtTaxTypeEnum, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantData'), merchantDataType, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest'), CTD_ANON_45, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billToAddress'), contact, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount'), transactionAmountType, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData'), CTD_ANON_38, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enhancedData'), CTD_ANON_13, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress'), contact, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customBilling'), CTD_ANON_16, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions'), CTD_ANON_15, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mpos'), mposType, scope=CTD_ANON_88))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pos'), CTD_ANON_2, scope=CTD_ANON_88))
CTD_ANON_88._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mpos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'token')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypage')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_88._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authInformation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'surchargeAmount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shipToAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customBilling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billMeLaterRequest')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enhancedData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'processingInstructions')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pos')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amexAggregatorData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'debtRepayment')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_88._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_88._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_89._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId'), litleIdType, scope=CTD_ANON_89))
CTD_ANON_89._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_89._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subscriptionId')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_89._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_89._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_90))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_90))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse'), CTD_ANON_7, scope=CTD_ANON_90))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudResult'), CTD_ANON_37, scope=CTD_ANON_90))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), responseType, scope=CTD_ANON_90))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, scope=CTD_ANON_90))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_90))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=CTD_ANON_90))
CTD_ANON_90._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseTime')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'message')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudResult')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'giftCardResponse')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_90._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_90._GroupModel, min_occurs=0L, max_occurs=1)



CTD_ANON_91._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderSource'), orderSourceType, scope=CTD_ANON_91))

CTD_ANON_91._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), transactionAmountType, scope=CTD_ANON_91))

CTD_ANON_91._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card'), cardType, scope=CTD_ANON_91))

CTD_ANON_91._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=CTD_ANON_91))
CTD_ANON_91._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_91._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_91._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_91._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderSource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_91._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_91._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_91._GroupModel, min_occurs=0L, max_occurs=1)

refundReversal._setSubstitutionGroup(transaction)

loadReversal._setSubstitutionGroup(transaction)

updatePlan._setSubstitutionGroup(recurringTransaction)

unloadReversal._setSubstitutionGroup(transaction)

cancelSubscriptionResponse._setSubstitutionGroup(recurringTransactionResponse)

updateSubscriptionResponse._setSubstitutionGroup(recurringTransactionResponse)

balanceInquiry._setSubstitutionGroup(transaction)

createPlanResponse._setSubstitutionGroup(recurringTransactionResponse)

updatePlanResponse._setSubstitutionGroup(recurringTransactionResponse)

activateReversal._setSubstitutionGroup(transaction)

unloadReversalResponse._setSubstitutionGroup(transactionResponse)

updateCardValidationNumOnToken._setSubstitutionGroup(transaction)

createPlan._setSubstitutionGroup(recurringTransaction)

deactivateReversalResponse._setSubstitutionGroup(transactionResponse)

deactivateReversal._setSubstitutionGroup(transaction)

creditResponse._setSubstitutionGroup(transactionResponse)

accountUpdateResponse._setSubstitutionGroup(transactionResponse)

echeckVerification._setSubstitutionGroup(transaction)

echeckToken._setSubstitutionGroup(echeckOrEcheckToken)

registerTokenResponse._setSubstitutionGroup(transactionResponse)

echeckRedeposit._setSubstitutionGroup(transaction)

updateSubscription._setSubstitutionGroup(recurringTransaction)

echeckCredit._setSubstitutionGroup(transaction)

echeckRedepositResponse._setSubstitutionGroup(transactionResponse)

authReversalResponse._setSubstitutionGroup(transactionResponse)

captureResponse._setSubstitutionGroup(transactionResponse)

void._setSubstitutionGroup(transaction)

balanceInquiryResponse._setSubstitutionGroup(transactionResponse)

voidResponse._setSubstitutionGroup(transactionResponse)

echeckVoid._setSubstitutionGroup(transaction)

captureGivenAuthResponse._setSubstitutionGroup(transactionResponse)

authorization._setSubstitutionGroup(transaction)

echeckVoidResponse._setSubstitutionGroup(transactionResponse)

sale._setSubstitutionGroup(transaction)

activateReversalResponse._setSubstitutionGroup(transactionResponse)

forceCaptureResponse._setSubstitutionGroup(transactionResponse)

deactivateResponse._setSubstitutionGroup(transactionResponse)

echeck._setSubstitutionGroup(echeckOrEcheckToken)

loadReversalResponse._setSubstitutionGroup(transactionResponse)

depositReversal._setSubstitutionGroup(transaction)

fraudCheck._setSubstitutionGroup(transaction)

depositReversalResponse._setSubstitutionGroup(transactionResponse)

saleResponse._setSubstitutionGroup(transactionResponse)

loadResponse._setSubstitutionGroup(transactionResponse)

card._setSubstitutionGroup(cardOrToken)

accountUpdate._setSubstitutionGroup(transaction)

registerTokenRequest._setSubstitutionGroup(transaction)

authorizationResponse._setSubstitutionGroup(transactionResponse)

updateCardValidationNumOnTokenResponse._setSubstitutionGroup(transactionResponse)

credit._setSubstitutionGroup(transaction)

refundReversalResponse._setSubstitutionGroup(transactionResponse)

token._setSubstitutionGroup(cardOrToken)

fraudCheckResponse._setSubstitutionGroup(transactionResponse)

authReversal._setSubstitutionGroup(transaction)

load._setSubstitutionGroup(transaction)

capture._setSubstitutionGroup(transaction)

forceCapture._setSubstitutionGroup(transaction)

activateResponse._setSubstitutionGroup(transactionResponse)

echeckSalesResponse._setSubstitutionGroup(transactionResponse)

echeckVerificationResponse._setSubstitutionGroup(transactionResponse)

activate._setSubstitutionGroup(transaction)

echeckSale._setSubstitutionGroup(transaction)

echeckCreditResponse._setSubstitutionGroup(transactionResponse)

deactivate._setSubstitutionGroup(transaction)

captureGivenAuth._setSubstitutionGroup(transaction)

cancelSubscription._setSubstitutionGroup(recurringTransaction)

unloadResponse._setSubstitutionGroup(transactionResponse)

unload._setSubstitutionGroup(transaction)
