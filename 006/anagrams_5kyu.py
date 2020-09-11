"""https://www.codewars.com/kata/523a86aa4230ebb5420001e1"""

from collections import Counter
def anagrams(word, words):
    """Return all anagrams in the list as a list"""
    return [elem for elem in words if Counter(word) == Counter(elem)]

def test_cases():
    """Sample test cases"""
    assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
    assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']
    print("Test Success!")

test_cases()
