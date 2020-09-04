"""Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers."""

import re
def order(sentence):
    """Funciton to return a sentence in special ordering"""
    word_dict = {re.search(r'[0-9]', word).group(0): word for word in sentence.split()}
    return " ".join([sorted(word_dict.items())[i][1] for i in range(len(word_dict)) ])


def test_cases():
    """Some test cases to validate"""
    assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
    assert order("") == ""
    print("Test Success!")

test_cases()
