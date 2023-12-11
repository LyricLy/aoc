from common import *
from collections import Counter
from functools import cmp_to_key
a = get_input()

strs = "AKQT98765432J"
def _get_hand_type(x):
    assert len(x) == 5
    p = Counter(x)
    if 5 in p.values():
        return 6
    if 4 in p.values():
        return 5
    if 3 in p.values() and 2 in p.values():
        return 4
    if 3 in p.values():
        return 3
    if list(p.values()).count(2) == 2:
        return 2
    if 2 in p.values():
        return 1
    return 0

def get_hand_type(x):
    posses = [""]
    for c in x:
        new_posses = []
        for pos in posses:
            if c == "J":
                for ccc in strs:
                    if ccc == "J":
                        continue
                    new_posses.append(pos + ccc)
            else:
                new_posses.append(pos + c)
        posses = new_posses
    return max(_get_hand_type(p) for p in posses)

def valify(x):
    return [strs[::-1].index(c) for c in x]

def hand_cmp(x, y):
    tx = get_hand_type(x)
    ty = get_hand_type(y)
    if tx > ty:
        return 1
    if tx < ty:
        return -1
    vx = valify(x)
    vy = valify(y)
    if vx < vy:
        return -1
    if vx == vy:
        return 0
    if vx > vy:
        return 1

cards = [(x[0].string, x[1].num) for x in a.items]
cards.sort(key=cmp_to_key(lambda x, y: hand_cmp(x[0], y[0])))
c = 0
for i, (_, r) in enumerate(cards, start=1):
    c += i * r
print(c)
