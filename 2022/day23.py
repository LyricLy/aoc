example = 0

with open("example.txt" if example else "input.txt") as f:
    t = f.read()

from common import Grid, offset, directions
from collections import Counter, deque, defaultdict

og = Grid.parse(t, lambda x: x)
g = Grid(1000, 1000, ".")
for p in og:
    g[offset(p, (50-(og.width//2), 50-(og.height//2)))] = og[p]
ds = deque([((0, -1), (1, -1), (-1, -1)), ((0, 1), (1, 1), (-1, 1)), ((-1, 0), (-1, -1), (-1, 1)), ((1, 0), (1, -1), (1, 1)),])

elves = set()
for p in g:
    if g[p] == "#":
        elves.add(p)

def do_round():
    propositions = defaultdict(list)
    elf_moved = False
    for p in elves:
        for d in directions:
            if g[offset(p, d)] == "#":
                break
        else:
            continue
        elf_moved = True
        for target, not_this, or_this in ds:
            if "#" not in [g[aa] for x in (target, not_this, or_this) if (aa := offset(p, x)) is not None]:
                propositions[offset(p, target)].append(p)
                break
    for s, l in propositions.items():
        if len(l) != 1:
            continue
        g[s] = "#"
        elves.add(s)
        g[l[0]] = "."
        elves.remove(l[0])
    ds.rotate(-1)
    return elf_moved

i = 1
while True:
    if not do_round():
        break
    i += 1
print(i)
