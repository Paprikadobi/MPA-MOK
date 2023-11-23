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
    return [secret] + [random.randint(0, q - 1) for _ in range(degree)]

def eval_poly(poly: List[int], x: int, q: int) -> int:
    """Evaluate polynomial with provided x value.

    :param poly: Polynomial that should be evaluated.
    :param x: Value that should be used during evaluation
    :param q: Coefficient modulus.
    :return: Evaluation of polynomial.
    """
    return sum([(coeff * pow(x, i, q)) % q for i, coeff in enumerate(poly)])

def create_shares(n: int, poly: List[int], q: int) -> List[tuple[int, int]]:
    """Create shares that represent polynomial

    :param n: Number of shares that should be created.
    :param poly: Unique polynomial used to create shares.
    :param q: Coefficients modulus.
    :return: List of x values and its polynomial evaluations.
    """
    xs = range(1, n + 1)

    return list(zip(xs, [eval_poly(poly, x, q) % q for x in xs]))

def reconstruct_secret(shares: List[tuple[int, int]], degree: int, q: int) -> int:
    """Reconstruct secret from provided shares.

    :param shares: Secret that should be used in polynomial.
    :param degree: Degree of polynomial.
    :param q: Coefficients modulus.
    :return: Reconstructed secret.
    """
    matrix: List[List[int]] = []

    xs, ys = zip(*shares)

    for x in xs:
        matrix.append([pow(x, i, q) for i in range(degree + 1)])

    result: sympy.Matrix = solve_matrix(sympy.Matrix(matrix), sympy.Matrix(ys), q)

    return list(result)[0]

def solve_matrix(a: sympy.Matrix, b: sympy.Matrix, q: int) -> sympy.Matrix:
    """Solve system of modular equations.

    :param a: NxN matrix.
    :param b: Nx1 matrix.
    :param q: Coefficient modulus.
    :return: Solution matrix.
    """
    det = int(a.det())

    if gcd(det, q) == 1:
        return pow(det, -1, q) * a.adjugate() @ b % q

    raise ValueError(f"Equation cannot be solved: det={det}.")

if __name__ == '__main__':
    secret = 5
    degree = 2
    n = 3
    q = 11

    poly = gen_poly(secret, degree, q)
    shares = create_shares(n, poly, q)

    print(poly)
    print(shares)
    print(reconstruct_secret(shares, degree, q))