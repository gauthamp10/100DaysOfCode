"""Your team is writing a fancy new text editor and you've been tasked with implementing
the line numbering. Write a function which takes a list of strings and returns each line
prepended by the correct number.The numbering starts at 1. The format is n: string.
Notice the colon and space in between."""

def number(lines):
    """Function to return a formatted sting with line number"""
    pass

def test_cases():
    """Some useful test cases"""
    assert number([]), []
    assert number(["a", "b", "c"]) == ["1: a", "2: b", "3: c"]

test_cases()
