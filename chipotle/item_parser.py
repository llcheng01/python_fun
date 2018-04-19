from item_type import Item, Food, Side, Beverage, FoodType

class Parser:
    """
    get row and determine type based on name
    and return the correct ItemType
    """
    @staticmethod
    def parse(row):
        name = row[2].lower()
        price = row[4]
        desc = row[3]
        if "burrito" in name:
            return Food(name, desc, price, FoodType.burrito)
        elif "tacos" in name:
            return Food(name, desc, price, FoodType.taco)
        elif "bowl" in name:
            return Food(name, desc, price, FoodType.bowl)
        elif "chips" in name:
            return Side(name, price)
        else:
            return Beverage(name, desc, price)



