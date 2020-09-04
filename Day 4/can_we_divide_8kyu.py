"""Your task is to create functionisDivideBy (or is_divide_by) to
check if an integer number is divisible by each out of two arguments."""

def is_divide_by(number, num_a, num_b):
    """Function to check divisibility"""
    return True if abs(number) % abs(num_a) == 0 and abs(number) % abs(num_b) ==0 else False

def test_cases():
    """Some test cases"""
    assert is_divide_by(-12, 2, -6) is True
    assert is_divide_by(-12, 2, -5) is False
    assert is_divide_by(45, 1, 6) is False
    assert is_divide_by(45, 5 ,15) is True
    assert is_divide_by(4, 1, 4) is True
    assert is_divide_by(15, -5, 3) is True
    print("Test Success!")

test_cases()
