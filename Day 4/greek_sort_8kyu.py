"""Write a comparator for a list of phonetic words for the letters of the greek alphabet."""

greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

def greek_comparator(lhs, rhs):
    """Function which return index difference of greek words"""
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)

def test_cases():
    """Some test cases"""
    assert greek_comparator('alpha', 'beta') <= -1
    assert greek_comparator('psi', 'psi') == 0
    assert greek_comparator('upsilon', 'rho') >= 1
    print("Test Successs!")

test_cases()
