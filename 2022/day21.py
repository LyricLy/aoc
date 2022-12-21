example = 0

with open("example.txt" if example else "input.txt") as f:
    t = f.read()

monkeys = {x: y for line in t.splitlines() for x, y in [line.split(": ")]}

def do_op(op, x, y):
    match op:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y

def invert_op(op, x, y, wanted):
    either = x if x is not None else y
    match op, x, y:
        case "+", *_:
            return wanted - either
        case "*", *_:
            return wanted / either
        case "-", _, None:
            return x - wanted
        case "-", None, _:
            return y + wanted
        case "/", _, None:
            return x / wanted
        case "/", None, _:
            return y * wanted 

def evaluate(m):
    s = monkeys[m]
    if m == "humn":
        return None
    if s.isdigit():
        return int(s)
    x, op, y = s.split()
    x = evaluate(x)
    y = evaluate(y)
    if x is None or y is None:
        return None
    return do_op(op, x, y)

def antivaluate(m, wanted_value):
    if m == "humn":
        return wanted_value
    s = monkeys[m]
    x, op, y = s.split()
    if evaluate(x) is None:
        return antivaluate(x, invert_op(op, None, evaluate(y), wanted_value))
    else:
        return antivaluate(y, invert_op(op, evaluate(x), None, wanted_value))

left, right = monkeys["root"].split()[::2]
if (solid := evaluate(left)) is None:
    solid = evaluate(right)
    bendy = left
else:
    bendy = right
print(antivaluate(bendy, solid))
