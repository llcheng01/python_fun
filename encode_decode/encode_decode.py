# import pdb

def encode(input):
    """
    Local variables. :(
    """
    result = ""
    temp = input[0]
    current = 1
    for i, x in enumerate(input, start=1):
        if temp != x:
            count = i - current
            result += str(count) + temp
            # pdb.set_trace()
            current = i
            temp = x
    result += str(len(input) - current) + temp
    return result

def decode(input):
    """
    str.isdigit(), set current multipler
    else, create the str by multiple digit with current alpha
    """
    count = 0
    result = ""
    for i, x in enumerate(input):
        if x.isdigit():
            count = x
        else:
            result += int(count) * x

    return result

