with open("input.txt") as f:
    rules, msg = f.read().split("\n\n")

import lark
import re
t = lark.Lark(re.sub("(\d+)", r"t\1", rules), start="t0")
c = 0
for m in msg.splitlines():
    try:
        t.parse(m)
        c += 1
    except:
        pass
print(c)
