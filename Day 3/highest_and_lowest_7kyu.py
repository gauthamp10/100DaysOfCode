"""In this little assignment you are given a string of space separated
numbers, and have to return the highest and lowest number."""

def high_and_low(numbers):
    "Function to return the smallest and largest element from a list"
    numbers = [int(num) for num in numbers.split(" ")]
    return "{max} {min}".format(max=max(numbers),min=min(numbers))

def test_case():
    """Some useful test cases for the problem"""
    assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
    print("Test Success!")

test_case()
