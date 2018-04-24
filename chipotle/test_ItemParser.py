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

    def test_can_parse_burrito_item(self):
        row = [5,1,'Steak Burrito', '[Fresh Tomato Salsa, [Rice, Black Beans, Pinto Beans, Cheese, Sour Cream, Lettuce]]', '$9.25']
        item = Parser.parse(row)
        assert isinstance(item, Food)
        assert item.food_type == FoodType.burrito
        assert 'burrito' in item.name
        assert item.price == 9.25
        assert item.topplings_count() == 7


    def test_can_parse_drink_item(self):
        row = ['1', '1', 'Nantucket Nectar', '[Apple]', '$3.39']
        item = Parser.parse(row)
        assert isinstance(item, Beverage)
        assert 'nantucket' in item.name
        assert item.price == 3.39


    def test_can_parse_side_item(self):
        row = [5, 1, 'Chips and Guacamole', 'NULL', '$4.45 ']
        item = Parser.parse(row)
        assert isinstance(item, Side)
        assert 'chips' in item.name
        assert item.price == 4.45
