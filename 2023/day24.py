from common import *
import z3
a = get_input()
hailstones = []
for l in a:
    x, y = l.split("@")
    hailstones.append((x.nums, y.nums))

x = z3.Int("x")
y = z3.Int("y")
z = z3.Int("z")
dx = z3.Int("dx")
dy = z3.Int("dy")
dz = z3.Int("dz")

s = z3.Solver()

for i, ((x_, y_, z_), (dx_, dy_, dz_)) in enumerate(hailstones):
    t = z3.Int(f"t_{i}")
    s.add(t >= 0)
    s.add(x + dx * t == x_ + dx_ * t)
    s.add(y + dy * t == y_ + dy_ * t)
    s.add(z + dz * t == z_ + dz_ * t)

s.check()
m = s.model()
print(m[x] + m[y] + m[z])
