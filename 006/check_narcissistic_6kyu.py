"""https://www.codewars.com/kata/5287e858c6b5a9678200083c"""


def narcissistic(value):
    """Return True if given number is narcissistic."""
    return sum([int(digit)**len(str(value)) for digit in str(value)]) == value


def test_cases():
    """Sample test cases"""
    assert narcissistic(56) is False
    assert narcissistic(371) is True
    assert narcissistic(122) is False
    assert narcissistic(370) is True
    print("Test Success!")

test_cases()
