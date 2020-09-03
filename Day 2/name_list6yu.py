"""Given: an array containing hashes of names
Return: a string formatted as a list of names separated by commas
except for the last two names, which should be separated by an ampersand."""

def namelist(names):
    for namedict in names:
        if len(names) == 0:
            return ''
        elif len(names) == 1:
            return namedict['name']
