import time
from secrets import compare_digest
from typing import Tuple

import pqcrypto.kem
import pqcrypto.kem.saber
import pqcrypto.kem.mceliece460896
import pqcrypto.kem.kyber768

import pqcrypto.sign.dilithium4
import pqcrypto.sign.falcon_1024
import pqcrypto.sign.rainbowVc_classic


KEMs = (
    pqcrypto.kem.saber,
    pqcrypto.kem.mceliece460896,
    pqcrypto.kem.kyber768,
)
SIGs = (
    pqcrypto.sign.dilithium4,
    pqcrypto.sign.falcon_1024,
    pqcrypto.sign.rainbowVc_classic,
)


def do_kem(kem) -> Tuple[int, int, int]:
    """Perform encryption and decryption routine."""
    public_key, secret_key = kem.generate_keypair()
    ciphertext, plaintext = kem.encrypt(public_key)
    recovered = kem.decrypt(secret_key, ciphertext)
    assert compare_digest(plaintext, recovered)

    return len(public_key), len(secret_key), len(ciphertext)


def do_sig(sig) -> Tuple[int, int, int]:
    """Perform signature."""
    public_key, secret_key = sig.generate_keypair()
    signature = sig.sign(secret_key, b"test string")
    assert sig.verify(public_key, b"test string", signature)

    return len(public_key), len(secret_key), len(signature)


if __name__ == "__main__":
    for kem in KEMs:
        print(f"{kem.__name__}: ", end="")

        now = time.time()
        for _ in range(10):
            result = do_kem(kem)
            print(".", end="", flush=True)
        delta = (time.time() - now) / 10
        print()

        pk_len, sk_len, c_len = result

        print(f"  pk {pk_len}, sk {sk_len}, c {c_len}")
        print(f"  avg run {delta:.6f} s")

    for sig in SIGs:
        print(f"{sig.__name__} ", end="")

        now = time.time()
        for _ in range(10):
            result = do_sig(sig)
            print(".", end="", flush=True)
        delta = (time.time() - now) / 10
        print()

        pk_len, sk_len, s_len = result

        print(f"  pk {pk_len}, sk {sk_len}, s {s_len}")
        print(f"  avg run {delta:.6f} s")
