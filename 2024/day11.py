from common import *
import functools
from collections import Counter
a = Counter([int(x) for x in str(get_input()).split()])

@functools.cache
def answer_of(stone):
    s = str(stone)
    l = len(s)
    return [1] if not stone else [stone*2024] if l % 2 else [int(s[:l//2]), int(s[l//2:])]

for i in range(75):
    print(i)
    b = Counter()
    for stone, count in a.items():
        for others in answer_of(stone):
            b[others] += count
    a = b

print(sum(a.values()))
