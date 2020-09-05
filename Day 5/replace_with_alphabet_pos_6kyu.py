"""In this kata you are required to, given a string, replace every letter with
its position in the alphabet.If anything in the text isn't a letter, ignore it
and don't return it."""

import string
from random import randint

def alphabet_position(text):
    """Function to return alphabet pos"""
    alpha_dict = dict(zip(list(string.ascii_lowercase), range(1,27)))
    return  " ".join([str(alpha_dict[char]) for char in text.lower() if char.isalpha()]) \
                if not text.isdigit() else ""

def test_cases():
    """Test cases"""
    assert alphabet_position("The sunset sets at twelve o' clock.") \
             == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    assert alphabet_position("The narwhal bacons at midnight.") \
             == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
    number_test = ""
    for item in range(10):
        number_test += str(randint(1, 9))
    assert alphabet_position(number_test) == ""
    print("Test Success!")

test_cases()
