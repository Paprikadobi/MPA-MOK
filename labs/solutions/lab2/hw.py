import lattice as lt
import ggh_plain as ggh
import numpy as np

print('Alice computes')
print('Key generation')

private, public, uni = ggh.key_gen(4)

print(f'Private key: {private}, hamdamard ratio: {lt.hamdamard_ratio(private)}')
print(f'Public key: {public}, hamdamard ratio: {lt.hamdamard_ratio(public)}')
print(f'Unimodular matrix: {uni}')

print('Bob computes')

cipher_text = ggh.encrypt('test', public)
print(f'Ciphertext: {cipher_text}')

public_inv = np.linalg.inv(public)

print('Alice computes')

print(f'Decrypted: {ggh.decrypt(cipher_text, private, uni)}')
