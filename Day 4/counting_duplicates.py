"""Write a function that will return the count of distinct case-insensitive
alphabetic characters and numeric digits that occur more than once in the
input string. The input string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits."""

def duplicate_count(text):
    """Return duplicate count"""
    unique = dict()
    for elem in text.lower():
        if elem  in unique:
            unique[elem] = unique[elem]+1
        else:
            unique[elem] = 1
    return len([k for k,v in unique.items() if v >= 2])

def test_cases():
    """Some test cases"""
    assert duplicate_count("abcde") == 0
    assert duplicate_count("abcdea") == 1
    assert duplicate_count("invincibility") == 2
    print("Test Success!")

test_cases()
