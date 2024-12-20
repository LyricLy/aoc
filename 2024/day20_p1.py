from common import *
from collections import Counter
a = get_input().grid
print(a)
start = a.extract("S", ".")
end = a.extract("E", ".")
best = a.pathfind(".", start, end)

def given_cheat(aa, b):
    return pathfind(start, lambda p: p == end, lambda p: [(b, 2)] if p == aa else [(x, 1) for x in Grid.orthogonals(p) if a[x] == "."], lambda p: sum(abs(x - y) for x, y in zip(start, p)))

cheats = set()
for begin in a:
    if a[begin] != ".":
        continue
    for interim in a.orthogonals(begin):
        if a[interim] != "#":
            continue
        for ende in a.orthogonals(interim):
            if begin == ende or a[ende] != ".":
                continue
            cheats.add((begin, ende))

from tqdm import tqdm

c = 0
for cheat in tqdm(cheats):
    new = given_cheat(*cheat)
    if new is None:
        continue
    if best - new >= 100:
        c += 1
print(c)
