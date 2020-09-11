"""Data Structure introduction - Stack"""

class MyStack:
    """A blueprint to implement basic stack operations"""
    def __init__(self,size = 10):
        """Intialize"""
        self.stack = []
        self.size =size

    def __str__(self):
        """Pythonic way of converting objects to string"""
        return str(self.stack)

    def __bool__(self):
        """__nonzero___ equivalient"""
        return bool(self.stack)

    def push(self,item):
        """Add item into stack"""
        if len(self.stack) >= self.size:
            raise OverflowError("StackOverflow!")
        self.stack.append(item)

    def pop(self):
        """Delete/pop top element from stack"""
        if self.stack:
            return self.stack.pop()
        raise IndexError("Empty Stack!")

    def top(self):
        """Find and return stack's top element"""
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        """Return False if stack empty"""
        return False if bool(self.stack) else True

    def find_size(self):
        """Returns current stack size"""
        return len(self.stack)

    def  find_item(self,item):
        """Check if item is present"""
        return item in self.stack

    def clear_stack(self):
        """Empty stack items"""
        self.stack.clear()


if __name__ == "__main__":
    """Stack object creation"""
    stack = MyStack()
    """stack initialization"""
    bool([stack.push(elem) for elem in range(1,11)])
    print("\nStack Operations Demo")
    print("-------------------")
    print("{}:{}".format("Initial Stack:",str(stack)))
    print("pop(): " + str(stack.pop()))
    print("{}:{}".format("Stack after pop():",str(stack)))
    print("top(): " + str(stack.top()))
    stack.push(777)
    print("{}:{}".format("Stack after push():",str(stack)))
    print("is_empty(): " + str(stack.is_empty()))
    print("size(): " + str(stack.find_size()))
    # stack.push(33) -- Raise Overflow error
    """The below statement raises IndexError since stack is empty"""
    #bool([stack.pop() for i in range(stack.find_size()+1)])
    CHECK_NUM= 777
    print("{} :{}".format("Is "+str(CHECK_NUM)+" present in stack?",stack.find_item(CHECK_NUM)))
    stack.clear_stack()
    print("Empty stack:", stack)
