"""We want an array, but not just any old array, an array with contents!
Write a function that produces an array with the numbers 0 to N-1 in it."""

def arr(num=0):
    """Function which return a list of n elements"""
    return [elem for elem in range(num)]

def test_cases():
    """Some test cases"""
    assert arr(5) == [0,1,2,3,4]
    assert arr(0) == []
    assert arr() == []
    print("Test Success!")

test_cases()
