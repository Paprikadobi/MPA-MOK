import random
import math

def initialize(s: int, p: int, g: int, h: int) -> tuple[int, tuple[int, int]]:
    """Initialize parameters of P2 in OT-Elgamal protocol.

    :param s: 0 or 1 representing which message can be decrypted.
    :param p: Prime number defining Z_p.
    :param g: Generator in Z_p.
    :param h: Public key computed as h = g^x % p.
    :return: Tuple (u, (h0, h1)).
    """
    u = random.randint(0, p - 2)

    if s == 0:
        return (u, (pow(g, u, p), (h * pow(g, -u, p) % p)))
    else:
        return (u, ((h * pow(g, -u, p) % p), pow(g, u, p)))

def encrypt_messages(x: tuple[int, int], h: tuple[int, int], p: int, g: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Encrypts messages for OT, only one of those will be possible to decrypt.

    :param x: Tuple of 0 or 1 representing which message data.
    :param h: Tuple (h0, h1) generated in `initialize` function.
    :param p: Prime number defining Z_p.
    :param g: Generator in Z_p.
    :return: Tuple ((A0, A1), (B0, B1)) representing encrypted messages.
    """
    u = (random.randint(0, p - 2), random.randint(0, p - 2))

    return (
        (pow(g, u[0], p), pow(g, u[1], p)),
        ((pow(h[0], u[0], p) * pow(g, x[0], p)) % p, (pow(h[1], u[1], p) * pow(g, x[1], p)) % p)
    )

def decrypt_message(s: int, u: int, A: tuple[int, int], B: tuple[int, int], p: int, g: int) -> int:
    """Decrypts message based on s parameter.

    :param s: 0 or 1 representing which message can be decrypted.
    :param A: Tuple (A0, A1) representing first parts of encrypted messages.
    :param B: Tuple (B0, B1) representing second parts of encrypted messages.
    :param p: Prime number defining Z_p.
    :param g: Generator in Z_p.
    :return: 0 or 1 representing decrypted message.
    """
    return int(math.log((B[s] * pow(A[s], -u, p)) % p, g))

if __name__ == '__main__':
    p = 11
    g = 2
    x = 3
    h = pow(g, x, p)

    s = 1
    x = (0, 1)

    u, h = initialize(s, p, g, h)

    A, B = encrypt_messages(x, h, p, g)

    print(f'Received message: {decrypt_message(s, u, A, B, p, g)}')