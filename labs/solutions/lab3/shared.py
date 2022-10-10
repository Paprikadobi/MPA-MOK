import numpy as np

def random_poly(mod, size):
    return np.random.randint(low = 1 - mod, high = mod - 1, size = size)

def init_poly(mod, seed):
    r = [1, 0, 1]

    np.random.seed(seed)

    p1 = random_poly(mod, 5)
    p2 = random_poly(mod, 5)

    return (r, p1, p2)