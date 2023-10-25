from SubscriberInterface import OrderPlacedSubscriber, OrderCancelledSubscriber
from Flipkart import Flipkart

class EmailSender(OrderPlacedSubscriber, OrderCancelledSubscriber):

    def __init__(self):
        flipkart: Flipkart = Flipkart.get_instance()
        flipkart.registerOrderPlacedSubscriber(self)
        flipkart.registerOrderCancelledSubscriber(self)
    
    def announceOrderPlaced(self):
        self.__sendEmail("Order has been placed")

    def announceOrderCancelled(self):
        self.__sendEmail("Order has been cancelled")
    
    def __sendEmail(self, email):
        print("Sending Email : " + email)
    