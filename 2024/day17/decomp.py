from common import *
a = get_input()

def eval_combo(n):
    if n < 4:
        return str(n)
    return "abc"[n - 4]

prog = a[1].nums
i = 0
while i < len(prog):
    op = prog[i]
    erand = prog[i+1]
    i += 2
    print(f"{i:02}: ", end="")
    match op:
        case 0:
            print(f"a >>= {eval_combo(erand)}")
        case 1:
            print(f"b ^= {erand}")
        case 2:
            print(f"b = {eval_combo(erand)} % 8")
        case 3:
            print(f"jnz a, {erand}")
        case 4:
            print("b ^= c")
        case 5:
            print(f"out {eval_combo(erand)} % 8")
        case 6:
            print(f"b = a >> {eval_combo(erand)}")
        case 7:
            print(f"c = a >> {eval_combo(erand)}")
