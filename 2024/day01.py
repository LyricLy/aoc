from common import *
a = get_input()

x, y = zip(*[b.nums for b in a])
x = sorted(x)
y = sorted(y)
print(sum(n * y.count(n) for n in x))
