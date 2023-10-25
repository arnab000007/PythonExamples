from SubscriberInterface import OrderPlacedSubscriber
from Flipkart import Flipkart

class InvoiceGenerator(OrderPlacedSubscriber):

    def __init__(self):
        flipkart: Flipkart = Flipkart.get_instance()
        flipkart.registerOrderPlacedSubscriber(self)
    
    def announceOrderPlaced(self):
        print("Generating invaoice for Order placed")