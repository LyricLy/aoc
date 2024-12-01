from common import *
a = get_input()

x, y = zip(*[b.nums for b in a])
x = sorted(x)
y = sorted(y)
print(sum(abs(n - m) for n, m in zip(x, y)))
