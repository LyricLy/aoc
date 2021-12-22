with open("input.txt") as f:
    t = f.read()

import itertools 
import copy
digits = [
    [0, 1, 2, 4, 5, 6],
    [2, 5],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 5, 6],
    [1, 2, 3, 5],
    [0, 1, 3, 5, 6],
    [0, 1, 3, 4, 5, 6],
    [0, 2, 5],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 5, 6],
]

things = t.splitlines()
s = 0

def is_possible(m, example, digit):
    if not digit:
        return not example
    p = digit[0]
    for c in example:
        if p in m[c] and is_possible(m, example.replace(c, ""), digit[1:]):
            return True
    return False

def have_soln(m):
    return all(len(v) == 1 for v in m.values())

def consistify(m):
    for k, v in m.items():
        if len(v) == 1:
            for k2, v2 in m.items():
                if k != k2:
                    v2.discard(list(v)[0])
                

def get_m(examples, m=None):
    m = m or {
        "a": {*range(0, 7)},
        "b": {*range(0, 7)},
        "c": {*range(0, 7)},
        "d": {*range(0, 7)},
        "e": {*range(0, 7)},
        "f": {*range(0, 7)},
        "g": {*range(0, 7)},
    }
    examples, output = thing.split(" | ")
    for example in examples.split():
        possible_digits = [x for x in range(0, 10) if is_possible(m, example, digits[x])]
        d = set(range(0, 7))
        for digit in possible_digits:
            for s in digits[digit]:
                d.discard(s)
        for h in d:
            for k, v in m.items():
                if k in example:
                    v.discard(h)
        consistify(m)
    if not have_soln(m):
        for k in m:
            if len(m[k]) == 1:
                continue
            for v in m[k]:
                g = copy.deepcopy(m)
                g[k] = {v}
                r = get_m(examples, g)
                if have_soln(r):
                    return r
    return m

import time
start = time.time()
s = 0
for thing in things:
    examples, output = thing.split(" | ")
    m = get_m(examples)
    st = ""
    for ch in output.split():
        d = []
        for c in ch:
            d.append(list(m[c])[0])
        for digit, dd in enumerate(digits):
            if set(d) == set(dd):
                st += str(digit)
                break
    s += int(st)
print(s)
print(time.time() - start)
