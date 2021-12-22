from __future__ import annotations

with open("input.txt") as f:
    t = f.read()

class Pair:
    left: int | Pair
    right: int | Pair

    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None

    @classmethod
    def from_list(cls, ls):
        if type(ls) == int:
            return ls
        t = cls()
        t.left = Pair.from_list(ls[0])
        if isinstance(t.left, Pair):
            t.left.parent = t
        t.right = Pair.from_list(ls[1])
        if isinstance(t.right, Pair):
            t.right.parent = t
        return t

    def magnitude(self):
        s = 0
        if isinstance(self.left, int):
            s = self.left
        else:
            s = self.left.magnitude()
        if isinstance(self.right, int):
            r = self.right
        else:
            r = self.right.magnitude()
        return s*3+r*2

    def __repr__(self):
        return f"[{self.left},{self.right}]"

ls = [eval(x) for x in t.splitlines()]

def try_explode(num, nest):
    if isinstance(num, Pair):
        r = try_explode(num.left, nest+1)
        if r == 2:
            num.left = 0
            return True
        elif r:
            return True
        if nest >= 4 and isinstance(num.left, int) and isinstance(num.right, int):
            t = num
            while True:
                if t.parent is None:
                    t = None
                    break
                if t.parent.left != t:
                    if type(t.parent.left) == int:
                        t.parent.left += num.left
                        t = None
                        break
                    t = t.parent.left
                    break
                t = t.parent
            if t:
                while True:
                    if isinstance(t.right, int):
                        t.right += num.left
                        break
                    t = t.right
            r = num
            while True:
                if r.parent is None:
                    r = None
                    break
                if r.parent.right != r:
                    if type(r.parent.right) == int:
                        r.parent.right += num.right
                        r = None
                        break
                    r = r.parent.right
                    break
                r = r.parent
            if r:
                while True:
                    if isinstance(r.left, int):
                        r.left += num.right
                        break
                    r = r.left
            return 2
        r = try_explode(num.right, nest+1)
        if r == 2:
            num.right = 0
            return True
        elif r:
            return True
        return False
    else:
        return False

import math
def try_split(num):
    if isinstance(num, int):
        return False
    if isinstance(num.left, int) and num.left >= 10:
        n = num.left
        num.left = Pair()
        num.left.left = n//2
        num.left.right = math.ceil(n/2)
        num.left.parent = num
        return True
    elif try_split(num.left):
        return True
    elif isinstance(num.right, int) and num.right >= 10:
        n = num.right
        num.right = Pair()
        num.right.left = n//2
        num.right.right = math.ceil(n/2)
        num.right.parent = num
        return True
    elif try_split(num.right):
        return True
    else:
        return False

def reduce(num):
    if try_explode(num, 0):
        reduce(num)
    elif try_split(num):
        reduce(num)

import itertools
l = []
for x, y in itertools.permutations(ls, 2):
    new = Pair()
    new.left = Pair.from_list(x)
    new.left.parent = new
    new.right = Pair.from_list(y)
    new.right.parent = new
    reduce(new)
    l.append(new.magnitude())
print(max(l))
