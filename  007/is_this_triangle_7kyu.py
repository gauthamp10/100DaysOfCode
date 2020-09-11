"""https://www.codewars.com/kata/56606694ec01347ce800001b"""

def is_triangle(side_a, side_b, side_c):
    """Returns True if the input satisifes the sides of a triangle"""
    return side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a

def test_cases():
    """Sample test cases"""
    assert is_triangle(1, 2, 2) is True
    assert is_triangle(7, 2, 2) is False
    assert is_triangle(0, 2, 3) is False
    assert is_triangle(5, 1, 5) is True
    print("Test Success!")

test_cases()
