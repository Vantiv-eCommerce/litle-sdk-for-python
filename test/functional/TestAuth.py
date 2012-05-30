from SetupTest import *
import unittest

class TestAuth(unittest.TestCase):
    
    def test_auth(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '123'
        authorization.amount = 123
        authorization.orderSource = 'ecommerce'
    
        card = litleXmlFields.cardType()
        card.number = "42424242424242424242"
        card.expDate = "0912"
        card.cardValidationNum = '123'
        card.type = 'VI'
    
        authorization.card = card
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.litleXmlMapper(authorization)
            
        self.assertEquals(response.message, "Approved")
        
if __name__ == '__main__':
    unittest.main()        
        


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
#        assertEquals("4100100000000000", response.getAccountUpdater().getOriginalCardInfo().getNumber())
