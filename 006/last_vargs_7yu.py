"""https://www.codewars.com/kata/541629460b198da04e000bb9"""

def last(*args):
    """Return last value from any object type - list,tuple,int,string"""
    if len(args) == 1:
        return int(''.join(map(str,args))) if isinstance(args[0],int) else args[0][-1]
    return args[-1]

def test_cases():
    """Sample test cases"""
    assert last([1,2,3,4,5]) == 5
    assert last("abcde") == "e"
    assert last(1, "b", 3, "d", 5) ==  5
    assert last(99) == 99
    print("Test Success!")

test_cases()
