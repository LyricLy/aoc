from common import *
import functools
a = get_input()

@functools.cache
def solve(haystack, needles):
    if not haystack:
        return 1
    c = 0
    for needle in needles:
        new = haystack.removeprefix(needle)
        if new != haystack:
            c += solve(new, needles)
    return c

needles = [x.string for x in a[0]]
c = 0
for haystack in a[1]:
    c += solve(haystack.string, tuple(needles))
print(c)
