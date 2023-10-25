from IceCreamConeConstituents import IceCreamConeConstituents

class OrangeCone(IceCreamConeConstituents):

    __previous_ice_cream:IceCreamConeConstituents
    __COST:int = 25
    __DESCRIPTION:str = "Orange Cone"

    def __init__(self, ice_cream:IceCreamConeConstituents = None):
        self.__previous_ice_cream = ice_cream

    def getCost(self)-> int:
        if self.__previous_ice_cream is not None:
            return self.__previous_ice_cream.getCost() + self.__COST
        return self.__COST
    
    def getDescription(self)-> str:
        
        if self.__previous_ice_cream is not None:
            return "{0} + {1}".format(self.__previous_ice_cream.getDescription(), self.__DESCRIPTION)
        
        return self.__DESCRIPTION