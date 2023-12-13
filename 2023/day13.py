from common import *
a = get_input()

def matches(x, y):
    return x is None or y is None or x == y

def line_of(g, is_not):
    for p in range(g.width-1):
        if all([matches(g[x, y], g[p*2-x + 1, y]) for x, y in g]):
            r = ("l", p+1)
            if r != is_not:
                return r
    for p in range(g.height-1):
        if all([matches(g[x, y], g[x, p*2-y + 1]) for x, y in g]):
            r = ("-", p+1)
            if r != is_not:
                return r
    return None

c = 0
for g in a:
    g = g.grid
    st = line_of(g, None)
    for p in g:
        tmp = g[p]
        g[p] = ".#"[tmp == "."]
        if l := line_of(g, st):
            match l:
                case ("l", hh):
                    c += hh
                case ("-", hh):
                    c += 100*hh
            break
        g[p] = tmp
print(c)
