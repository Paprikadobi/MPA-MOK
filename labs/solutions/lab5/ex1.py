def caesar_enc(plaintext: str, key: int, alphabet: str) -> str:
    """Encrypt plain text using Caesar cipher.

    :param plaintext: Text that should be encrypted.
    :param key: Shift value used during encryption.
    :param alphabet: Characters that can `plaintext` contains.
    :return: Encrypted text.
    """
    ciphertext = ""
    for char in plaintext:
        ciphertext += alphabet[(alphabet.index(char) + key) % len(alphabet)]

    return ciphertext

def caesar_dec(ciphertext: str, key: int, alphabet: str) -> str:
    """Decrypt plain text using Caesar cipher.

    :param ciphertext: Text that should be decrypted.
    :param key: Shift value used during decryption.
    :param alphabet: Characters that can `ciphertext` contains.
    :return: Decrypted text.
    """
    plaintext = ""
    for char in ciphertext:
        plaintext += alphabet[(alphabet.index(char) - key) % len(alphabet)]

    return plaintext

def sum_letters(letters1: str, letters2: str, alphabet: str) -> str:
    letters = ''

    for (char1, char2) in zip(letters1, letters2):
        letters += alphabet[(alphabet.index(char1) + alphabet.index(char2)) % len(alphabet)]

    return letters

def main():
    print("m1 + m2 = Dec(Enc(m1, key) + Enc(m2, key), 2 * key)")

    m1 = "HELLO"
    m2 = "WORLD"
    key = 3
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    c1 = caesar_enc(m1, key, alphabet)
    c2 = caesar_enc(m2, key, alphabet)

    c3 = sum_letters(c1, c2, alphabet)

    print(sum_letters(m1, m2, alphabet), caesar_dec(c3, 2 * key, alphabet))


if __name__ == "__main__":
    main()