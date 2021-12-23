class Rod:
    def __init__(self, target, cap):
        self.target = target
        self.cap = cap
        self.ents = []

    def can_enter(self):
        return len(self.ents) < self.cap

    def can_pass(self):
        return self.target or self.can_enter()

    def is_done(self):
        return not self.target or len(self.ents) == self.cap and all(e == self.target for e in self.ents)

    def depth(self):
        r = self.cap-len(self.ents)
        if not self.target:
            r -= 1
        return r

min_cost = float('inf')
from collections import defaultdict
done = defaultdict(lambda: float('inf'))

class Thing:
    def __init__(self):
        self.rods = [Rod(None, 1), Rod(None, 1), Rod("A", 4), Rod(None, 1), Rod("B", 4), Rod(None, 1), Rod("C", 4), Rod(None, 1), Rod("D", 4), Rod(None, 1), Rod(None, 1)]
        example = False
        if example:
            self.rods[2].ents.extend(["A", "D", "D", "B"])
            self.rods[4].ents.extend(["D", "B", "C", "C"])
            self.rods[6].ents.extend(["C", "A", "B", "B"])
            self.rods[8].ents.extend(["A", "C", "A", "D"])
        else:
            self.rods[2].ents.extend(["C", "D", "D", "A"])
            self.rods[4].ents.extend(["C", "B", "C", "D"])
            self.rods[6].ents.extend(["D", "A", "B", "A"])
            self.rods[8].ents.extend(["B", "C", "A", "B"])

    def get_moves(self):
        moves = []
        for idx, er in enumerate(self.rods):
            if all(x == er.target for x in er.ents):
                continue
            top = er.ents[-1]
            if idx:
                idxk = idx
                for rod in self.rods[idx-1::-1]:
                    idxk -= 1
                    if rod.can_enter() and (rod.target == top and all(x == top for x in rod.ents) or rod.target is None and er.target is not None):
                        moves.append((idx, idxk))
                    if not rod.can_pass():
                        break
            for idxk, rod in enumerate(self.rods[idx+1:], start=idx+1):
                if rod.can_enter() and (rod.target == top and all(x == top for x in rod.ents) or rod.target is None and er.target is not None):
                    moves.append((idx, idxk))
                if not rod.can_pass():
                    break 
        return moves

    def get_answer(self, cost_so_far=0, moves=[]):
        global min_cost, best_moves
        o = tuple(tuple(x.ents) for x in self.rods)
        if cost_so_far >= done[o]:
            return
        done[o] = cost_so_far

        if all(r.is_done() for r in self.rods):
            min_cost = cost_so_far
            best_moves = moves
            print(min_cost)
            return
        
        for fro, to in self.get_moves():
            to_move = self.rods[fro].ents.pop()
            dist = self.rods[fro].depth() + self.rods[to].depth() + abs(fro-to)
            cost = {
                "A": 1,
                "B": 10,
                "C": 100,
                "D": 1000,
            }[to_move] * dist
            self.rods[to].ents.append(to_move)
            self.get_answer(cost_so_far+cost, moves+[(fro, to)])
            # put back
            self.rods[to].ents.pop()
            self.rods[fro].ents.append(to_move)

    def __repr__(self):
        s = "#############\n#"
        for rod in self.rods:
            if rod.target or not rod.ents:
                s += "."
            else:
                s += rod.ents[0]
        s += "#\n###"
        for rod in self.rods[2:-2]:
            if not rod.target:
                s += "#"
            elif len(rod.ents) < 4:
                s += "."
            else:
                s += rod.ents[3]
        s += "###\n  #"
        for rod in self.rods[2:-2]:
            if not rod.target:
                s += "#"
            elif len(rod.ents) < 3:
                s += "."
            else:
                s += rod.ents[2]
        s += "#  \n  #"
        for rod in self.rods[2:-2]:
            if not rod.target:
                s += "#"
            elif len(rod.ents) < 2:
                s += "."
            else:
                s += rod.ents[1]
        s += "#  \n  #"
        for rod in self.rods[2:-2]:
            if not rod.target:
                s += "#"
            elif not rod.ents:
                s += "."
            else:
                s += rod.ents[0]
        s += "#  \n  #########  "
        return s

t = Thing()
t.get_answer()
print(min_cost)
for fro, to in best_moves:
    to_move = t.rods[fro].ents.pop()
    t.rods[to].ents.append(to_move)
    print(t)