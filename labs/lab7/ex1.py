from typing import List
import random
import sympy

from math import gcd

def gen_poly(secret: int, degree: int, q: int) -> List[int]:
    """Generate polynomial with secret.

    :param secret: Secret that should be used in polynomial.
    :param degree: Degree of polynomial.
    :param q: Coefficients modulus.
    :return: Generated polynomial.
    """
    # TODO: Complete the code here

def create_shares(n: int, poly: List[int], q: int) -> List[tuple[int, int]]:
    """Create shares that represent polynomial.

    :param n: Number of shares that should be created.
    :param poly: Unique polynomial used to create shares.
    :param q: Coefficients modulus.
    :return: List of x values and its polynomial evaluations.
    """
    # TODO: Complete the code here

def reconstruct_secret(shares: List[tuple[int, int]], degree: int, q: int) -> int:
    """Reconstruct secret from provided shares.

    :param shares: Secret that should be used in polynomial.
    :param degree: Degree of polynomial.
    :param q: Coefficients modulus.
    :return: Reconstructed secret.
    """
    # TODO: Complete the code here