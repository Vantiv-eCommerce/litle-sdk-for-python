import litleXmlFileds
import pyxb
import unittest

class TestAuth:

    litle = litleXmlFields.litleOnlineRequest()
    def setUp():
        #something
        1+1;
    
    def simpleAuthWithCard(self):
        newAuthorization = authorization()
        newAuthorization.setReportGroup("Planets")
        newAuthorization.setOrderId("12344")
        newAuthorization.setAmount(106L)
        newAuthorization.setOrderSource(OrderSourceType.ECOMMERCE)
        
        card = litleXmlFields.cardType()
        card.setExpDate("1210")
        card.setNumber("4100000000000001")
        card.setType("VI")
        authorize.setCard(card);
        
        assertEquals(true)
    
#    def simpleAuthWithPaypal():
#        newAuthorization = authorization()
#        authorization.setReportGroup("Planets");
#        authorization.setOrderId("123456");
#        authorization.setAmount(106L);
#        authorization.setOrderSource(OrderSourceType.ECOMMERCE);
#        PayPal paypal = new PayPal();
#        paypal.setPayerId("1234");
#        paypal.setToken("1234");
#        paypal.setTransactionId("123456");
#        authorization.setPaypal(paypal);
#        
#        AuthorizationResponse response = litle.authorize(authorization);
#        assertEquals(response.getMessage(), "Approved",response.getMessage());
#    
#    public void posWithoutCapabilityAndEntryMode() throws Exception {
#        Authorization authorization = new Authorization();
#        authorization.setReportGroup("Planets");
#        authorization.setOrderId("12344");
#        authorization.setAmount(106L);
#        authorization.setOrderSource(OrderSourceType.ECOMMERCE);
#        Pos pos = new Pos();
#        pos.setCardholderId(PosCardholderIdTypeEnum.PIN);
#        authorization.setPos(pos);
#        CardType card = new CardType();
#        card.setType(MethodOfPaymentTypeEnum.VI);
#        card.setNumber("4100000000000002");
#        card.setExpDate("1210");
#        authorization.setCard(card);
#        
#        try {
#            litle.authorize(authorization);
#            fail("expected exception");
#        } catch(LitleOnlineException e) {
#            assertTrue(e.getMessage(),e.getMessage().startsWith("Error validating xml data against the schema"));
#    
#    public void accountUpdate() throws Exception {
#        Authorization authorization = new Authorization();
#        authorization.setReportGroup("Planets");
#        authorization.setOrderId("12344");
#        authorization.setAmount(106L);
#        authorization.setOrderSource(OrderSourceType.ECOMMERCE);
#        CardType card = new CardType();
#        card.setType(MethodOfPaymentTypeEnum.VI);
#        card.setNumber("4100100000000000");
#        card.setExpDate("1210");
#        authorization.setCard(card);
#        
#        AuthorizationResponse response = litle.authorize(authorization);
#        assertEquals("4100100000000000", response.getAccountUpdater().getOriginalCardInfo().getNumber());