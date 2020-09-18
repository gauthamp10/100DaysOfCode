"""https://www.codewars.com/kata/578553c3a1b8d5c40300037c"""

def binary_array_to_number(arr):
    """Returns decimal from the contactanation of the given binary list"""
    return int(''.join([str(x) for x in arr]),2)

def test_cases():
    """Sample test cases"""
    assert binary_array_to_number([0,0,0,1]) == 1
    assert binary_array_to_number([0,0,0,1]) == 1
    assert binary_array_to_number([0,0,1,0]) == 2
    assert binary_array_to_number([1,1,1,1]) == 15
    assert binary_array_to_number([0,1,1,0]) == 6  
    print("Test Success!")

test_cases()
