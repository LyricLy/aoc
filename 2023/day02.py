with open("input.txt") as f:
    r = f.read()

from collections import Counter
from functools import reduce

c = 0
for game in r.split("\n"):
    if not game: continue
    x, y = game.split(": ")
    i = int(x.split()[-1])
    sides = [Counter(dict([((x := bb.split())[1], int(x[0])) for bb in side.split(", ")])) for side in y.split("; ")]
    possible = sides[0]
    for side in sides[1:]:
        possible |= side
    c += reduce(lambda x, y: x * y, possible.values())
print(c)
