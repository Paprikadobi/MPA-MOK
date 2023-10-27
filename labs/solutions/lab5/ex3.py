from phe import paillier

def check_homomorphic(m1, m2):
    pk, sk, = paillier.generate_paillier_keypair()

    c1 = pk.raw_encrypt(m1)
    c2 = pk.raw_encrypt(m2)

    def test_1():
        print("Dec((c1 * c2) % n^2) = (m1 + m2) % n")

        dec = sk.raw_decrypt((c1 * c2) % pk.nsquare)

        print(dec, (m1 + m2) % pk.n)

    def test_2():
        print("Dec((c1 * g^m2) % n^2) = (m1 + m2) % n")

        dec = sk.raw_decrypt((c1 * pow(pk.g, m2, pk.nsquare)) % pk.nsquare)

        print(dec, (m1 + m2) % pk.n)

    def test_3():
        print("Dec(c1^m2 % n^2) = (m1 * m2) % n")

        dec = sk.raw_decrypt(pow(c1, m2, pk.nsquare))

        print(dec, (m1 * m2) % pk.n)

    def test_4():
        print("Dec(c2^m1 % n^2) = (m1 * m2) % n")

        dec = sk.raw_decrypt(pow(c2, m1, pk.nsquare))

        print(dec, (m1 * m2) % pk.n)

    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == "__main__":
    check_homomorphic(1, 3)
    check_homomorphic(3, 2)
    check_homomorphic(2, 4)
    check_homomorphic(5, 18)
    check_homomorphic(32, 64)