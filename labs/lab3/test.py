from typing import Tuple

from numpy.polynomial import Polynomial as P
from numpy.polynomial import polynomial as poly

import ex1
import ex2
import ex3
import ex4

import pytest


@pytest.mark.parametrize(
    "p1,p2,cmod,pmod,expected",
    [
        (P([7, -5, 9]), P([-5, -2, -7]), 13, P([0, -8, 0]), P([2])),
        (P([-1, 9, 9]), P([-2, -5, 9]), 17, P([-9, -7, 1]), P([6, 11])),
        (P([5, 6, -4]), P([5, 9, -5]), 7, P([-9, 6, 3]), P([4, 5])),
        (P([8, 3, -4]), P([9, -6, 4]), 11, P([7, -3, -4]), P([6, 8])),
        (P([-5, -7, 4]), P([-8, -3, 7]), 17, P([6, -9, 3]), P([16, 6])),
    ],
)
def test_polyadd(p1: P, p2: P, cmod: int, pmod: P, expected: P):
    result: P = ex1.polyadd(p1, p2, cmod, pmod)
    assert expected == result


@pytest.mark.parametrize(
    "p1,p2,cmod,pmod,expected",
    [
        (P([-9, -6, 7]), P([-5, -2, 9]), 7, P([0, 6, 6]), P([3, 0])),
        (P([6, 1, -8]), P([9, -3, -5]), 7, P([7, 1, -1]), P([5, 1])),
        (P([5, -8, -6]), P([4, 9, 4]), 13, P([7, -1, -1]), P([7, 8])),
        (P([-4, -4, 9]), P([4, -2, 4]), 7, P([2, -1, -1]), P([2, 4])),
    ],
)
def test_polymul(p1: P, p2: P, cmod: int, pmod: P, expected: P):
    result: P = ex2.polymul(p1, p2, cmod, pmod)
    assert list(expected.coef) == list(result.coef)


def test_generate_keypair():
    keypair = ex3.generate_keypair(4, 5, P([1, 0, 1]))
    private_key, public_key, error = keypair
    assert len(private_key) == 2
    assert type(private_key[0]) is P
    assert type(private_key[1]) is P
    assert type(public_key) is P


@pytest.mark.parametrize("message", [5, 11, 64, 150, 178])
def test_encrypt(message: int):
    pmod = P([1, 0, 0, 0, 1])
    cmod: int = 6481
    mmod: int = 179
    dimension: int = 4

    keypair = ex3.generate_keypair(dimension, cmod, pmod)
    public_key, private_key, error = keypair

    ciphertext = ex4.encrypt(public_key, dimension, mmod, cmod, pmod, message)
    assert message == ex4.decrypt(private_key, cmod, mmod, pmod, ciphertext)
