import math
from common import *
a = get_input()

c = 0
for x in zip(*[x.split() for x in a]):
    if x[-1] == "*":
        c += math.prod(t.num for t in x[:-1])
    else:
        c += sum(t.num for t in x[:-1])
print(c)
