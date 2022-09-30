import numpy as np

def ex1(seed, dim, mod):
    np.random.seed(seed)

    M = np.random.randint(-(mod - 1), mod - 1, (dim, dim))
    v = np.random.randint(-(mod - 1), mod - 1, dim)

    return M.dot(v) % mod

if __name__ == '__main__':
    print(ex1(20, 3, 11))