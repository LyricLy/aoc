from common import *
a = get_input()

fresh = rangeset()
for x in a[0]:
    fresh |= irange(*x)

print(len(fresh))
