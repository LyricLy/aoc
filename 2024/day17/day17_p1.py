from common import *
a = get_input()

registers = [a[0]["Register A"].num, a[0]["Register B"].num, a[0]["Register C"].num]
prog = a[1].nums

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
print(",".join(map(str, outputs)))
