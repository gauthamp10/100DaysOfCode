""" A funciton to evalute postfix expressions"""

import operator as op
from stack import MyStack

oper_dict = {
    "^":op.pow,
    "*":op.mul,
    "/":op.floordiv,
    "+":op.add,
    "-":op.sub,
}

def postfix_eval(postfix):
    """Return evaluated resultant of postfix"""
    for item in postfix.split(" "):
        if item.isdigit():
            stack.push(item)
        else:
            temp_two = int(stack.pop())
            temp_one = int(stack.pop())
            stack.push(oper_dict[item](temp_one,temp_two))
    return int(stack.top())

stack = MyStack()

def test_cases():
    """Sample test cases"""
    assert postfix_eval('45 3 11 * + 9 +') == 87
    assert postfix_eval('3 4 * 2 5 + / 2 5 4 + * 2 * 36 -') == 0
    assert postfix_eval('6') ==  6
    print("Test Success!")

test_cases()
