# Test equivalence between the canonical bird combinators and their
# corresponding SKI form.
import pytest

from birds.canon import B, C, I, K, M, S, Y


def test_B_ski():
    # B = ((S(KS))K)
    assert B(I)(I)(M) == (S(K(S)))(K)(I)(I)(M)


def test_I_ski():
    # I = ((SK)K)
    assert I(1) == S(K)(K)(1)


def test_M_ski():
    # M = ((S((SK)K))((SK)K))
    assert M(I) == (S((S(K))(K)))((S(K))(K))(I)
