import itertools


class Group:
    def __init__(self, ids, top, right, bottom, left):
        self.ids = ids
        self.groups = (top, right, bottom, left)

    @property
    def top(self):
        return self.groups[0]

    @property
    def right(self):
        return self.groups[1]

    @property
    def bottom(self):
        return self.groups[2]

    @property
    def left(self):
        return self.groups[3]

    def __repr__(self):
        return repr(self.groups)

    def rot(self):
        right, bottom, left, top = self.groups
        return Group(np.rot90(self.ids, -1), top, right, bottom, left)

    def flip_lr(self):
        top, left, bottom, right = self.groups
        return Group(np.fliplr(self.ids), top[::-1], right[::-1], bottom[::-1], left[::-1])

    def flip_ud(self):
        bottom, right, top, left = self.groups
        return Group(np.flipud(self.ids), top[::-1], right[::-1], bottom[::-1], left[::-1])

    def match(self, other):
        for r, f in itertools.product([(), (Group.rot,), (Group.rot, Group.rot), (Group.rot, Group.rot, Group.rot)], [(), (Group.flip_lr,), (Group.flip_ud,), (Group.flip_lr, Group.flip_ud)]):
            t = other
            for o in r + f:
                t = o(t)
            if self.right == t.left[::-1]:
                return Group(np.concatenate((self.ids, t.ids), 1), self.top + t.top, t.right, t.bottom + self.bottom, self.left)
            elif self.bottom == t.top[::-1]:
                return Group(np.concatenate((self.ids, t.ids), 0), self.top, self.right + t.right, t.bottom, t.left + self.left)
            elif self.left == t.right[::-1]:
                return Group(np.concatenate((t.ids, self.ids), 1), t.top + self.top, self.right, self.bottom + t.bottom, t.left)
            elif self.top == t.bottom[::-1]:
                return Group(np.concatenate((t.ids, self.ids), 0), t.top, t.right + self.right, self.bottom, self.left + t.left)
        return None

import numpy as np
import numpy.ma as ma

def g2n(g):
    t = np.array([[int(x == "#") for x in y[1:-1]] for y in g.splitlines()[1:-1]])
    return t

with open("input.txt") as f:
    data = f.read().split("\n\n")
    d = [Group(g2n(x[11:]), x[11:].replace("\n", "")[:10], x[11:].replace("\n", "")[9::10], x[11:].replace("\n", "")[:-11:-1], x[11:].replace("\n", "")[-10::-10]) for x in data]


import random
while len(d) > 1:
    for i, j in itertools.combinations(range(len(d)), r=2):
        r = d[i].match(d[j])
        if r is not None:
            d.pop(i)
            d.pop(j - (i<j))
            d.append(r)
            d.reverse()
            break
    else:
        print("no matches possible")
        break

img = d[0].ids

monster = [[int(x == "#") for x in y] for y in """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()]

for r, f in itertools.product([(), (lambda a: np.rot90(a, -1),), (lambda a: np.rot90(a, -2),), (lambda a: np.rot90(a, 1),)], [(), (np.fliplr,), (np.flipud,), (np.fliplr, np.flipud)]):
    t = img
    for o in r + f:
        t = o(t)
    c = 0
    for x, y in itertools.product(*map(range, t.shape)):
        for dx, dy in itertools.product(range(len(monster[0])), range(len(monster))):
            try:
                if monster[dy][dx] and not t[y + dy, x + dx]:
                    break
            except: break
        else:
            c += 1
    if c:
        break
print(np.sum(img) - (c * 15))
