"""https://www.codewars.com/kata/576bb71bbbcf0951d5000044"""

def count_positives_sum_negatives(arr):
    """Return count of postive and sum of negatives"""
    return [len([elem for elem in arr if elem > 0]), \
            sum([elem for elem in arr if elem < 0])]  if arr!=[] else arr

def test_cases():
    """Sample test cases"""
    assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) \
        == [10,-65]
    print("Test Success!")

test_cases()
