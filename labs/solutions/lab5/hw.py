from damgard_jurik import keygen
from random import random

# Set-up
pk, sk_ring = keygen(n_bits = 64, s = 1, threshold = 5, n_shares = 10)

votes, votes_enc = [], []

# Voting phase
for i in range(50):
    vote = int(random() < 0.5)
    votes.append(vote)
    votes_enc.append(pk.encrypt(vote))

# Counting phase
c = votes_enc[0]
for i in range(1, len(votes_enc)):
    c += votes_enc[i]

print(f"m: {sum(votes)} , c: {c.value}, dec: {sk_ring.decrypt(c)}")
