# Church encodings of numerals and arithmetic operators
from .booleans import TRUE, FALSE


def ZERO(x):
    '''
    Church numeral "zero".
    "Alpha-equivalent" to FALSE.
    '''
    def f(y):
        return y
    return f


def ISZERO(x):
    """
    Test for zero equality.
    """
    def f(_):
        return FALSE
    return x(f)(TRUE)


def SUCC(x):
    """
    Successor function.
    """
    def f(y):
        def g(z):
            return y(x(y)(z))
        return g
    return f


# arithmetic operators
def ADD(x):
    """
    Addition arithmetic operator for Church numerals.
    """
    def f(y):
        return y(SUCC)(x)
    return f
