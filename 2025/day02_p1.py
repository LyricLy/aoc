from common import *
a = get_input()

c = 0
for x, y in a:
    for n in irange(x, y):
        s = str(n)
        p = len(s)//2
        if s[p:] == s[:p]:
            c += n
print(c)
