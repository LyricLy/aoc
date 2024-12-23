from common import *
from collections import defaultdict
a = get_input()

MASK = 0xFFFFFF

def step(n):
    n = (n << 6 ^ n) & MASK
    n = (n >> 5 ^ n) & MASK
    return (n << 11 ^ n) & MASK

scores = defaultdict(int)

for x in a:
    prices = []
    for _ in range(2000):
        prices.append(x % 10)
        x = step(x)
    changes = []
    for i, x in enumerate(prices[1:], start=1):
        changes.append(prices[i] - prices[i-1])
    seen = set()
    for i, x in enumerate(prices[4:]):
        cs = tuple(changes[i:i+4])
        if cs in seen:
            continue
        seen.add(cs)
        scores[cs] += x
print(max(scores.items(), key=lambda x: x[1]))
