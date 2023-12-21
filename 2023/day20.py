from common import *
from collections import defaultdict, deque
a = get_input()

class And:
    def __init__(self, name, targets):
        self.name = name
        self.targets = targets
        self.state = {}

    def you_have_an_input(self, inputter):
        self.state[inputter] = False

    def call(self, inputter, val):
        self.state[inputter] = val
        pulse(self, not all(self.state.values()))

class FlipFlop:
    def __init__(self, name, targets):
        self.name = name
        self.targets = targets
        self.state = False

    def you_have_an_input(self, _):
        pass

    def call(self, _, val):
        if not val:
            self.state = not self.state
            pulse(self, self.state)

class Null:
    def __init__(self, name):
        self.name = name
        self.targets = []

    def you_have_an_input(self, _):
        pass

    def call(self, _, __):
        pass


class Broadcaster:
    def __init__(self, targets):
        self.name = "broadcaster"
        self.targets = targets

things = {}
for name, targets in a:
    t, *name = name.string
    name = "".join(name)
    targets = [x.string for x in targets.split(",")]
    if t == "%":
        things[name] = FlipFlop(name, targets)
    elif t == "&":
        things[name] = And(name, targets)
    else:
        broadcaster = Broadcaster(targets)

for name, t in list(things.items()):
    for target in t.targets:
        if target not in things:
            things[target] = Null(target)
        things[target].you_have_an_input(name)

q = deque()
def pulse(me, height):
    q.extend((me.name, target, height) for target in me.targets)

def do():
    pulse(broadcaster, False)
    while q:
        name, target, val = q.popleft()
        if target == "zh" and val:
            print(name, i)
        things[target].call(name, val)

i = 0
while True:
    do()
    i += 1
