from typing import Tuple

import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import Polynomial as P

from ex1 import polyadd
from ex2 import polymul


def get_binary_polynomial(size: int) -> P:
    result = np.random.randint(0, 2, size)
    return P(result)


def get_uniform_polynomial(size: int, modulus: int) -> P:
    result = np.random.randint(0, modulus, size)
    return P(result)


def get_normal_polynomial(size: int) -> P:
    result = np.random.normal(0, 2, size)
    return P(np.int64(result))


def generate_keypair(
    dimension: int,
    coefficient_modulus: int,
    polynomial_modulus: P,
) -> Tuple[Tuple[P, P], P, P]:
    """Generate public and private keys.

    :param dimension: Size of the vectors.
    :param coefficient_modulus: Coefficient modulus.
    :param polynomial_modulus: Polynomial modulus.

    - 'a' is a random polynomial of size 'dimension' modulus 'coefficient_modulus'
    - 'e' is a polynomial normally distributed of size 'dimension'
    - 's' is a binary polynomial of size 'dimension'
    - 'b' = -a*s - e

    :return: Public key tuple (A, b), private key (s), error (e).
    """
    s = get_binary_polynomial(dimension)
    a = get_uniform_polynomial(dimension, coefficient_modulus)
    e = get_normal_polynomial(dimension)

    b: P = polyadd(
        polymul(-a, s, coefficient_modulus, polynomial_modulus),
        -e,
        coefficient_modulus,
        polynomial_modulus,
    )
    return (b, a), s, e
