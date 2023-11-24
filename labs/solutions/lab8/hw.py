from __future__ import annotations
from typing import List
import random

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
    return sum([(coeff * pow(x, i, q)) % q for i, coeff in enumerate(poly)]) % q

class Tallier:
    def __init__(self, i: int, t: int, n: int, p: int, q: int, g: int):
        self.i = i
        self.p = p
        self.q = q

        self.s = random.randint(0, q - 1)
        self.poly = gen_poly(self.s, t - 1, q)

        self.hs = [pow(g, self.s, p) if i == j else 0 for j in range(n)]
        self.shares = [0 for _ in range(n)]

    def send_initial_messages(self, talliers: List[Tallier]):
        self.shares[self.i] = eval_poly(self.poly, self.i + 1, self.q)

        for tallier in talliers:
            if self.i != tallier.i:
                tallier.receive_initial_message(self.i, self.hs[self.i], eval_poly(self.poly, tallier.i + 1, self.q))

    def receive_initial_message(self, i: int, g: int, share: int):
        self.hs[i] = g
        self.shares[i] = share

    def finalize_init(self):
        self.h = 1
        self.x = sum(self.shares) % self.p

        for h in self.hs:
            self.h = (self.h * h) % self.p

    def partial_decrypt(self, c1: int) -> int:
        return pow(c1, self.x, self.p)

def vote(v: int, p: int, g: int, h: int) -> tuple[int, int]:
    r = random.randint(0, p - 1)

    return (pow(g, r, p), (pow(h, r, p) * pow(g, v, p)) % p)

if __name__ == '__main__':
    p = 29
    q = 7
    g = 16
    n = 5
    t = 3

    talliers = [Tallier(i, t, n, p, q, g) for i in range(n)]

    for tallier in talliers:
        tallier.send_initial_messages(talliers)

    for tallier in talliers:
        tallier.finalize_init()

    h = talliers[0].h

    votes = [0, 0, 0, 1, 1, 0, 1]

    c1, c2 = 1, 1
    for e1, e2 in map(lambda v: vote(v, p, g, h), votes):
        c1 = (c1 * e1) % p
        c2 = (c2 * e2) % p

    d = 1
    for tallier in talliers[:t]:
        l = 1
        for j in range(t):
            if tallier.i != j:
                l = (l * (j + 1) * pow(j - tallier.i, -1, q)) % q
        d = (d * pow(tallier.partial_decrypt(c1), l, p)) % p

    m = (c2 * pow(d, -1, p)) % p

    for i in range(p):
        if pow(g, i, p) == m:
            print(i)
            break

