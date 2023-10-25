from abc import ABC, abstractmethod

class IceCreamConeConstituents(ABC):

    @abstractmethod
    def getCost(self)-> int:
        pass

    @abstractmethod
    def getDescription(self)-> str:
        pass
    