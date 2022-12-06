import re
from common import Grid

with open("input.txt") as f:
    head, insts = f.read().split("\n\n")

grid = Grid.parse(head, lambda x: x[1], lambda s: [s[i:i+4] for i in range(0, len(s), 4)])
towers = [list(filter(str.strip, reversed(grid.take(x))))[1:] for x in grid.columns()]

for inst in insts.splitlines():
    count, start, end = map(int, re.findall("\d+", inst))
    s = towers[start-1]
    towers[end-1].extend(s[-count:])
    del s[-count:]

print("".join([tower[-1] for tower in towers]))
