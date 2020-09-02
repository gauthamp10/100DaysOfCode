"""Your job is to change the given string s using a non-negative integer n.Each bit
in n will specify whether or not to swap the case for each alphabetic
character in s: if the bit is 1, swap the case; if its 0, leave it as is.
When you finished with the last bit of n, start again with the first bit.
You should skip the checking of bits when a non-alphabetic character
Wis encountered, but they should be preserved in their original positions."""

from itertools import cycle

def swap(word, num):
    """Method to swao case using n (binary)"""
    bins = cycle(bin(num)[2:])
    res = ""
    for letter in word:
        if letter.isalpha() and int(next(bins)) == 1:
            res += letter.swapcase()
        else:
            res += letter
    return res

def test_cases():
    """Some useful test cases for th problem"""
    assert swap('Hello world!', 11) == 'heLLO wORLd!'
    assert swap("gOOd MOrniNg", 7864) == 'GooD MorNIng'
    assert swap('', 11345) == ''
    assert swap('the lord of the rings', 0) == 'the lord of the rings'
    print(f"Test Successfull")

test_cases()
