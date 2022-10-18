from typing import Tuple

import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import Polynomial as P


def get_binary_polynomial(size: int) -> P:
    # TODO: Complete the code
    # Hint: Use numpy.random.randint
    pass


def get_uniform_polynomial(size: int, modulus: int) -> P:
    # TODO: Complete the code
    # Hint: Use numpy.random.randint
    pass


def get_normal_polynomial(size: int) -> P:
    # TODO: Complete the code
    # Hint: Use numpy.random.normal
    pass


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
    # TODO: Complete the code
