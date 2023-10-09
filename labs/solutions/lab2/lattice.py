import numpy as np
import random

def hamdamard_ratio(basis: np.ndarray):
	"""This function is used to determine how orthogonal the matrix is.

	:param basis: Basis, whose hamdamard ratio is computed
	:return: float in range <0, 1> (close to 1 = orthogonal, close to 0 = parallel vectors)
	"""
	mult = 1
	for v in basis:
		mult = mult * np.linalg.norm(v)

	return abs(np.linalg.det(basis) / mult) ** (1.0 / basis.ndim)

def rand_unimod(n: int) -> np.ndarray:
	"""This function will create a random unimodular matrix that will be used to transform our public vector.

	:param n: Dimension of unimodular matrix
	:return: Random unimodular matrix
	"""

	random_matrix = np.random.randint(-10, 11, size=(n, n))
	upper_tri = np.triu(random_matrix, 0)
	lower_tri = np.tril(random_matrix, 0)

	# we want to create an upper and lower triangular matrix with +/- 1 in the diag
	for r in range(len(upper_tri)):
		for c in range(len(upper_tri)):
			if(r == c):
				upper_tri[r][c] = (2 * random.randint(0, 1)) - 1
				lower_tri[r][c] = (2 * random.randint(0, 1)) - 1

	return np.matmul(upper_tri,lower_tri)

def babai(basis: np.ndarray, vector: np.ndarray) -> np.ndarray:
	"""Babai’s Closest Vertex Algorithm.
	It permits to solve the closest vector to `vector` in the lattice `basis`.

	:param basis: Basis defining lattice.
	:param vector: Vector to which we want to find closest vector in lattice.
	:return: Closest vector in lattice
	"""
	basis_inv = np.linalg.inv(basis)
	t = np.round(vector @ basis_inv)

	return t @ basis
