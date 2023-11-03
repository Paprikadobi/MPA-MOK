import seal
import requests

HANGMAN_PICS = [
'''   +---+
       |
       |
       |
      ===''',
'''   +---+
   O   |
       |
       |
      ===''',
'''   +---+
   O   |
   |   |
       |
      ===''',
'''   +---+
   O   |
  /|   |
       |
      ===''',
'''   +---+
   O   |
  /|\  |
       |
      ===''',
'''   +---+
   O   |
  /|\  |
  /    |
      ===''',
'''   +---+
   O   |
  /|\  |
  / \  |
      ===''']

if __name__ == '__main__':
    # initialize BFV scheme parameters
    params = seal.EncryptionParameters(seal.scheme_type.bfv)

    poly_modulus_degree = 4096
    params.set_poly_modulus_degree(poly_modulus_degree)
    params.set_coeff_modulus(seal.CoeffModulus.BFVDefault(poly_modulus_degree))
    params.set_plain_modulus(seal.PlainModulus.Batching(poly_modulus_degree, 20))

    context = seal.SEALContext(params)

    # initilize encoder that is used for encoding list of ints to `seal.Plaintext` and then decoding vice versa
    encoder = seal.BatchEncoder(context)

    # initialize encryptor and decryptors with keys
    keygen = seal.KeyGenerator(context)

    encryptor = seal.Encryptor(context, keygen.create_public_key())
    decryptor = seal.Decryptor(context, keygen.secret_key())

    msg = '_' * 51
    incorrect_guesses = 0

    while '_' in msg and incorrect_guesses < len(HANGMAN_PICS) - 1:
        letter = input('Input letter: ')

        plain = seal.Plaintext(f'{ord(letter):x}')
        # plain = encoder.encode([ord(x) for x in 'Craig Gentry proposed the first FHE scheme in 2009.'])
        cipher = encryptor.encrypt(plain)

        # check given letter from server
        response = requests.post(f'http://xdobia13.pythonanywhere.com/check_letter', data= {'letter': cipher.to_string().hex()}).content

        # deserialize ciphertext
        cipher = context.from_cipher_str(bytes.fromhex(response.decode()))

        # decrypt and decode ciphertext
        decoded = encoder.decode(decryptor.decrypt(cipher))

        new_msg = ''.join([letter if decoded[i] == 0 else x for i, x in enumerate(msg)])

        if new_msg == msg:
            incorrect_guesses += 1

        msg = new_msg

        print(HANGMAN_PICS[incorrect_guesses])
        print(f'Current msg: {msg}')

if '_' in msg:
    print('You lost')
else:
    print('You won')