from common import *
a = get_input()

def parse_workflow(s):
    name, body = s.split("{", 1)
    cases = body.rstrip("}").split(",")
    cases = [c.split(":") if ":" in c else ("True", c) for c in cases]
    return name, cases

workflows = {
    "A": [("True", True)],
    "R": [("True", False)],
}
for workflow in a[0]:
    name, cases = parse_workflow(workflow.string)
    workflows[name] = cases

def parse_bad_dict(s):
    return eval(s.replace("=", ":"), {"x": "x", "m": "m", "a": "a", "s": "s"})

def accepts(workflow, x):
    for cond, r in workflows[workflow]:
        if eval(cond, x):
            break
    if isinstance(r, bool):
        return r
    return accepts(r, x)

c = 0
for d in a[1]:
    d = parse_bad_dict(d.string)
    if accepts("in", d):
        d.pop("__builtins__")
        c += sum(d.values())
print(c)
