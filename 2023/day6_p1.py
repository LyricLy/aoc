from common import *

with open("input.txt") as f:
    r = Aoc(f.read())

time = r["Time"].nums
distance = r["Distance"].nums

c = 1
for t, record in zip(time, distance):
    rr = 0
    for x in range(t):
        if (t - x) * x > record:
            rr += 1
    c *= rr
print(c)
