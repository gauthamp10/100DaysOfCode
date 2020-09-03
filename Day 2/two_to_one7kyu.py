"""Take 2 strings str_1 and str_2 including only letters from a to z.
Return a new sorted string, the longest possible, containing distinct letters"""

def longest(str_1,str_2):
    """Function which concat, sort and find set difference of two given strings"""
    return "".join(sorted([str(s) for s in set(str_1+str_2)]))

def test_cases():
    """Some useful test cases for the problem"""
    assert longest("aretheyhere", "yestheyarehere") == "aehrsty"
    assert longest("loopingisfunbutdangerous", "lessdangerousthancoding") == "abcdefghilnoprstu"
    assert longest("inmanylanguages", "theresapairoffunctions") == "acefghilmnoprstuy"
    print("Test Successfull")

test_cases()
