from typing import Tuple

import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import Polynomial as P

from ex1 import polyadd
from ex2 import polymul
from ex3 import get_binary_polynomial, get_uniform_polynomial, get_normal_polynomial


def encrypt(
    public_key: Tuple[P, P],
    dimension: int,
    message_modulus: int,
    coefficient_modulus: int,
    polynomial_modulus: P,
    message: int,
) -> Tuple[P, P]:
    """Encrypt a plaintext.

    :param public_key: Public key.
    :param dimension: Size of the polynomials0
    :param message_modulus: Message modulus.
    :param coefficient_modulus: Coefficient modulus.
    :param polynomial_modulus: Polynomial modulus0
    :param message: An integer in Zt.
    :return: Two vectors of the ciphertext.

    - 'u' is a random binary polynomial of size 'dimension'.
    - 'e1' and 'e2' are normally distributed polynomials of size 'dimension'.
    - 'q' is coefficient modulus.
    - 't' is mesasge modulus.
    - 'd = q // t'.
    - 'm' is a constant polynomial. For example:
      - 'message' is 3 => 'm = [3, 0, 0]',
      - 'message' is 5 => 'm = [5, 0, 0, 0, 0]'.
    - 'ct0 = b*u + e1 + d*m % coefficient_modulus' is the first part of ciphertext.
    - 'ct1 = a*u + e2 % coefficient_modulus' is the second part of ciphertext.
    """
    # TODO: Complete the code


def decrypt(
    private_key: P,
    coefficient_modulus: int,
    message_modulus: int,
    polynomial_modulus: np.array,
    ciphertext: Tuple[P, P],
) -> int:
    """Decrypt a ciphertext back into an integer.

    :param private_key: Private key.
    :param coefficient_modulus: Coefficient modulus.
    :param message_modulus: Message modulus.
    :param polynomial_modulus: Polynomial modulus.
    :param ciphertext: Encrypted message.
    """
    decrypted: P = polymul(
        ciphertext[1], private_key, coefficient_modulus, polynomial_modulus
    )
    plaintext: P = polyadd(
        decrypted, ciphertext[0], coefficient_modulus, polynomial_modulus
    )

    delta: int = coefficient_modulus // message_modulus
    decrypted_poly = np.round(plaintext.coef / delta) % message_modulus
    return int(decrypted_poly[0])
