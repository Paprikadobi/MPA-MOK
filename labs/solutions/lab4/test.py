from typing import List

import pytest

import ex3


@pytest.mark.parametrize(
    "p,a,q,n,expected",
    [
        ([3, 4, 1, 0], 2, 5, 4, [3, 0, 0, 4]),
        ([0, 0, 3, 2], 5, 7, 4, [5, 3, 1, 1]),
        ([4, 4, 3, 6, 3], 3, 7, 5, [6, 0, 1, 0, 2]),
    ],
)
def test_ntt(p: List[int], a: int, q: int, n: int, expected: List[int]):
    result = ex3.ntt(p, a, q, n)
    assert result == expected


@pytest.mark.parametrize(
    "p,a,q,n,expected",
    [
        ([3, 0, 0, 4], 2, 5, 4, [3, 4, 1, 0]),
        ([5, 3, 1, 1], 5, 7, 4, [0, 0, 3, 2]),
        ([6, 0, 1, 0, 2], 3, 7, 5, [4, 4, 3, 6, 3]),
    ],
)
def test_intt(p: List[int], a: int, q: int, n: int, expected: List[int]):
    result = ex3.innt(p, a, q, n)
    assert result == expected
