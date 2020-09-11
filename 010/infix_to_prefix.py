"""A funciton to convert a given infix expression
to prefix expression using Shunting Yard Algorithm"""

from stack import MyStack

# Returns True if char is an operand
is_operand = lambda char: char.isalpha() or char.isnumeric()

# Returns the precedence of char from PRIORITY dict"""
PRIORITY = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}
precedence = lambda char: PRIORITY[char] if char in PRIORITY else -1

def convert_to_prefix(postfix):
    """Returns prefix of given postfix"""
    prefix = []
    for char in postfix:
        if is_operand(char):
            prefix.append(char)
        else:
            temp_one = prefix.pop()
            temp_two = prefix.pop()
            prefix.append(char+" "+temp_two+" "+temp_one)
    return prefix[0]

def infix_to_prefix(infix):
    """Converts given infix expression to postfix expression
       using Shunting Yard Algorithm and converts that postfix to prefix"""

    if infix == "":
        return ""
    #stack to temporarily store operators and paranthesis
    stack = MyStack(size= len(infix)+1)
    postfix = []                      # a list to store postifix expression

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
    stack.clear_stack()
    # returns prefix string after converting the postfix passed to convert_to_prefix
    return convert_to_prefix(postfix)

def test_cases():
    """Some sample test cases"""
    assert infix_to_prefix("(A+B)*(C+D)") == "* + A B + C D"
    assert infix_to_prefix("x^y/(5*z)+2") == "+ / ^ x y * 5 z 2"
    assert infix_to_prefix("7") == "7"
    assert infix_to_prefix("") == ""
    print("Test success!")

test_cases()
