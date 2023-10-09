import numpy as np

def ex1(seed: int, dim: int, mod: int) -> np.ndarray:
    """Multiply random matrix with random vector.

    :param seed: Seed for random generation.
    :param dim: Dimension of matrix M and size of vector v.
    :param mod: Modulus.
    :return: c = (M * v) % m.
    """
    np.random.seed(seed)

    M = np.random.randint(-(mod - 1), mod, (dim, dim))
    v = np.random.randint(-(mod - 1), mod, dim)

    return M.dot(v) % mod