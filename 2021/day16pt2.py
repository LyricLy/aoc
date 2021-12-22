from common import *

with open("input.txt") as f:
    t = bin(int(f.read(), 16))[2:]

if len(t) % 4:
    t = "0" * (4 - (len(t)%4)) + t


from functools import reduce

class StringView:
    def __init__(self, data):
        self.d = data
        self.i = 0

class Operator:
    def __init__(self, ver, i, ops):
        self.ver = ver
        self.id = i
        self.ops = ops

    def __repr__(self):
        return f"Operator(ver={self.ver}, id={self.id}, {self.ops})"

    def ver_sum(self):
        return self.ver + sum(x.ver_sum() for x in self.ops)

    def eval(self):
        if self.id == 0:
            return sum(x.eval() for x in self.ops)
        elif self.id == 1:
            return reduce(lambda x, y: x * y, (x.eval() for x in self.ops))
        elif self.id == 2:
            return min(x.eval() for x in self.ops)
        elif self.id == 3:
            return max(x.eval() for x in self.ops)
        elif self.id == 5:
            return int(self.ops[0].eval() > self.ops[1].eval())
        elif self.id == 6:
            return int(self.ops[0].eval() < self.ops[1].eval())
        elif self.id == 7:
            return int(self.ops[0].eval() == self.ops[1].eval())

class Literal:
    def __init__(self, ver, n):
        self.ver = ver
        self.n = n

    def __repr__(self):
        return f"Literal(ver={self.ver}, {self.n})"

    def ver_sum(self):
        return self.ver

    def eval(self):
        return self.n

def parse_packet(v):
    ver = int(v.d[v.i:v.i+3], 2)
    id = int(v.d[v.i+3:v.i+6], 2)
    v.i += 6
    if id == 4:
        num = ""
        while True:
            group = v.d[v.i:v.i+5]
            v.i += 5
            num += group[1:]
            if group[0] == "0":
                break
        return Literal(ver, int(num, 2))
    else:
        ty = v.d[v.i]
        v.i += 1
        ops = []
        if ty == "0":
            n = int(v.d[v.i:v.i+15], 2)
            v.i += 15
            target = v.i + n
            while v.i < target:
                ops.append(parse_packet(v))
        else:
            n = int(v.d[v.i:v.i+11], 2)
            v.i += 11
            for _ in range(n):
                ops.append(parse_packet(v))
        return Operator(ver, id, ops)

print(parse_packet(StringView(t)))
