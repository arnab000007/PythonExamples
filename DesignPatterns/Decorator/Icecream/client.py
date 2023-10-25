from IceCreamConeConstituents import IceCreamConeConstituents
from Cone.OrangeCone import OrangeCone
from Cone.ChocolateCone import ChocolateCone

from Topping.ChocoChips import ChocoChips
from Topping.StrawberryScoop import StrawberryScoop
from Topping.VanillaScoop import VanillaScoop
from Topping.ChocolateSyrup import ChocolateSyrup

def main():
    ice_cream:IceCreamConeConstituents = OrangeCone()
    ice_cream:IceCreamConeConstituents = ChocolateSyrup(ice_cream)
    ice_cream:IceCreamConeConstituents = ChocolateCone(ice_cream)
    ice_cream:IceCreamConeConstituents = VanillaScoop(ice_cream)
    ice_cream:IceCreamConeConstituents = StrawberryScoop(ice_cream)
    ice_cream:IceCreamConeConstituents = ChocoChips(ice_cream)

    print("IceCream Cost is {0}".format(ice_cream.getCost()))
    print("IceCream Description is {0}".format(ice_cream.getDescription()))



if __name__ == '__main__':
    main()