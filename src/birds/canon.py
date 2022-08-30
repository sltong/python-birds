# The canonical list of combinator birds in _To Kill a Mockingbird_.

def B(x):
    """
    The Bluebird (B) combinator.
    """
    def f(y):
        def g(z):
            return x(y(z))
        return g
    return f

bluebird = B


def C(x):
    """
    The Cardinal (C) combinator.
    """
    def f(y):
        def g(z):
            return x(z)(y)
        return g
    return f

cardinal = C


def D(x):
    """
    The Dove (D) combinator.
    """
    def f(y):
        def g(z):
            def h(w):
                x(y)(z(w))
            return h
        return g
    return f

dove = D


def E(x):
    """
    The Eagle (E) combinator.
    """
    def f(y):
        def g(z):
            def h(w):
                def j(v):
                    return x(y)(z(w)(v))
                return j
            return h
        return g
    return f

eagle = E


def F(x):
    """
    The Finch (F) combinator.
    """
    def f(y):
        def g(z):
            return z(y)(x)
        return g
    return f

finch = F


def G(x):
    """
    The Goldfinch (G) combinator.
    """
    def f(y):
        def g(z):
            def h(w):
                return x(w)(y(z))
            return h
        return g
    return f

goldfinch = G


def H(x):
    """
    The hummingbird (H) combinator.
    """
    def f(y):
        def g(z):
            return x(y)(z)(y)
        return g
    return f

hummingbird = H


def I(x):
    """
    The Identity bird (I) combinator.
    Also known as the Idiot.
    """
    return x

idiot = identity = I


def J(x):
    """
    The Jay (J) combinator.
    """
    def f(y):
        def g(z):
            def h(w):
                return x(y)(x(w)(z))
            return h
        return g
    return f

jay = J


def K(x):
    """
    The Kestrel (K) combinator.
    """
    def f(y):
        return x
    return f

kestrel = K


def L(x):
    """
    The Lark (L) combinator.
    """
    def f(y):
        return x(y(y))
    return f

lark = L


def M(x):
    """
    The Mockingbird (M) combinator.
    """
    return x(x)

mockingbird = M


def O(x):
    """
    The Owl (O) combinator.
    """
    def f(y):
        return y(x(y))
    return f

owl = O


def Q(x):
    """
    The Queer (Q) combinator.
    """
    def f(y):
        def g(z):
            return y(x(z))
        return g
    return f

queer = Q


def Q_1(x):
    """
    The Quixotic (Q_1) combinator.
    """
    def f(y):
        def g(z):
            return x(z(y))
        return g
    return f

quixotic = Q_1


def Q_2(x):
    """
    The Quirky (Q_2) combinator.
    """
    def f(y):
        def g(z):
            return z(x(y))
        return g
    return f

quirky = Q_2


def R(x):
    """
    The Robin (R) combinator.
    """
    def f(y):
        def g(z):
            return y(z)(x)
        return g
    return f

robin = R


def S(x):
    """
    The Starling (S) combinator.
    """
    def f(y):
        def g(z):
            return x(z)(y(z))
        return g
    return f

starling = S


def T(x):
    """
    The Thrush (T) combinator.
    """
    def f(y):
        return y(x)
    return f

thrush = T


def U(x):
    """
    The Turing (U) combinator.
    """
    def f(y):
        return y(x(x)(y))
    return f

turing = U


def V(x):
    """
    The Vireo (V) combinator.
    """
    def f(y):
        def g(z):
            return z(x)(y)
        return g
    return f

vireo = V


def W(x):
    """
    The Warbler (W) combinator.
    """
    def f(y):
        return x(y)(y)
    return f

warbler = W


def W1(x):
    """
    The Converse Warbler (W1) combinator.
    """
    def f(y):
        def g(z):
            return y(x)(x)
        return g
    return f

converse_warbler = W1


def Y(f):
    """
    The Sage bird (Y) combinator.
    Actually, this is the Z combinator since Python eagerly evaluates function
    arguments.
    """
    def g(x):
        def h(y):
            return x(x)(y)
        return f(h)
    return ((g)(g))

sage = Y
