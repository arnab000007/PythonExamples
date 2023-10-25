from IceCreamConeConstituents import IceCreamConeConstituents

class ChocolateSyrup(IceCreamConeConstituents):

    __previous_ice_cream:IceCreamConeConstituents
    __COST:int = 10
    __DESCRIPTION:str = "Chocolate Syrup"

    def __init__(self, ice_cream:IceCreamConeConstituents):

        if ice_cream is None:
            raise ValueError("Ice cream should have a base before adiing any topping")
        
        self.__previous_ice_cream = ice_cream

    def getCost(self)-> int:
        if self.__previous_ice_cream is not None:
            return self.__previous_ice_cream.getCost() + self.__COST
        
        
    
    def getDescription(self)-> str:
        
        if self.__previous_ice_cream is not None:
            return "{0} + {1}".format(self.__previous_ice_cream.getDescription(), self.__DESCRIPTION)
        
        