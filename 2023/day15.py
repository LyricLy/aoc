from common import *
a = Aoc(get_input().string.replace("\n",""))

def h(s):
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current %= 256
    return current

t = [{} for _ in range(256)]

for a, b in a.split(","):
    box = h(a.string)
    if not b.string:
        t[box].pop(a, None)
    else:
        t[box][a] = b.num

c = 0
for i in range(256):
    for j, l in enumerate(t[i].values(), 1):
        c += (i+1)*j*l
print(c)
