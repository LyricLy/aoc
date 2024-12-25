from common import *
a = get_input()

keys = []
locks = []

for obj in a:
    g = obj.grid
    heights = tuple(g.height - 1 - len("".join(g.take(c)).strip("#")) for c in g.columns())
    if g[0, 0] == "#":
        locks.append(heights)
    else:
        keys.append(heights)

c = 0
from tqdm import tqdm
for key in tqdm(keys):
    for lock in locks:
        c += all([x + y < a[0].grid.height - 1 for x, y in zip(key, lock)])
print(c)
