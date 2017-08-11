ROMAN_LETTERS = {1 : {1:'I', 5:'V'},
                  10 : {1:'X', 5:'L'},
                  100 : {1:'C', 5:'D'},
                  1000 : {1:'M'}}

def numeral(val):
    """ 1. Convert arabic to decimal integers i.e. 1234 => [4,3,2,1]
        2. Convert arabic integers to roman letter strings
           [4,3,2,1] should get ['IIII', 'XXX', 'CC', 'M]
        3. Shorten each string, and skip if empty string
        4. Reverse list and join list items together """

    arabics = convert_to_romans(val, len(str(val)) - 1,[])[::-1]
    letters = [generate_letters(num, index) for index, num in enumerate(arabics)]
    shorten_letters = [shorten(l) for l in letters]
    return ''.join(shorten_letters[::-1])


def convert_to_romans(val, power, result=[]):
    """Convert arabic numeral to list of roman letters
       i.e. 1234 => [4,3,2,1]. Each letter would be
       pop() out to form list of roman chatacters"""

    """exit condition, when n is 0"""
    if power < 0:
        return result

    steps = pow(10, power)
    denom = val / steps
    result.append(denom)
    return convert_to_romans(val % steps, power-1, result)

def generate_letters(times, power):
    """Generate patterns for letters of
       specific powers, i.e. 8, 10^1  would turns
       into 'XXXXXXXX'"""

    if times == 0:
        return ''

    key = pow(10, power)
    result = ""
    for i in range(times):
        result += ROMAN_LETTERS[key][1]
    return result

def shorten(romans):
    """For 4s, replace letters from the right with 5th of
       certain power. For 9s replace the right with 10th
       of the NEXT power. For all other val, replace from
       the left the 5th of certain power."""

    val = len(romans)
    if (val < 4 or romans[0] == 'M'):
        return romans

    if val == 5:
        fifth = find_fifth(romans[0])
        return fifth

    if not (val == 4 or val == 9):
        fifth = find_fifth(romans[0])
        return fifth + romans[-(val - 5)::]

    if val == 4:
        fifth = find_fifth(romans[0])
        return romans[val-1] + fifth

    if val == 9:
        tenth = find_tenth(romans[0])
        return romans[val-1] + tenth

def find_fifth(val):
    """Accepted values are ['I','X','C']
       Handle thousand exception because there is not
       NEXT power"""

    for key, item in ROMAN_LETTERS.iteritems():
        if item[1] == val:
            return ROMAN_LETTERS[key][5]

def find_tenth(val):
    """Accepted values are ['I','X','C']
       Handle thousand exception because there is not
       NEXT power"""

    if val == 'M':
        raise ValueError("'M' has no next power")

    for key, item in ROMAN_LETTERS.iteritems():
        if item[1] == val:
            return ROMAN_LETTERS[key * 10][1]
