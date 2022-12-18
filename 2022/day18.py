from functools import cache

example = 0
with open("example.txt" if example else "input.txt") as f:
    t = f.read()

g = set()

for line in t.splitlines():
    g.add(eval(line))

mx = min(x for x, _, _ in g)
my = min(y for _, y, _ in g)
mz = min(z for _, _, z in g)
Mx = max(x for x, _, _ in g)
My = max(y for _, y, _ in g)
Mz = max(z for _, _, z in g)

@cache
def is_trapped(p):
    a = [p]
    done = set()
    while a:
        b = a.pop()
        if b in g or b in done:
            continue
        done.add(b)
        if not mx <= b[0] <= Mx or not my <= b[1] <= My or not mz <= b[2] <= Mz:
            return False
        for n in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            x, y, z = b
            dx, dy, dz = n
            a.append((x+dx,y+dy,z+dz))
    return b
    

s = 0
for p in g:
    for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        x, y, z = p
        dx, dy, dz = d
        dp = (x+dx,y+dy,z+dz)
        if not is_trapped(dp):
            s += 1
print(s)
