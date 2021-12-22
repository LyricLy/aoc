with open("input.txt") as f:
    t = [int(x) for x in f.read().split(",")]

from collections import defaultdict
counts = defaultdict(int)
for fish in t:
    counts[fish] += 1
for n in range(0, 256):
    counts[n+9] += counts[n]
    counts[n+7] += counts[n]
n += 1
print(sum(v for (k, v) in counts.items() if k >= n))
