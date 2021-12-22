with open("input.txt") as f:
    data = [*map(int, f.read().split(","))]

from collections import defaultdict
base = 0
been_since = defaultdict(int)
for t in data:
    base += 1
    been_since[t] = base
last_bean = base

from tqdm import tqdm

for _ in tqdm(range(30000000-len(data))):
    a = base-last_bean
    base += 1
    last_bean = been_since[a]
    if last_bean == 0:
        last_bean = base
    been_since[a] = base

print(a)
