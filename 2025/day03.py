from common import *
a = get_input()

c = 0
for line in a.strings:
    i = 0
    r = ""
    for left in irange(11, 0):
        i, x = max(enumerate(line[i:-left or None], start=i+1), key=lambda x: x[1])
        r += x
    c += int(r)
print(c)
