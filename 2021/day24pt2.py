import functools

l = list(zip(
    [14, 11, 12, 11, -10, 15, -14, 10, -4, -3, 13, -3, -9, -12],
    [False, False, False, False, True, False, True, False, True, True, False, True, True, True],
    [16, 3, 2, 7, 13, 6, 10, 11, 6, 5, 11, 4, 4, 6]
))

@functools.cache
def try_input(stack=None, i=0):
    if i == 14:
        if not stack:
            return []
        else:
            return None
    stack = list(stack) if stack else []
    rs = []
    for dg in range(1, 10):
        sc = stack.copy()
        e, p, d = l[i]
        if (dg != sc[-1]+e) if sc else (dg != e):
            sc.append(dg+d)
        if sc and p:
            sc.pop()
        if (rl := try_input(tuple(sc), i+1)) is not None:
            return [dg] + rl

def monad(inps):
    stack = []
    for inp, e, p, d in zip(
        inps,
        [14, 11, 12, 11, -10, 15, -14, 10, -4, -3, 13, -3, -9, -12],
        [False, False, False, False, True, False, True, False, True, True, False, True, True, True],
        [16, 3, 2, 7, 13, 6, 10, 11, 6, 5, 11, 4, 4, 6]
    ):
        if (inp != stack[-1]+e) if stack else (inp != e):
            stack.append(inp+d)
        if stack and p:
            stack.pop()
    return not stack

r = try_input()
print("".join(str(x) for x in r))
print(monad(r))
