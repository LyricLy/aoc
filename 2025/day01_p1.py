from common import *
a = get_input()

n = 50
c = 0
for line in a.items:
    r = -1 if line.string[0] == "L" else 1
    n = (n + r*line.num) % 100
    c += not n
print(c)
