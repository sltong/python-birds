import pytest

from birds.canon import B, C, I, K, M, S, W, Y


class TestC:
    def test_C_with_combinators(self):
        assert C(K)(M)(I) == K(I)(M)
        assert C(K)(M)(I) == I

class TestI:
    def test_I_self(self):
        assert I(I) == I

    def test_I_self_curried(self):
        assert I(I)(I)(I)(I)(I)(I)(I)(I)(I)(I)(I)(I) == I

    def test_I_self_nested(self):
        assert I(I(I(I(I(I(I(I(I(I(I(I(I)))))))))))) == I

    def test_I_literals(self):
        complex = 5 + 13j
        binary = 0b1010111
        empty_list = [""]

        assert I(1) == 1
        assert I(3.14159) == 3.14159
        assert I(complex) == complex
        assert I(binary) == binary
        assert I(empty_list) == empty_list
        assert I("chicken curry") == "chicken curry"

    def test_I_functions(self):
        def chirp(x):
            print(x)

        assert I(chirp) == chirp


class TestK:
    def test_K_with_combinators(self):
        assert K(I)(M) == I
        assert K(M)(I) == M
        assert K(K)(M) == K
        assert K(I)(K) == I


class TestM:
    def test_omega_recursion_error(self):
        # omega = M(M)
        # this would on indefinitely, so we expect a RecursionError
        with pytest.raises(RecursionError):
            M(M)


class TestS:
    def test_S_derived(self):
        # S = B(BW)(BBC)
        assert S(K)(M)(I) == B(B(W))(B(B)(C))(K)(M)(I)


class TestW:
    def test_W_with_combinators(self):
        assert W(M)(I) == M(I)(I)


class TestY:
    def test_factorial(self):
        # test recursion on a factorial function
        def factorial(f):
            return lambda n: 1 if n == 0 else n*f(n-1)

        assert Y(factorial)(0) == 1
        assert Y(factorial)(1) == 1
        assert Y(factorial)(3) == 6
        assert Y(factorial)(17) == 355687428096000
