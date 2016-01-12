import os
import re
import pdb

os.chdir('.')
print(os.getcwd())
'''It will open and read test data file'''
'''Find all numerical values and sum them'''

class Haystack(object):
    def __init__(self, value=''):
        self.value = value
        self.numbers = []

    def open_read(self):
        with open('regex_sum_199880.txt', 'r') as f:
            self.value  = f.read()
        f.closed

    """Parse the string and extract the integer"""
    def parse(self):
        self.numbers = re.findall(r'\d+', self.value)
        return self.numbers

    """Sum all the integer"""
    def sum(self, numbers=[]):
        results = map(int, numbers)
        return reduce(lambda a, x: a + x, results)

def main():
    h = Haystack("I am 17 years old")
    pdb.set_trace()
    h.open_read()
    pdb.set_trace()
    arr = h.parse()
    pdb.set_trace()
    print(arr)
    s = h.sum(arr)
    pdb.set_trace()
    print("sum:", s)


if __name__ == '__main__':
    main()
