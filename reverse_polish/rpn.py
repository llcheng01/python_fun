"""
Reverse Polish Notation
"""
def calculate(input):
    stack = []
    result = 0
    for x in input.split(" "):
        if x.isdigit():
            stack.append(x)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            result = perform(int(op2), int(op1), x)
            stack.append(result)
    return result

def perform(x1, x2, operator):
    if operator == '+':
        return x1 + x2
    elif operator == '-':
        return x1 - x2
    elif operator == '*':
        return x1 * x2
    elif operator == '/':
        return x1 / x2
