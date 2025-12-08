from common import *
a = get_input()

c = 0
for line in a.strings:
    i, x = max(enumerate(line[:-1]), key=lambda x: x[1])
    y = max(line[i+1:])
    c += int(x + y)
print(c)
