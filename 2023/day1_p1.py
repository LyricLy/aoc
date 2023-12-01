with open("input.txt") as f:
    r = f.read()

import re
t = [int(x[0] + x[-1]) if (x := re.findall(r"\d", l)) or True else None for l in r.split("\n") if l]
print(sum(t))
