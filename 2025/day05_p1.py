from common import *
a = get_input()

fresh = rangeset()
for x in a[0]:
    fresh |= irange(*x)

c = 0
for x in a[1]:
    c += x in fresh
print(c)
