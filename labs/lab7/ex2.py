from typing import List
import ex1

def reconstruct_secret(shares: List[tuple[int, int]], q: int) -> int:
    """Reconstruct secret from provided shares.

    :param shares: Secret that should be used in polynomial.
    :param q: Coefficients modulus.
    :return: Reconstructed secret.
    """
    # TODO: Complete the code here