from common import *
import re
a = get_input()

def solve(haystack, needles):
    if not haystack:
        return True
    for needle in needles:
        new = haystack.removeprefix(needle)
        if new != haystack and solve(new, needles):
            return True
    return False

needles = [x.string for x in a[0]]
c = 0
for haystack in a[1]:
    c += solve(haystack.string, needles)
print(c)
