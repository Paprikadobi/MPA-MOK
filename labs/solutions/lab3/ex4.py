import numpy as np
from ex1 import polyadd_mod
from ex2 import polymul_mod
from ex3 import keygen

def encrypt(pk, dim, q, t, poly_mod, pt):
    a, b = pk
    u = np.random.randint(0, 2, size = dim)
    delta = q // t
    m = np.array([pt] + [0] * (dim - 1), dtype=np.int64) % t
    e1, e2 = np.random.normal(0, 1, size = dim), np.random.normal(0, 2, size = dim)

    ct0 = polymul_mod(b, u, q, poly_mod)
    ct0 = polyadd_mod(ct0, e1, q, poly_mod)
    ct0 = polyadd_mod(ct0, delta * m, q, poly_mod)

    ct1 = polymul_mod(a, u, q, poly_mod)
    ct1 = polyadd_mod(ct1, e2, q, poly_mod)

    return ct0, ct1

def decrypt(sk, mod, t, poly_mod, ct):
	scaled_pt = polyadd_mod(polymul_mod(ct[1], sk, mod, poly_mod), ct[0], mod, poly_mod)
	delta = mod // t
	decrypted_poly = np.round(scaled_pt / delta) % t

	return int(decrypted_poly[0])


if __name__ == '__main__':
    n = 4
    q = 6481
    t = 179
    poly_mod = [1, 0, 0, 0, 1]

    a, b, s = keygen(4, n, q, poly_mod)

    print(f'a: {a}, b: {b}, s: {s}')

    plain_text = 25

    ct = encrypt((a, b), n, q, t, poly_mod, plain_text)

    print(f'ct: {ct}')
    print(f'plain: {plain_text} decrypted: {decrypt(s, q, t, poly_mod, ct)}')