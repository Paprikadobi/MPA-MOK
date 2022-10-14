import pqcrypto.kem.kyber512
import pqcrypto.kem.mceliece348864f
import pqcrypto.kem.ntruhps2048509

import pqcrypto.sign.dilithium4
import pqcrypto.sign.falcon_1024
import pqcrypto.sign.sphincs_haraka_256s_robust

from timeit import timeit

def compare_kem(name, instance, import_statement):
    public_key, private_key = instance.generate_keypair()
    ciphertext, plaintext = instance.encrypt(public_key)
    decrypted = instance.decrypt(private_key, ciphertext)

    print(name)
    print(f'public key (size): {len(public_key)}B')
    print(f'private key (size): {len(private_key)}B')

    generate_keypair_it = timeit('instance.generate_keypair()', setup = f'{import_statement} as instance', number = 100)
    encrypt_it = timeit('instance.encrypt(public_key)', setup = f'{import_statement} as instance; public_key, private_key = instance.generate_keypair()', number = 100)
    decrypt_it = timeit('instance.decrypt(private_key, ciphertext)', setup = f'{import_statement} as instance; public_key, private_key = instance.generate_keypair(); ciphertext, plaintext = instance.encrypt(public_key)', number = 100)

    print(f'generate keypair (time): {generate_keypair_it}s')
    print(f'encrypt (time): {encrypt_it}s')
    print(f'decrypt (time): {decrypt_it}s')

    print('-------------------------------------------')

def compare_sign(name, instance, import_statement):
    public_key, private_key = instance.generate_keypair()
    signature = instance.sign(private_key, b'test')
    verified = instance.verify(public_key, b'test', signature)

    print(name)
    print(f'public key (size): {len(public_key)}B')
    print(f'private key (size): {len(private_key)}B')
    print(f'signature (size): {len(signature)}B')

    generate_keypair_it = timeit('instance.generate_keypair()', setup = f'{import_statement} as instance', number = 100)
    encrypt_it = timeit('instance.sign(private_key, b"test")', setup = f'{import_statement} as instance; public_key, private_key = instance.generate_keypair()', number = 100)
    decrypt_it = timeit('instance.verify(public_key, b"test", signature)', setup = f'{import_statement} as instance; public_key, private_key = instance.generate_keypair(); signature = instance.sign(private_key, b"test")', number = 100)

    print(f'generate keypair (time): {generate_keypair_it}s')
    print(f'sign (time): {encrypt_it}s')
    print(f'verify (time): {decrypt_it}s')

    print('-------------------------------------------')


print('KEM schemes')
compare_kem('KYBER', pqcrypto.kem.kyber512, 'import pqcrypto.kem.kyber1024')
compare_kem('MCEliece', pqcrypto.kem.mceliece348864f, 'import pqcrypto.kem.mceliece348864f')
compare_kem('NTRU', pqcrypto.kem.ntruhps2048509, 'import pqcrypto.kem.ntruhps2048509')

print('Signature schemes')
compare_sign('Dilithium', pqcrypto.sign.dilithium4, 'import pqcrypto.sign.dilithium4')
compare_sign('Falcon', pqcrypto.sign.falcon_1024, 'import pqcrypto.sign.falcon_1024')
compare_sign('SPHINCS', pqcrypto.sign.sphincs_haraka_256s_robust, 'import pqcrypto.sign.sphincs_haraka_256s_robust')