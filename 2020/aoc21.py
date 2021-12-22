import re


with open("input.txt") as f:
    input = f.read()

d = []

for m in re.finditer(r"(.*)\(contains (.*)\)", input):
    d.append((m.group(1).split(), m.group(2).split(", ")))

from collections import defaultdict, Counter
ps = {}

for i_s, a_s in d:
    for a in a_s:
        try:
            ps[a] &= set(i_s)
        except KeyError:
            ps[a] = set(i_s)

t = list(sorted(ps.items(), key=lambda l: len(l[1])))
aa = []
while t:
    x, y = t.pop(0)
    if len(y) != 1:
        t.append((x, y))
        t.sort(key=lambda l: len(l[1]))
        continue
    r = list(y)[0]
    print(f"{x} = {r}")
    aa.append((x, r))
    for _, y_ in t:
        y_.discard(r)

print(",".join(x[1] for x in sorted(aa, key=lambda l: l[0])))
