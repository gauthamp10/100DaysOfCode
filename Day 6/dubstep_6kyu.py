"""https://www.codewars.com/kata/551dc350bf4e526099000ae5"""

def song_decoder(song):
    """Return decoded song string"""
    return ' '.join((song.replace("WUB"," ").strip()).split())

def test_cases():
    """Sample test cases"""
    assert song_decoder("AWUBBWUBC") == "A B C","WUB should be replaced by 1 space"
    assert song_decoder("AWUBWUBWUBBWUBWUBWUBC") == "A B C", \
                        "multiples WUB should be replaced by only 1 space"
    assert song_decoder("WUBAWUBBWUBCWUB") == "A B C","heading or trailing spaces should be removed"
    print("Test Success!")

test_cases()
