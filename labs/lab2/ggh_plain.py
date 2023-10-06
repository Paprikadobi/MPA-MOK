import numpy as np
import lattice

from typing import Tuple

def key_gen(n: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
	"""Here we generate a public and private key using an orthogonal private key
	and a nearly parallel public key.

    :param n: Security parameter, determines the size of message that will be encrypted.
    :return: Tuple of private key, public key and unimodular matrix.
    """
	while True:
		private = np.random.randint(-10, 11, size=(n, n))
		# check that the basis has good form (individual vectors are almost orthogonal)
		if lattice.hamdamard_ratio(private) >= 0.8:
			break

	while True:
		unimodular = lattice.rand_unimod(n)
		public = unimodular @ private

		# check that the basis has bad form (individual vectors are almost parallel)
		if lattice.hamdamard_ratio(public) <= 0.1:
			return (private, public, unimodular)

def encrypt(msg: str, public: np.ndarray) -> np.ndarray:
	"""This method is used to encrypt a message with the public vector.
	Multiplication should be performed as m_1 * b_1 + m_2 * b_2 ... m_n * b_n.

	:param msg: Message that should be encrypted.
	:param public: Public key representing bad basis.
	:return: Encrypted ciphertext.
	"""
	assert len(msg) == public.shape[0]

	e = np.random.randint(-1, 2, len(msg))
	m = np.array([ord(x) for x in msg])

	return (m @ public) + e

def decrypt(ciphertext: np.ndarray, private: np.ndarray, unimodular: np.ndarray) -> str:
	"""This will take a ciphertext and revert it back to its original form.

	:param ciphertext: Ciphertext that should be decrypted.
	:param private: Private key representing good basis.
	:param unimodular: Unimodular matrix that was used during public key computation.
	:return: Decrypted message.
	"""
	assert ciphertext.shape[0] == private.shape[0]

	private_inv = np.linalg.inv(private)
	unimodular_inv = np.linalg.inv(unimodular)

	decrypted = np.round((np.round((ciphertext @ private_inv)) @ unimodular_inv)).astype(int)

	return ''.join([chr(x) for x in decrypted])
