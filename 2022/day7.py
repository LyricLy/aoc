from collections import defaultdict

def go(t):
    lines = t.splitlines()
    i = 0
    def next_line():
        nonlocal i
        i += 1
        return lines[i-1]
    f = lambda: defaultdict(f)
    a = f()
    current_path = []
    while i < len(lines):
        cmd = next_line().removeprefix("$ ").split()
        match cmd:
            case ["cd", ".."]:
                current_path.pop()
            case ["cd", "/"]:
                current_path.clear()
            case ["cd", x]:
                current_path.append(x)
            case ["ls"]:
                b = a
                for x in current_path:
                    b = b[x]
                while i < len(lines) and not lines[i].startswith("$"):
                    size, name = next_line().split()
                    if size == "dir": continue
                    b[name] = int(size)
    needed = 30000000 - (70000000 - total_size(a))
    return min(x for x in total_sizes(a) if x >= needed)

def total_size(d):
    s = 0
    for x in d.values():
        if isinstance(x, int):
            s += x
        else:
            s += total_size(x)
    return s

def total_sizes(d):
    s = [total_size(d)]
    for x in d.values():
        if not isinstance(x, int):
            s.extend(total_sizes(x))
    return s
