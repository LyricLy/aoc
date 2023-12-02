with open("input.txt") as f:
    r = f.read()

from collections import Counter

c = 0
for game in r.split("\n"):
    if not game: continue
    x, y = game.split(": ")
    i = int(x.split()[-1])
    sides = [Counter(dict([((x := bb.split())[1], int(x[0])) for bb in side.split(", ")])) for side in y.split("; ")]
    possible = True
    for side in sides:
        if side["red"] > 12 or side["green"] > 13 or side["blue"] > 14:
            possible = False
            break
    c += i*possible
print(c)
