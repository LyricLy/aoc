import common

def go(t):
    trees = common.Grid.parse(t, int)
    visible = trees.copy()
    css = []
    for x, y in trees:
        us = trees[x, y]
        row = trees.rows()[y]
        col = trees.columns()[x]
        a, b = row[:x], row[x+1:]
        c, d = col[:y], col[y+1:]
        cs = 1
        for l in (reversed(a), b, reversed(c), d):
            c = 0
            for p in trees.take(l):
                c += 1
                if p >= us:
                    break
            cs *= c
        css.append(cs)
    return max(css)
