import numpy as np
from ex1 import polyadd_mod
from ex2 import polymul_mod
from ex3 import keygen
from ex4 import encrypt, decrypt

def add_plain(ct, pt, mod, t, poly_mod):
    dim = len(poly_mod) - 1
    # encode the integer into a plaintext polynomial
    m = np.array([pt] + [0] * (dim - 1), dtype=np.int64) % t
    delta = mod // t
    scaled_m = delta * m
    new_ct0 = polyadd_mod(ct[0], scaled_m, mod, poly_mod)
    return (new_ct0, ct[1])

def add_cipher(ct1, ct2, mod, poly_mod):
    new_ct0 = polyadd_mod(ct1[0], ct2[0], mod, poly_mod)
    new_ct1 = polyadd_mod(ct1[1], ct2[1], mod, poly_mod)
    return (new_ct0, new_ct1)

def mul_plain(ct, pt, mod, t, poly_mod):
    dim = len(poly_mod) - 1
    # encode the integer into a plaintext polynomial
    m = np.array([pt] + [0] * (dim - 1), dtype=np.int64) % t
    new_c0 = polymul_mod(ct[0], m, mod, poly_mod)
    new_c1 = polymul_mod(ct[1], m, mod, poly_mod)
    return (new_c0, new_c1)

if __name__ == '__main__':
    n = 4
    q = 6481
    t = 179
    poly_mod = [1, 0, 0, 0, 1]

    a, b, s = keygen(42, n, q, poly_mod)

    plain_text = 15

    plain = 3
    ct1 = encrypt((a, b), n, q, t, poly_mod, plain_text)
    ct2 = encrypt((a, b), n, q, t, poly_mod, plain_text + plain)

    print("Dec(a + Enc(pt)) = Dec(Enc(pt+a))")
    print(decrypt(s, q, t, poly_mod, add_plain(ct1, plain, q, t, poly_mod)), decrypt(s, q, t, poly_mod, ct2))

    ct1 = add_cipher(ct1, ct2, q, poly_mod)
    ct2 = encrypt((a, b), n, q, t, poly_mod, plain_text + plain_text + plain)
    print("Dec(Enc(pt) + Enc(pt')) = Dec(Enc(pt+pt'))")
    print(decrypt(s, q, t, poly_mod, ct1), decrypt(s, q, t, poly_mod, ct2))

    ct1 = encrypt((a, b), n, q, t, poly_mod, plain_text)
    ct2 = encrypt((a, b), n, q, t, poly_mod, (plain_text * plain) % t)
    print("Dec(a*Enc(pt)) = Dec(Enc(pt*a))")
    print(decrypt(s, q, t, poly_mod, mul_plain(ct1, plain, q, t, poly_mod)), decrypt(s, q, t, poly_mod, ct2))