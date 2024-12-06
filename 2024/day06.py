from common import *
from tqdm import tqdm
a = get_input().grid

for p in a:
    if a[p] == "^":
        guard_pos_og = p
        a[p] = "."
        break

def loops(a):
    states = set()
    guard_pos = guard_pos_og
    guard_dir = (0, -1)
    while True:
        if not a[guard_pos]:
            return False
        if a[n := offset(guard_pos, guard_dir)] != "#":
            guard_pos = n
        else:
            dx, dy = guard_dir
            guard_dir = -dy, dx
        state = guard_pos, guard_dir
        if state in states:
            return True
        states.add(state)

c = 0
for p in tqdm(a, total=a.width * a.height):
    b = a.copy()
    b[p] = "#"
    c += loops(b)
print(c)
