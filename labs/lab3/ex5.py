from typing import Tuple

import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import Polynomial as P

from ex1 import polyadd
from ex2 import polymul


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
