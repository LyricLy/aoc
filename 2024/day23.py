from common import *
from collections import defaultdict
a = get_input()

d = defaultdict(set)
for x, y in a:
    d[x.string].add(y.string)
    d[y.string].add(x.string)

def bron_kerbosch(r, p, x):
    if not p and not x:
        yield r
    for v in p:
        yield from bron_kerbosch(r | {v}, p & d[v], x & d[v])
        p = p - {v}
        x = x | {v}

print(",".join(sorted(max(bron_kerbosch(set(), set(d), set()), key=len))))
