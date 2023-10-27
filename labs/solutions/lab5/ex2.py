def rsa_enc(msg: int, pk: int, n: int) -> int:
    """Encrypt message using RSA.

    :param msg: Number that should be encrypted.
    :param pk: RSA Public key.
    :param n: Modulus used during RSA encryption.
    :return: Encrypted number.
    """
    return pow(msg, pk, n)

def rsa_dec(cipher: int, sk: int, n: int) -> int:
    """Decrypt message using RSA.

    :param cipher: Number that should be decrypted.
    :param sk: RSA private key.
    :param n: Modulus used during RSA decryption.
    :return: Decrypted number number.
    """
    return pow(cipher, sk, n)

def main():
    print("m1 * m2 = Dec(Enc(m1, pk) * Enc(m2, pk), sk)")

    r = 11
    s = 13
    n = r * s

    pk = 7
    sk = pow(7, -1, (r - 1) * (s - 1))

    m1 = 28
    m2 = 33

    c1 = rsa_enc(m1, pk, n)
    c2 = rsa_enc(m2, pk, n)

    print((m1 * m2) % n, rsa_dec(c1 * c2, sk, n))


if __name__ == "__main__":
    main()