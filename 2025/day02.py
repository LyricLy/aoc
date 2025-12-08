from common import *
import re
a = get_input()

c = 0
for x, y in a:
    for n in irange(x, y):
        if re.fullmatch(r"(.+)\1+", str(n)):
            c += n
print(c)
