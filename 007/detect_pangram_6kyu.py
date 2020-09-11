"""https://www.codewars.com/kata/545cedaa9943f7fe7b000048"""

def is_pangram(s):
    """Returns true if string  is a panagram"""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return sorted(set([elem for elem in s.lower() if elem in alpha])) == list(alpha.lower())

def test_cases():
    """Sample test cases"""
    assert is_pangram("The quick, brown fox jumps over the lazy dog!") is True
    assert is_pangram("Python is good for one-liners") is False
    assert is_pangram("Two driven jocks help fax my big quiz") is True
    print("Test Success!")

test_cases()
