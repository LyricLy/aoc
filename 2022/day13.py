example = 0
with open("example.txt" if example else "input.txt") as f:
    t = f.read()

pairs = [eval(y) for y in t.splitlines() if y]

def compare(left, right):
    match left, right:
        case int(), int():
            return -1 if left < right else 1 if left > right else 0
        case list(), list():
            for x, y in zip(left, right):
                if (m := compare(x, y)) is not 0:
                    return m
            if len(left) < len(right):
                return -1
            if len(right) < len(left):
                return 1
            return 0
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])

import functools
pairs.append([[6]])
pairs.append([[2]])
pairs.sort(key=functools.cmp_to_key(compare))

n = 1
for i, p in enumerate(pairs):
    if p in ([[6]], [[2]]):
        n *= i+1
print(n)
