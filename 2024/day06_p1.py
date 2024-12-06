from common import *
a = get_input().grid
guard_dir = (0, -1)
for p in a:
    if a[p] == "^":
        guard_pos = p
        a[p] = "."
        break

def show_guard():
    b = a.copy()
    b[guard_pos] = "$"
    print(b)

poses = set()
while True:
    if not a[guard_pos]:
        break
    if a[n := offset(guard_pos, guard_dir)] != "#":
        poses.add(guard_pos)
        guard_pos = n
    else:
        dx, dy = guard_dir
        guard_dir = -dy, dx
print(len(poses))
