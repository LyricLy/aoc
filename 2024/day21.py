from common import *
import functools
a = get_input()

final_pad = Grid.parse("""
789
456
123
 0A
""".strip("\n"))

dir_pad = Grid.parse("""
 ^A
<v>
""".strip("\n"))

def pos_of(grid, x):
    for p, y in grid.items():
        if y == x:
            return p
    assert False

def do_actions(beneath, pad, actions):
    last_action = "A"
    c = 0
    for action in actions:
        c += (r := do_action(beneath, pad, action, last_action))
        last_action = action
    return c

@functools.cache
def do_action(beneath, pad, action, last_action):
    if not beneath:
        # we (the human) control this pad and can press any button
        return 1
    # there's a robot controlling this pad that needs to be directed
    current = pos_of(pad, last_action)
    target = pos_of(pad, action)
    dx, dy = target[0] - current[0], target[1] - current[1]
    horizontal = "<"*-dx if dx < 0 else ">"*dx
    vertical = "^"*-dy if dy < 0 else "v"*dy
    return min([
        *[do_actions(beneath-1, dir_pad, horizontal+vertical+"A")]*(pad[offset(current, (dx, 0))] != " "),
        *[do_actions(beneath-1, dir_pad, vertical+horizontal+"A")]*(pad[offset(current, (0, dy))] != " "),
    ])

c = 0
for code in a.items:
    c += do_actions(26, final_pad, str(code))*int(str(code)[:-1])
print(c)
