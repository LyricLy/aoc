from common import *

with open("input.txt") as f:
    r = Aoc(f.read())

t = int("".join(r["Time"].body.split()))
record = int("".join(r["Distance"].body.split()))

rr = 0
for x in range(t):
    if (t - x) * x > record:
        rr += 1
print(rr)
