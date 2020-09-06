"""Given 2 strings, a and b, return a string of the form short+long+short,
with the shorter string on the outside and the longer string on the inside.
The strings will not be the same length, but they may be empty ( length 0 )."""

def solution(a, b):
    """Return value based on condition"""
    return a+b+a if len(a)<len(b) else b+a+b

def test_cases():
    """Sample test cases"""
    assert solution("1","22") == '1221'
    assert solution("33","1") == '1331'
    print("Test Success!")

test_cases()
