from common import *
from collections import defaultdict

with open("input.txt") as f:
    t = f.read()

s, _, *rules = t.splitlines()
rs = {}
for rule in rules:
    x, y = rule.split(" -> ")
    rs[x] = y

m = defaultdict(int)
for i in range(len(s)-1):
    m[s[i:i+2]] += 1

def do_step(m):
    mp = defaultdict(int)
    for p, v in m.items():
        if p in rs:
            r = rs[p]
            mp[p[0] + r] += m[p]
            mp[r + p[1]] += m[p]
        else:
            mp[p] = m[p]
    return mp

for _ in range(12_000):
    m = do_step(m)
import collections
c = collections.Counter()
for p, v in m.items():
    c[p[0]] += v
    c[p[1]] += v
l = c.most_common()
print((l[0][1] - l[-1][1]) // 2 + 1)
