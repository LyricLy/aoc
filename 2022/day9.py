from common import *
import itertools

def go(t):
    g = Grid(1000, 1000, False)
    head = 500, 500
    tails = [(500, 500)]*9
    for inst in t.splitlines():
        d, a = inst.split()
        for _ in range(int(a)):
            head = offset(head, orthagonals["URDL".index(d)])
            for h, (i, t) in zip(itertools.chain([head], tails), enumerate(tails)):
                delta = offset(h, invert(t))
                if not (h == t or is_normal(delta)):
                    tails[i] = offset(t, (*map(lambda x: -1 if x < 0 else 0 if x == 0 else 1, delta),))
            g[tails[-1]] = True
    return g.count(lambda x: x)
