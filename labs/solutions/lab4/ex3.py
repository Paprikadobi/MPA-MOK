import math
from typing import List

import sympy
import numpy as np


def ntt(p: List[int], a: int, q: int, n: int) -> List[int]:
    """Convert polynomial to NTT domain.

    :param p: Polynomial to be converted.
    :param a: Subgroup generator of degree n.
    :param q: Coefficient modulus.
    :param n: Degree of a polynomial.
    :return: NTT representation of the polynomial.
    """
    res: List[int] = []
    for i in range(n):
        x = pow(a, i, q)
        val: float = np.polynomial.polynomial.polyval(x, p) % q
        res.append(int(val))
    return res


def innt(p: List[int], a: int, q: int, n: int) -> List[int]:
    """Convert polynomial from NTT domain.

    :param p: NTT polynomial to be converted.
    :param a: Subgroup generator of degree n.
    :param q: Coefficient modulus.
    :param n: Degree of a polynomial.
    :return: The polynomial.
    """
    A = sympy.Matrix.zeros(n, n)

    for i in range(n):
        for j in range(n):
            x = pow(a, i, q)
            A[i, j] = pow(x, j, q)

    return list(solve_matrix(A, sympy.Matrix(p), q))


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
