from common import *
import itertools
a = get_input()
p = 0, 0
l = []
for _, _, z in a.dechaff:
    n = int(z.string[:-1], 16)
    l.append(p)
    t = orthagonals[(int(z.string[-1])+1) % 4]
    p = offset(p, (t[0] * n, t[1] * n))

def getnth(i):
    return l[i % len(l)]

print(sum((y1+y2)*(x1-x2)+(abs(x1-x2)+(abs(y1-y2))) for i in range(len(l)) for ((x1, y1), (x2, y2)) in [[getnth(i), getnth(i+1)]]) // 2 + 1)
