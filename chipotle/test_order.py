import pytest
from item_parser import Parser
from item_type import Item, Food, Side, Beverage, FoodType
from order import Order

class TestOrder(object):

    def test_can_add_items(self):
        order = Order()
        burrito = Food('awesome burritos', '[hot sause, [corn, steak]', '$9.99', FoodType.burrito)
        drink = Beverage('spirit', '[lime]', '$3.00')
        bowl = Food('Chicken bowl', '[tomatos, [cheese]', '$7.75', FoodType.bowl)
        order.add(1, 2, burrito)
        order.add(1, 2, drink)
        order.add(2, 1, bowl)
        order.add(2, 1, drink)
        assert len(order.line) == 2
        assert len(order.line.keys()) == 2

    def test_can_get_all_item_type(self):
        order = Order()
        burrito = Food('awesome burritos', '[hot sause, [corn, steak]', '$9.99', FoodType.burrito)
        bowl = Food('Chicken bowl', '[tomatos, [cheese]', '$7.75', FoodType.bowl)
        drink = Beverage('spirit', '[lime]', '$3.00')
        order.add(1, 2, burrito)
        order.add(1, 2, drink)
        order.add(2, 1, bowl)

        foods = order.get_all(Food)
        print('What??', foods)
        assert len(foods) == 2
        soda = order.get_all(Beverage)
        print(soda)
        assert len(soda) == 2
