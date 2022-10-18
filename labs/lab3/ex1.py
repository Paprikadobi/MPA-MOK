import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import Polynomial as P


def polyadd(poly1: P, poly2: P, coefficient_modulus: int, polynomial_modulus: P) -> P:
    """Add two polynomials.

    :param poly1: First polynomial.
    :param poly2: Second polynomial.
    :param coefficient_modulus: Coefficient modulus.
    :param polynomial_modulus: Polynomial modulus.
    :return: New polynomial poly1+poly2 in Zp[x]/f(x).
    """
    # TODO: Complete the code here
    # Hint: Divide poly1+poly2 by polynomial_modulus
    pass
