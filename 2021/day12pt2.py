with open("input.txt") as f:
    t = f.read()

from collections import defaultdict
connections = defaultdict(list)
for l in t.splitlines():
    if not l:
        continue
    s, e = l.split("-")
    connections[s].append(e)
    connections[e].append(s)

def possible_paths(s, b=None, d=True):
    b = b or defaultdict(int)
    p = 0
    if s == "end":
        return 1
    for k in connections[s]:
        if ((d and b[k] < 2) or (b[k] < 1)) and k != "start":
            nd = d
            if b[k] == 1:
                nd = False
            nb = b.copy()
            if s.islower():
                nb[s] += 1
            p += possible_paths(k, nb, nd)
    return p

print(possible_paths("start"))
