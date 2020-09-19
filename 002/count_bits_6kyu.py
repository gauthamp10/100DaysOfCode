"""Write a function that takes an integer as input, and returns the number of
bits that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative."""


def count_bits(num):
    """Function to count the number of 1's in binary of given value for n"""
    count = ''
    return len([count for bit in bin(num)[2:] if int(bit) == 1])


def test_cases():
    """Some useful test cases for the problem"""
    assert count_bits(0) == 0
    assert count_bits(4) == 1
    assert count_bits(7) == 3
    assert count_bits(9) == 2
    assert count_bits(10) == 2
    print("Test success!")


test_cases()
