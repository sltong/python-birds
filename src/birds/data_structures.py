from .booleans import TRUE, FALSE


def CONS(x):
    """
    A cons (pair).
    "Alpha-equivalent" to V (Vireo).
    """
    def f(y):
        def g(z):
            return z(x)(y)
        return g
    return f


def CAR(x):
    """
    First value of a cons pair.
    """
    return x(TRUE)


def CDR(x):
    """
    Second value of a cons pair.
    """
    return x(FALSE)
