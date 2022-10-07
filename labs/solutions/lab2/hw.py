import lattice as lt
import ggh_plain as ggh

print('Alice computes')
print('Key generation')

private, public, uni = ggh.keyGeneration(4)

print(f'Private key: {private}, hamdamard ratio: {lt.hamdamard_ratio(private)}')
print(f'Public key: {public}, hamdamard ratio: {lt.hamdamard_ratio(public)}')
print(f'Unimodular matrix: {uni}')

print('Bob computes')
cipher_text = ggh.encrypt('test.txt', public)

print(f'Ciphertext: {cipher_text}')

print('Alice computes')

print(f'Decrypted: {"".join(chr(c) for c in ggh.decrypt(cipher_text, private, public, uni))}')
