import ex1
import ex2

import pytest


@pytest.mark.parametrize(
    "m,c",
    [
        ("THISISMESSAGE", "WKLVLVPHVVDJH"),
        ("CAESARISTHEBEST", "FDHVDULVWKHEHVW"),
    ],
)
def test_caesar(m: str, c: str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = 3

    assert c == ex1.caesar_enc(m, key, alphabet)
    assert m == ex1.caesar_dec(c, key, alphabet)

@pytest.mark.parametrize(
    "m,c,r,s",
    [
        (10, 82, 7, 13),
        (23, 460, 23, 29),
        (102, 19979, 127, 199),
    ],
)
def test_rsa(m: int, c: int, r: int, s: int):
    n = r * s
    pk = 5
    sk = pow(pk, -1, (r - 1) * (s - 1))

    assert c == ex2.rsa_enc(m, pk, n)
    assert m == ex2.rsa_dec(c, sk, n)
