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
    # TODO: Complete the code here

def encrypt_messages(x: tuple[int, int], h: tuple[int, int], p: int, g: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Encrypts messages for OT, only one of those will be possible to decrypt.

    :param x: Tuple of 0 or 1 representing which message data.
    :param h: Tuple (h0, h1) generated in `initialize` function.
    :param p: Prime number defining Z_p.
    :param g: Generator in Z_p.
    :return: Tuple ((A0, A1), (B0, B1)) representing encrypted messages.
    """
    # TODO: Complete the code here

def decrypt_message(s: int, u: int, A: tuple[int, int], B: tuple[int, int], p: int, g: int) -> int:
    """Decrypts message based on s parameter.

    :param s: 0 or 1 representing which message can be decrypted.
    :param A: Tuple (A0, A1) representing first parts of encrypted messages.
    :param B: Tuple (B0, B1) representing second parts of encrypted messages.
    :param p: Prime number defining Z_p.
    :param g: Generator in Z_p.
    :return: 0 or 1 representing decrypted message.
    """
    # TODO: Complete the code here
