from common import *
from collections import Counter
a = get_input().grid
agnes = Counter([a.extract("S", ".")[0]])
for row in range(a.height):
    new = Counter()
    for agne, c in agnes.items():
        if a[agne, row] == "^":
            new[agne-1] += c
            new[agne+1] += c
        else:
            new[agne] += c
    agnes = new
print(agnes.total())
