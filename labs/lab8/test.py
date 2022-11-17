import ex2

import pytest

@pytest.mark.parametrize(
    "p,g,x,s,msg",
    [
        (11, 2, 3, 1, (0, 1)),
        (17, 2, 12, 0, (0, 1)),
        (31, 2, 23, 0, (1, 1)),
    ],
)
def test_OT(p: int, g: int, x: int, s: int, msg: tuple[int, int]):
    u, h = ex2.initialize(s, p, g, pow(g, x, p))

    A, B = ex2.encrypt_messages(msg, h, p, g)

    decrypted = ex2.decrypt_message(s, u, A, B, p, g)

    assert decrypted == msg[s]