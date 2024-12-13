from common import *
import functools
a = get_input()

@functools.cache
def solve(pos, da, db):
    if pos[0] < 0 or pos[1] < 0:
        return float("inf")
    if pos == (0, 0):
        return 0
    return min(
        solve(offset(pos, invert(da)), da, db) + 3,
        solve(offset(pos, invert(db)), da, db) + 1,
    )

c = 0
for mach in a:
    r = solve(tuple(mach["Prize"].nums), tuple(mach["Button A"].nums), tuple(mach["Button B"].nums))
    if r != float("inf"):
        c += r
print(c)
