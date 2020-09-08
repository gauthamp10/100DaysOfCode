"""https://www.codewars.com/kata/576b93db1129fcf2200001e6"""

def sum_array(arr):
    """Returns sum of list without highest and lowest vlues"""
    return 0 if arr is None or arr == [] else sum(sorted(arr)[1:-1])

def test_cases():
    """Sample test cases"""
    assert sum_array(None) == 0
    assert sum_array([]) == 0
    assert sum_array([3]) == 0
    assert sum_array([-3]) == 0
    assert sum_array([ 3, 5]) == 0
    assert sum_array([-3, -5]) == 0
    assert sum_array([6, 2, 1, 8, 10]) == 16
    assert sum_array([6, 0, 1, 10, 10]) == 17
    assert sum_array([-6, -20, -1, -10, -12]) == -28
    assert sum_array([-6, 20, -1, 10, -12]) == 3
    print("Test Success!")

test_cases()
