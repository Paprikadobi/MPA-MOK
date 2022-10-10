import numpy as np
from shared import random_poly
from ex1 import polyadd_mod
from ex2 import polymul_mod

def keygen(seed, dim, mod, poly_mod):
    np.random.seed(seed)

    a = random_poly(mod, dim)
    e = np.random.normal(0, 1, size = dim)
    s = np.random.randint(0, 2, size = dim)

    b = polyadd_mod(polymul_mod(-a, s, mod, poly_mod), -e, mod, poly_mod)

    print(f'e: {e}')

    return (a, b, s)

if __name__ == '__main__':
    r = [1, 0, 1]
    a, b, s = keygen(2, 4, 5, r)
    print(f'a: {a}, b: {b}, s: {s}')