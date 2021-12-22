with open("input.txt") as f:
    t = f.read()

open2close = {
    "<": ">",
    "(": ")",
    "[": "]",
    "{": "}",
}

close2open = {v: k for k, v in open2close.items()}

s = []
def do_line(l):
    stack = []
    for c in l:
        if c not in "[]()<>{}":
            continue
        if c in open2close:
            stack.append(c)
        elif c in close2open:
            if stack[-1] != close2open[c]:
                return
            else:
                stack.pop()
    score = 0
    for t in stack[::-1]:
        score *= 5
        score += {")": 1, "]": 2, "}": 3, ">": 4}[open2close[t]]
    s.append(score)
for line in t.splitlines():
    do_line(line)
print(s)
s.sort()
print(s[len(s)//2])
