import seal
import random

class Server:
    def __init__(self, msg: str):
        self.msg = msg

        # initialize BFV scheme parameters
        params = seal.EncryptionParameters(seal.scheme_type.bfv)

        poly_modulus_degree = 4096
        params.set_poly_modulus_degree(poly_modulus_degree)
        params.set_coeff_modulus(seal.CoeffModulus.BFVDefault(poly_modulus_degree))
        params.set_plain_modulus(seal.PlainModulus.Batching(poly_modulus_degree, 20))

        self.context = seal.SEALContext(params)

        # initilize encoder that is used for encoding list of ints to `seal.Plaintext` and then decoding vice versa
        self.encoder = seal.BatchEncoder(self.context)

        # initialize evaluator that is used for evaluating operations on `seal.Ciphertext`
        self.evaluator = seal.Evaluator(self.context)


    def check_letter(self, cipher_letter: str) -> str:
        # encode msg so we can do operations with it
        encoded = self.encoder.encode(list(map(lambda x: ord(x), self.msg)))

        # convert string to `seal.Ciphertext` so we can do operations with it
        ciphertext = self.context.from_cipher_str(bytes.fromhex(cipher_letter))

        # compute difference between letter and letters in msg
        diff = self.evaluator.sub_plain(ciphertext, encoded)

        # multiply difference by random number, so we don't give away msg
        r = self.encoder.encode([random.randint(1, 10000) for _ in self.msg])
        result = self.evaluator.multiply_plain(diff, r)

        # return hex representation of result
        return result.to_string().hex()