from typing import Tuple

import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import Polynomial as P

from ex1 import polyadd
from ex2 import polymul
from ex3 import generate_keypair
from ex4 import encrypt, decrypt


def add_plain(
    ciphertext: Tuple[P, P], message: int, cmod: int, mmod: int, pmod: P
) -> Tuple[P, P]:
    """Add ciphertext and plaintext together.

    :param ciphertext: Ciphertext.
    :param message: Message.
    :param cmod: Coefficient modulus.
    :param mmod: Message modulus.
    :param pmod: Polynomial modulus.
    :return: New ciphertext.
    """
    dimension: int = len(pmod) - 1
    m = np.array([message] + [0] * (dimension - 1)) % pmod
    d: int = cmod // mmod
    ct0_: P = polyadd(ciphertext[0], d * m, cmod, pmod)
    return ct0_, ciphertext[1]


def add_cipher(
    ciphertext1: Tuple[P, P], ciphertext2: Tuple[P, P], cmod: int, pmod: P
) -> Tuple[P, P]:
    """Add two ciphertexts together.

    :param ciphertext1: Ciphertext.
    :param ciphertext2: Ciphertext.
    :param cmod: Coefficient modulus.
    :param pmod: Polynomial modulus.
    :return: New ciphertext.
    """
    ct0_: P = polyadd(ciphertext1[0], ciphertext2[0], cmod, pmod)
    ct1_: P = polyadd(ciphertext1[1], ciphertext2[1], cmod, pmod)
    return ct0_, ct1_


def mul_plain(
    ciphertext: Tuple[P, P], integer: int, cmod: int, imod: int, pmod: P
) -> Tuple[P, P]:
    """Multiply ciphertext by integer.

    :param ciphertext: Ciphertext.
    :param integer: Integer to multiply with.
    :param cmod: Ciphertext modulus.
    :param imod: Integer modulus.
    :param pmod: Polynomial modulus.
    :return: New ciphertext.
    """
    dimension: int = len(pmod) - 1
    m = P(np.array([integer] + [0] * (dimension - 1)) % imod)
    ct0_: P = polymul(ciphertext[0], m, cmod, pmod)
    ct1_: P = polymul(ciphertext[1], m, cmod, pmod)
    return ct0_, ct1_


def main():
    dim: int = 4
    deg: int = 2**4

    cmod: int = 2**15
    mmod: int = 2**8
    pmod: P = P([1] + [0] * (deg - 1) + [1])

    pk, sk, err = generate_keypair(dim, cmod, pmod)

    message1 = 15
    message2 = 3

    def test_1():
        print("Dec(a + Enc(pt)) = Dec(Enc(pt+a))")

        enc1 = encrypt(pk, dim, mmod, cmod, pmod, message1)
        enc2 = encrypt(pk, dim, mmod, cmod, pmod, message1 + message2)

        dec1 = decrypt(
            sk, cmod, mmod, pmod, add_plain(enc1, message2, cmod, mmod, pmod)
        )
        dec2 = decrypt(sk, cmod, mmod, pmod, enc2)

        print(dec1, dec2)

    def test_2():
        print("Dec(Enc(pt) + Enc(pt')) = Dec(Enc(pt+pt'))")

        enc1a = encrypt(pk, dim, mmod, cmod, pmod, message1)
        enc1b = encrypt(pk, dim, mmod, cmod, pmod, message2)
        enc1 = add_cipher(enc1a, enc1b, cmod, pmod)
        enc2 = encrypt(pk, dim, mmod, cmod, pmod, message1 + message2)

        dec1 = decrypt(sk, cmod, mmod, pmod, enc1)
        dec2 = decrypt(sk, cmod, mmod, pmod, enc2)

        print(dec1, dec2)

    def test_3():
        print("Dec(a*Enc(pt)) = Dec(Enc(pt*a))")

        enc1 = encrypt(pk, dim, cmod, mmod, pmod, message1)
        enc2 = encrypt(pk, dim, cmod, mmod, pmod, (message1 * message2) % mmod)

        dec1 = decrypt(
            sk, cmod, mmod, pmod, mul_plain(enc1, message2, cmod, mmod, pmod)
        )
        dec2 = decrypt(sk, cmod, mmod, pmod, enc2)

        print(dec1, dec2)

    def test_3():
        print("Dec(a*Enc(pt)) = Dec(Enc(pt*a))")

        enc1 = encrypt(pk, dim, mmod, cmod, pmod, message1)
        enc2 = encrypt(pk, dim, mmod, cmod, pmod, message1 * message2)

        dec1 = decrypt(
            sk, cmod, mmod, pmod, mul_plain(enc1, message2, cmod, mmod, pmod)
        )
        dec2 = decrypt(sk, cmod, mmod, pmod, enc2)

        print(dec1, dec2)

    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
