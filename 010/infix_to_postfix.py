"""A funciton to convert a given infix expression
to postfix expression using Shunting Yard Algorithm"""

from stack import MyStack

def infix_to_postfix(infix):
    """Converts given infix expression to postfix expression
       using Shunting Yard Algorithm"""
    
    #stack to temporarily store operators and paranthesis
    stack = MyStack(size= len(infix)+1) 
    postfix = []                      # a list to store postifix expression
    
    # Returns True if char is an operand
    is_operand = lambda char: char.isalpha() or char.isnumeric()

    # Returns the precedence of char from PRIORITY dict"""
    PRIORITY = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    precedence = lambda char: PRIORITY[char] if char in PRIORITY else -1

    for char in infix:
        if is_operand(char):
            postfix.append(char)
        elif char not in ['(',')']:
            while not stack.is_empty() and precedence(char) <= precedence(stack.top()):
                #Add elements from stack until stack is not empty and precedence of \n
                #char is less than the top most stack element
                postfix.append(stack.pop())
            stack.push(char)
        elif char == "(":
            stack.push(char)
        elif char == ")":
            while not stack.is_empty() and stack.top() != "(":
                postfix.append(stack.pop())
            if stack.top() != "(":
                raise ValueError("Parathesis Mismatch!")
            stack.pop()
    while not stack.is_empty():
        # pop out and add all existing elements from stack and add in onto postfix
        postfix.append(stack.pop())
    return " ".join(postfix)

def test_cases():
    """Some sample test cases"""
    assert infix_to_postfix("(A+B)*(C+D)") == "A B + C D + *"
    assert infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i") == "a b c d ^ e - f g h * + ^ * + i -"
    assert infix_to_postfix("7") == "7"
    assert infix_to_postfix("") == ""
    print("Test success!")

test_cases()
