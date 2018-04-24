from enum import Enum

class FoodType(Enum):
    burrito = 1
    taco = 2
    bowl = 3

class Item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = self.parse_price(price)

    # $16.68
    def parse_price(self, price):
        return float(price[1:].strip())

    def to_string(self):
        return self.name + " " + self.price

class Food(Item):
    def __init__(self, name, description, price,food_type):
        super(Food, self).__init__(name, price)
        # split on ', ['
        desc = description[1:-1].split(', [',1)
        self.topplings = self.parse_topplings(desc[1])
        self.sauces = self.parse_sauces(desc[0])
        self.food_type = food_type

    """
    desc = '[[Tomatillo-Red Chili Salsa (Hot)], [Black Beans, Rice, Cheese, Sour Cream]]'
    or desc = '[Tomatillo-Red Chili Salsa (Hot), [Black Beans, Rice, Cheese, Sour Cream]]'
    """
    def parse_sauces(self, desc):
        # parse element 0
        if desc.find('[') > -1:
# it is a list
           return desc[1:-1].split(',')
        return [desc]

    def parse_topplings(self, desc):
        # parse element 1
        return desc[:-1].split(',')

    def topplings_count(self):
        return len(self.sauces) + len(self.topplings)

class Beverage(Item):
    def __init__(self, name, desc, price):
        super(Beverage, self).__init__(name, price)
        self.desc = desc[1:-1]

class Side(Item):
    def __init__(self, name, price):
        super(Side, self).__init__(name, price)
