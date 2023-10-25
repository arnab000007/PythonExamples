from SubscriberInterface import OrderPlacedSubscriber, OrderCancelledSubscriber
from Flipkart import Flipkart

class AnalyticsUpdate(OrderPlacedSubscriber, OrderCancelledSubscriber):

    def __init__(self):
        flipkart: Flipkart = Flipkart.get_instance()
        flipkart.registerOrderPlacedSubscriber(self)
        flipkart.registerOrderCancelledSubscriber(self)
    
    def announceOrderPlaced(self):
        print("Updating Analytics Order placed")

    def announceOrderCancelled(self):
        print("Updating Analytics Order Cancelled")
    
    
    