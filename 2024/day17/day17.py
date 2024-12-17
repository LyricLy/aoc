from common import *
a = get_input()

prog = a[1].nums

def try_it(n):
    registers = [n, 0, 0]
    def eval_combo(t):
        if t < 4:
            return t
        return registers[t - 4]

    outputs = []

    i = 0
    while i < len(prog):
        op = prog[i]
        erand = prog[i+1]
        i += 2
        match op:
            case 0:
                registers[0] >>= eval_combo(erand)
            case 1:
                registers[1] ^= erand
            case 2:
                registers[1] = eval_combo(erand) % 8
            case 3:
                if registers[0]:
                    i = erand
            case 4:
                registers[1] ^= registers[2]
            case 5:
                outputs.append(eval_combo(erand) % 8)
            case 6:
                registers[1] = registers[0] >> eval_combo(erand)
            case 7:
                registers[2] = registers[0] >> eval_combo(erand)

    return outputs

def solve(c):
    for i in range(8):
        nc = (c << 3) + i
        l = try_it(nc)
        if l == prog:
            return nc
        if l == prog[-len(l):] and (r := solve(nc)):
            return r
print(solve(0))
