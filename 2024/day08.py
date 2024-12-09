from common import *
from collections import defaultdict
import itertools
a = get_input().grid
freqs = defaultdict(list)
for x, y in a.items():
    if y != ".":
        freqs[y].append(x)

b = Grid(a.width, a.height, False)
for freq in freqs.values():
    for p1, p2 in itertools.combinations(freq, 2):
        x1, y1 = p1
        x2, y2 = p2
        d = x2-x1, y2-y1
        while p1 in b:
            b[p1] = True
            p1 = offset(p1, invert(d))
        while p2 in b:
            b[p2] = True
            p2 = offset(p2, d)
print(b.count(bool))