"""Write a function that takes in a string of one or more words, and returns
the same string, but with all five or more letter words reversed
(Just like the name of this Kata). Strings passed in will consist of only
letters and spaces. Spaces will be included only when more than one word is present."""

def spin_words(sentence):
    """Return spinned words as a string"""
    return " ".join([word[::-1] if len(word)>4 else word for word in sentence.split()])

def test_cases():
    """Sample test cases"""
    assert spin_words("Welcome") == "emocleW"
    print("Test Success!")

test_cases()
