from common import *
a = get_input()

n = 50
c = 0
for line in a.items:
    r = -1 if line.string[0] == "L" else 1
    was = not n
    n += r*line.num
    if r == -1:
        c += abs(n // 100) + (not n % 100) - was
    else:
        c += abs(n // 100) + (not n)
    n %= 100
print(c)
