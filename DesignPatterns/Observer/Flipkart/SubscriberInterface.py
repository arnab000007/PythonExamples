from abc import ABC, abstractmethod

class OrderPlacedSubscriber(ABC):

    @abstractmethod
    def announceOrderPlaced(self):
        pass


class OrderCancelledSubscriber(ABC):

    @abstractmethod
    def announceOrderCancelled(self):
        pass