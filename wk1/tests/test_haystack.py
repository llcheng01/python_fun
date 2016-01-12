import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from haystack import Haystack

'''Stub some random test and see if the regex can parse just the numbers'''
def test_parse():
    s = """ Why should you learn to write programs? 7746
            12 1929 8827
            Writing programs (or programming) is a very creative
            7 and rewarding activity.  You can write programs for
            many reasons, ranging from making your living to solving
            8837 a difficult data analysis problem to having fun to helping 128
            someone else solve a problem.  This book assumes that
            everyone needs to know how to program ... """
    hay = Haystack(s)
    result = hay.parse()
    assert len(result) == 7
    assert int(result[6]) == 128

def test_sum():
    s = "Do not matter"
    result = ['125', '200', '75']
    hay = Haystack(s)
    sum = hay.sum(result)
    assert int(sum) == 400
