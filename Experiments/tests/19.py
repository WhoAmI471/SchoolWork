# +1, *2, *3
# >= 69
# (10,s)
# 1 ≤ S ≤ 58

from functools import lru_cache

def moves(h):
    a, b = h
    return  (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2), (a * 3, b), (a, b * 3)

@lru_cache(None)
def game(h):
    if sum(h) >= 69:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if any(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if all(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if any(game(m) == 'W' or game(m) for m in moves(h)):
        return 'B2'

for s in range(1,59):
    if game( (10, s) ) is not None:
        print(s, game( (10, s) ))








