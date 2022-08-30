import pytest

from birds.booleans import TRUE, FALSE, NOT, AND, OR, BEQ
from birds.canon import I, K, M


class TestTrue:
    def test_true_is_K(self):
        assert TRUE(I)(M) == K(I)(M)


class TestFalse:
    def test_false_is_KI(self):
        assert FALSE(I)(M) == K(I)(I)(M)


class TestNot:
    def test_not_true_is_false(self):
        assert NOT(TRUE) == FALSE

    def test_not_false_is_true(self):
        assert NOT(FALSE) == TRUE

    def test_double_negation(self):
        assert NOT(NOT(TRUE)) == TRUE


class TestAnd:
    def test_true_and_true_is_true(self):
        assert AND(TRUE)(TRUE) == TRUE

    def test_true_and_false_is_false(self):
        assert AND(TRUE)(FALSE) == FALSE

    def test_false_and_true_is_false(self):
        assert AND(FALSE)(TRUE) == FALSE

    def test_false_and_false_is_false(self):
        assert AND(FALSE)(FALSE) == FALSE


class TestOr:
    def test_true_or_true_is_true(self):
        assert OR(TRUE)(TRUE) == TRUE

    def test_true_or_false_is_true(self):
        assert OR(TRUE)(FALSE) == TRUE

    def test_false_or_true_is_false(self):
        assert OR(FALSE)(TRUE) == TRUE

    def test_false_or_false_is_false(self):
        assert OR(FALSE)(FALSE) == FALSE


class TestBooleanEquals:
    def test_true_equals_true(self):
        assert BEQ(TRUE)(TRUE) == TRUE

    def test_false_equals_false(self):
        assert BEQ(FALSE)(FALSE) == TRUE

    def test_true_does_not_equal_false(self):
        assert BEQ(TRUE)(FALSE) == FALSE

    def test_false_does_not_equal_true(self):
        assert BEQ(FALSE)(TRUE) == FALSE
