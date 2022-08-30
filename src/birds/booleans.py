# Church encodings of boolean values and operators

# values
def TRUE(x):
    '''
    Church encoding for the "true" Boolean value.
    "Alpha-equivalent" to K (Kestrel).
    '''
    def f(y):
        return x
    return f


def FALSE(x):
    '''
    Church encoding for the "false" Boolean value.
    "Alpha-equivalent" to K(I).
    '''
    def f(y):
        return y
    return f


# operators
def NOT(x):
    '''
    Church encoding for the "not" Boolean operator.
    '''
    return x(FALSE)(TRUE)


def AND(x):
    '''
    Church encoding for the "AND" Boolean operator.
    '''
    def f(y):
        return x(y)(FALSE)
    return f


def OR(x):
    '''
    Church encoding for the "or" Boolean operator. "or" is inclusive.
    '''
    def f(y):
        return x(TRUE)(y)
    return f


def BEQ(x):
    '''
    Church encoding for Boolean equivalence.
    '''
    def f(y):
        return x(y(TRUE)(FALSE))(y(FALSE)(TRUE))
    return f
