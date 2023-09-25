class Pizza:
    def __init__(self):
        self.name = ''
        self.ingredients = []
    
    def prepare(self):
        print("Preparing Pizza " + self.name)
        print("Adding ingredients " + ", ".join(self.ingredients))
    
    def bake(self):
        print("Baking Pizza " + self.name)
    
    def cut(self):
        print("Cutting Pizza " + self.name)
    
    def box(self):
        print("Boxing Pizza " + self.name)


class CheesePizza(Pizza):

    def __init__(self):
        super().__init__()

        self.name = 'Cheese Pizza'
        self.ingredients = ['Cheese', 'Tomato Sauce Original']

class PepperoniPizza(Pizza):

    def __init__(self):
        super().__init__()

        self.name = 'Pepperoni Pizza'
        self.ingredients = ['Pepperoni', 'Tomato Sauce']

class VeggePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = 'Vegge Pizza'
        self.ingredients = ['Vegge', 'Tomato Sauce']


class PizzaFactory:
    @staticmethod
    def createPizza(type):
        if type == 'cheese':
            return CheesePizza()
        elif type == 'peppperoni':
            return PepperoniPizza()
        elif type == 'vegg':
            return VeggePizza()
        else:
            return ValueError('Invalid Pizza type')

pizza_factory = PizzaFactory()

cheese = pizza_factory.createPizza('cheese')
cheese.prepare()
cheese.bake()
cheese.cut()
cheese.box()

peppperoni = pizza_factory.createPizza('peppperoni')
peppperoni.prepare()
peppperoni.bake()
peppperoni.cut()
peppperoni.box()

vegg = pizza_factory.createPizza('vegg')
vegg.prepare()
vegg.bake()
vegg.cut()
vegg.box()
                                
