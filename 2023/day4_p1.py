from common import *

with open("input.txt") as f:
    r = f.read().split("\n")[:-1]

hh = 0
for card in r:
    a, b = card.split(": ")
    id = int(a.split()[-1])
    c, d = b.split(" | ")
    winning = [int(x) for x in c.split()]
    gaming = [int(x) for x in d.split()]
    bb = sum(x in winning for x in gaming)
    if bb:
        hh += 2**(bb-1)
print(hh)
