from numpy.polynomial import polynomial as poly
from shared import init_poly

def polymul_mod(y, z, mod, poly_mod):
    _, rem = poly.polydiv(poly.polymul(y, z), poly_mod)

    return rem % mod

if __name__ == '__main__':
    mod = 11
    r, p1, p2 = init_poly(mod, 0)
    print(polymul_mod(p1, p2, mod, r))

    mod = 5
    r, p1, p2 = init_poly(mod, 0)
    print(polymul_mod(p1, p2, mod, r))
