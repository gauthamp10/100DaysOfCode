""" A funciton to evalute prefix expressions"""

import operator as op
from stack import MyStack

oper_dict = {
    "^":op.pow,
    "*":op.mul,
    "/":op.floordiv,
    "+":op.add,
    "-":op.sub,
}

def prefix_eval(prefix):
    """Return evaluated resultant of prefix"""
    for item in prefix.split()[::-1]:
        if item.isdigit():
            stack.push(item)
        else:
            temp_two = int(stack.pop())
            temp_one = int(stack.pop())
            stack.push(oper_dict[item](temp_two,temp_one))
    return int(stack.top())

stack = MyStack()

def test_cases():
    """Sample test cases"""
    assert prefix_eval('+ 39 * 42 2') == 123
    assert prefix_eval('/ * 20 2 + 4 1') == 8
    assert prefix_eval('6') ==  6
    print("Test Success!")

test_cases()
