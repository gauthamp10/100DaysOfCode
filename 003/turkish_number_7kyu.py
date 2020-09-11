"""Complete the function to convert an integer into a string of the Turkish name."""

turk_dict = {"0":"sıfır","1":"bir","2":"iki","3":"üç","4":"dört","5":"beş",
                "6":"altı","7":"yedi","8":"sekiz","9":"dokuz",
                "10":"on","20":"yirmi","30":"otuz","40":"kırk","50":"elli",
                "60":"altmış","70":"yetmiş","80":"seksen","90":"doksan"}
def get_turkish_number(num):
    """Function which returns the turkish evualent number"""
    num = str(num)
    if num in turk_dict:
        return turk_dict[num]
    return turk_dict[num[0]+"0"] +" "+turk_dict[num[1]]

def test_cases():
    """Some useful test cases"""
    assert get_turkish_number(1)  == "bir"
    assert get_turkish_number(13)  == "on üç"
    assert get_turkish_number(27)  == "yirmi yedi"
    assert get_turkish_number(38)  == "otuz sekiz"
    assert get_turkish_number(77)  == "yetmiş yedi"
    assert get_turkish_number(94)  == "doksan dört"
    print("Test Success!")

test_cases()
