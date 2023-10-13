import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import Polynomial as P


def polymul(poly1: P, poly2: P, coefficient_modulus: int, polynomial_modulus: P) -> P:
    """Multiply two polynomials.

    :param poly1: First polynomial.
    :param poly2: Second polynomial.
    :param coefficient_modulus: Coefficient modulus.
    :param polynomial_modulus: Polynomial modulus.
    :return: New polynomial poly1*poly2 in Zp[x]/f(x).
    """
    mult: np.ndarrar = poly.polymul(poly1.coef, poly2.coef) % coefficient_modulus
    _, remainder = poly.polydiv(mult, polynomial_modulus.coef)
    return P(remainder % coefficient_modulus)
