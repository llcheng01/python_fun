import item_type
from item_parser import Parser
from collections import defaultdict

"""
Order contains a map of items based on order_id
i.e. order_id => [(quantity, item),]
"""

class Order(object):
    def __init__(self):
        self.line = defaultdict(list)

    def add(self, order_id, quantity, item):
        self.line[order_id].append((quantity, item))

    def get_all(self, type):
        for i in  self.line.values():
            for y in i:
                print('Debug:', y)

        return [y[1] for y in i if isinstance(y[1], type) for i in self.line.values()]

    # def calculate_average(self):
