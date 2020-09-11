"""In this kata, you are asked to square every digit of a number and concatenate them"""

def square_digits(num):
    """"Return concatednated square of every digit of a given number"""
    num_list = [int(digit)**2 for digit in str(num)]
    return int(''.join(str(digit) for digit in num_list))

def test_cases():
    """Sample test case"""
    assert square_digits(9119) == 811181
    print("Test success!")

test_cases()
