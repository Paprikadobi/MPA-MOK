from typing import List

import math
import sympy


def ntt(p: List[int], a: int, q: int, n: int) -> List[int]:
    """Convert polynomial to NTT domain.

    :param p: Polynomial to be converted.
    :param a: Subgroup generator of degree n.
    :param q: Coefficient modulus.
    :param n: Degree of a polynomial.
    :return: NTT representation of the polynomial.
    """
    # TODO: Complete the code here
    # Hint: To evaluate polynomial at given point, use
    #       `numpy.polynomial.polynomial.polyval`.


def innt(p: List[int], a: int, q: int, n: int) -> List[int]:
    """Convert polynomial from NTT domain.

    :param p: NTT polynomial to be converted.
    :param a: Subgroup generator of degree n.
    :param q: Coefficient modulus.
    :param n: Degree of a polynomial.
    :return: The polynomial.
    """
    # TODO: Complete the code here
    # Hint: Use the function `solve_matrix` to solve modular equations.


def solve_matrix(a: sympy.Matrix, b: sympy.Matrix, q: int) -> sympy.Matrix:
    """Solve system of modular equations.

    :param a: NxN matrix.
    :param b: Nx1 matrix.
    :param q: Coefficient modulus.
    :return: Solution matrix.
    """
    det = int(a.det())
    if math.gcd(det, q) == 1:
        return pow(det, -1, q) * a.adjugate() @ b % q
    raise ValueError(f"Equation cannot be solved: det={det}.")
