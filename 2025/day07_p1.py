from common import *
a = get_input().grid
agnes = Counter([a.extract("S", ".")[0]])
c = 0
for row in range(a.height):
    agnes = {x for agne in agnes for x in ([agne] if a[agne, row] != "^" else globals().__setitem__("c", c + 1) or [agne-1, agne+1])}
print(c)
