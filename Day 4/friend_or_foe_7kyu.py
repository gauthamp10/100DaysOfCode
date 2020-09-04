"""Make a program that filters a list of strings and returns a list with
only your friends name in it.If a name has exactly 4 letters in it, you can
be sure that it has to be a friend of yours! Otherwise, you can be sure he's not..."""

def friend(names):
    """Function to find friends"""
    return [elem for elem in names if len(elem)==4]

def test_case():
    """Sample test case"""
    assert friend(["Ryan", "Kieran", "Mark",]) == ["Ryan", "Mark"]
    print("Test Succes!")

test_case()
