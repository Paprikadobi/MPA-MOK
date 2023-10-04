import numpy as np

import ex1
import ex2

import pytest

@pytest.mark.parametrize(
    "seed,dim,mod,expected",
    [
        (1, 3, 10, np.array([5, 9, 7])),
        (12, 7, 283, np.array([277, 184, 28, 56, 95, 239, 172])),
        (3, 14, 23, np.array([3, 9, 10, 0, 1, 6, 4, 19, 7, 5, 14, 19, 21, 4])),
    ],
)
def test_ex1(seed: int, dim: int, mod: int, expected: np.ndarray):
    result = ex1.ex1(seed, dim, mod)
    print(result)
    assert (expected == result).all()

@pytest.mark.parametrize(
    "basis,v,expected",
    [
        (np.array([[-5, 1, 0], [3, 2, -1], [0, 4, -5]]), np.array([-1, 1, 0]), 1.4142135623730951),
        (np.array([[-5, 1, 0], [3, 2, -1], [0, 4, -5]]), np.array([0, 4, -5]), 0),
        (np.array([[-3, 5, 1, 4], [1, 0, -1, 2], [4, 1, -3, 2], [0, 5, 2, -3]]), np.array([-2, 3, 0, 5]), 2.23606797749979),
    ],
)
def test_distance_lattice_vector(basis: np.ndarray, v: np.ndarray, expected: float):
    result = ex2.distance_lattice_vector(basis, v)
    assert expected == pytest.approx(result)

@pytest.mark.parametrize(
    "basis1, basis2,v,expected",
    [
        (np.array([[-5, 1, 0], [3, 2, -1], [0, 4, -5]]), np.array([[-2, 3, 0], [5, -2, 4], [3, 0, 4]]), np.array([-1, 1, 0]), 0),
        (np.array([[-5, 1, 0], [3, 2, -1], [0, 4, -5]]), np.array([[-2, 3, 0], [5, -2, 4], [3, 0, 4]]), np.array([3, 0, 4]), 1),
        (np.array([[-3, 5, 1, 4], [1, 0, -1, 2], [4, 1, -3, 2], [0, 5, 2, -3]]), np.array([[-2, 0, -1, 3], [2, 1, -4, -3], [-3, 0, -2, 5], [0, 3, 1, -4]]), np.array([-2, 3, 0, 5]), -1),
    ],
)
def test_check_bases(basis1: np.ndarray, basis2: np.ndarray, v: np.ndarray, expected: int):
    result = ex2.check_bases(basis1, basis2, v)
    assert expected == result