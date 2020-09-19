"""Given: an array containing hashes of names
Return: a string formatted as a list of names separated by commas
except for the last two names, which should be separated by an ampersand."""


def namelist(names):
    """Function to format a names list"""
    if not names:
        return ''
    names = [name["name"] for name in names]
    size = len(names)
    if size == 1:
        return names[0]
    index = 0
    res = ''
    while index != size-2:
        res += names[index] + ", "
        index += 1
    res += names[index] + " & " + names[index+1]
    return res


def test_cases():
    """Some useful test cases for the problem"""
    assert namelist([{'name': 'Bart'}, {
        'name': 'Lisa'}, {
        'name': 'Maggie'}, {
        'name': 'Homer'}, {'name': 'Marge'}
                    ]) == 'Bart, Lisa, Maggie, Homer & Marge'
    assert namelist([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart & Lisa'
    assert namelist([{'name': 'Bart'}]) == 'Bart'
    assert namelist([]) == ''
    print("Test Successfull")


test_cases()
