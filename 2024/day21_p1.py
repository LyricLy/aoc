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

@functools.cache
def convert(seq, pad, current=None, i=0):
    current = current or pos_of(pad, "A")
    if i >= len(seq):
        return [""]
    c = seq[i]
    if pad[current] == c:
        return ["A" + path for path in convert(seq, pad, current, i+1)]
    target = pos_of(pad, c)
    dx, dy = offset(invert(current), target)
    steps = []
    if dy > 0 and " " not in pad[current[0], current[1]:target[1]+1]:
        steps.append(("v" * dy, (0, dy)))
    if dy < 0 and " " not in pad[current[0], target[1]:current[1]]:
        steps.append(("^" * -dy, (0, dy)))
    if dx > 0 and " " not in pad[current[0]:target[0]+1, current[1]]:
        steps.append((">" * dx, (dx, 0)))
    if dx < 0 and " " not in pad[target[0]:current[0], current[1]]:
        steps.append(("<" * -dx, (dx, 0)))
    paths = []
    for step, d in steps:
        paths.extend(step + path for path in convert(seq, pad, offset(current, d), i))
    if not paths:
        print("sad!", dx, dy, current, pad)
    best = min(len(path) for path in paths)
    return [path for path in paths if len(path) == best]

def mass_convert(seqs, pad):
    paths = []
    for seq in seqs:
        paths.extend(convert(seq, pad))
    best = min(len(path) for path in paths)
    return [path for path in paths if len(path) == best]

def eval_path(seq, pad):
    pos = pos_of(pad, "A")
    out = ""
    for c in seq:
        match c:
            case "^":
                pos = offset(pos, (0, -1))
            case "v":
                pos = offset(pos, (0, 1))
            case ">":
                pos = offset(pos, (1, 0))
            case "<":
                pos = offset(pos, (-1, 0))
            case "A":
                out += pad[pos]
        if pad[pos] in (" ", None):
            raise ValueError("WENT OOB!")
    return out

c = 0
for code in a.items:
    ans = mass_convert(mass_convert(convert(code.string, final_pad), dir_pad), dir_pad)
    print(ans[0], len(ans[0]), code, eval_path(eval_path(eval_path(ans[0], dir_pad), dir_pad), final_pad))
    c += len(ans[0]) * int(code.string[:-1])
print(c)
