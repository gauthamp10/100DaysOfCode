"""Sum of positive"""

def positive_sum(arr):
    """Return positive sum"""
    return sum([elem for elem in arr if elem >0])

def test_cases():
    """Test cases"""
    assert positive_sum([1,2,3,4,5]) == 15
    assert positive_sum([1,-2,3,4,5]) == 13
    assert positive_sum([-1,2,3,4,-5]) == 9
    print("Test Success!")

test_cases()
