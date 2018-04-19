import pytest
from item_parser import Parser
from item_type import Item, Food, Side, Beverage, FoodType

class TestItemParser(object):

    def test_can_parse_bowl_item(self):
        row = [2, 2, 'Chicken Bowl', '[Tomatillo-Red Chili Salsa (Hot), [Black Beans, Rice, Cheese, Sour Cream]]', '$16.98']
        item = Parser.parse(row)
        assert isinstance(item, Food)
        assert item.food_type == FoodType.bowl
        assert 'bowl' in item.name
        assert item.price == 16.98
        assert item.topplings_count() == 5

        # row = [1, 1, 'Chips and Fresh Tomato Salsa', NULL]

