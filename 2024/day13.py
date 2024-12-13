from common import *
from z3 import *
a = get_input()

def solve(pos, da, db):
    a = Int("a")
    b = Int("b")
    cost = Int("cost")
    s = Optimize()
    s.add(
        da[0]*a + db[0]*b == pos[0] + 10000000000000,
        da[1]*a + db[1]*b == pos[1] + 10000000000000,
        cost == a*3 + b,
    )
    s.minimize(cost)
    if s.check() != sat:
        return float("inf")
    m = s.model()
    return m[cost].as_long()

c = 0
for mach in a:
    r = solve(tuple(mach["Prize"].nums), tuple(mach["Button A"].nums), tuple(mach["Button B"].nums))
    if r != float("inf"):
        c += r
print(c)
