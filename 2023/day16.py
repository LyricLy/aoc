from common import *
a = get_input().grid
answers = 0
for sp in a.rows()[0] + a.rows()[-1] + a.columns()[0] + a.columns()[-1]:
    for sd in orthagonals:
        b = set()

        ps = [(sp, sd)]
        seen = set()

        while ps:
            p, d = ps.pop()
            while p in a and (p, d) not in seen:
                seen.add((p, d))
                b.add(p)
                x, y = d
                c = a[p]
                if c == "/":
                    if x:
                        d = (y, -x)
                    else:
                        d = (-y, x)
                elif c == "\\":
                    if x:
                        d = (-y, x)
                    else:
                        d = (y, -x)
                elif c == "|" and x or c == "-" and y:
                    d = (y, -x)
                    ps.append((p, (-y, x)))
                p = offset(p, d)
        answers = max(answers, len(b))
print(answers)
