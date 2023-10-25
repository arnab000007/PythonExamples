from SubscriberInterface import OrderPlacedSubscriber, OrderCancelledSubscriber
from typing import List

class Flipkart:
    #Class Variables
    __instance = None

    __orderPlacedSubscriber: List[OrderPlacedSubscriber] = []
    __orderCancelledSubscriber: List[OrderCancelledSubscriber] = []

    @staticmethod
    def get_instance():

        if Flipkart.__instance == None:
            Flipkart()
        
        return Flipkart.__instance
    

    def __init__(self):
        '''Virtual Private constructor'''

        if Flipkart.__instance != None:
            raise Exception('This is a Singleton class instance')
        else:
            Flipkart.__instance = self
    

    def registerOrderPlacedSubscriber(self, subscriber:OrderPlacedSubscriber):
        self.__orderPlacedSubscriber.append(subscriber)
    
    def registerOrderCancelledSubscriber(self, subscriber:OrderCancelledSubscriber):
        self.__orderCancelledSubscriber.append(subscriber)
    

    def deRegisterOrderPlacedSubscriber(self, subscriber:OrderPlacedSubscriber):
        self.__orderPlacedSubscriber.remove(subscriber)
    
    def deRegisterOrderCancelledSubscriber(self, subscriber:OrderCancelledSubscriber):
        self.__orderCancelledSubscriber.remove(subscriber)

    def orderPlaced(self):

        for subscriber in self.__orderPlacedSubscriber:
            subscriber.announceOrderPlaced()
    
    def orderCancelled(self):

        for subscriber in self.__orderCancelledSubscriber:
            subscriber.announceOrderCancelled()
