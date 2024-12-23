from common import *
a = get_input()

MASK = 0xFFFFFF

def step(n):
    n = (n << 6 ^ n) & MASK
    n = (n >> 5 ^ n) & MASK
    return (n << 11 ^ n) & MASK

c = 0
for x in a:
    for _ in range(2000):
        x = step(x)
    c += x
print(c)
