"""The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}."""

def count(string):
    """"Function to return a dictionary of alphabet as keys
        and their count's as values from a list of alphabets"""
    unique = dict()
    for elem in string:
        if elem  in unique:
            unique[elem] = unique[elem]+1
        else:
            unique[elem] = 1
    return unique

def test_cases():
    """Some sample test cases"""
    assert count('aba') == {'a': 2, 'b': 1}
    assert count('abcddbacdb') == {'a': 2,'b': 3,'c': 2,'d': 3}
    assert count('') == {}
    print("Test Success!")

test_cases()
