from functools import reduce


with open("input.txt") as f:
    n, l = f.readlines()
    ll = [int(x) if x != "x" else None for x in l.split(",")]


def departs_at(t, n):
    return t % n == 0

def chinese_remainder(pairs):
  product = 1
  for _, x in pairs:
    product *= x
  total = 0
  for residue, mod in pairs:
    base = product // mod
    total += residue * base * pow(base, mod - 2, mod=mod)
    total %= product
  return total

print(chinese_remainder([(ll[n] - n, ll[n]) for n in range(len(ll)) if ll[n] is not None]))
