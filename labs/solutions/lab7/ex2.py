from typing import List
import ex1

def reconstruct_secret(shares: List[tuple[int, int]], q: int) -> int:
    """Reconstruct secret from provided shares.

    :param shares: Secret that should be used in polynomial.
    :param q: Coefficients modulus.
    :return: Reconstructed secret.
    """
    s = 0

    for (xj, y) in shares:
        prod, denum = y, 1

        for (xm, _) in shares:
            if xj != xm:
                prod = (prod * xm) % q
                denum = (denum * (xm - xj)) % q

        s = (s + prod * pow(denum, -1, q)) % q

    return s % q

if __name__ == '__main__':
    secret = 58
    degree = 100
    n = 101
    q = 103

    poly = ex1.gen_poly(secret, degree, q)
    shares = ex1.create_shares(n, poly, q)

    print(poly)
    print(shares)
    print(reconstruct_secret(shares, q))