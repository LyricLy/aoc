from aoccy import *
from functools import reduce


plus = lit(" + ").map(lambda _: lambda x, y: x + y)
mul = lit(" * ").map(lambda _: lambda x, y: x * y)
num = regexp("\d+").map(int)
base_expr = defer(lambda: lit("(") >> expr << lit(")") | num)
chain0 = cp((base_expr & (plus & base_expr)[:]).map(lambda r: reduce(lambda s, n: n[0](s, n[1]), r[1], r[0]))) | base_expr
chain1 = cp((chain0 & (mul & chain0)[:]).map(lambda r: reduce(lambda s, n: n[0](s, n[1]), r[1], r[0]))) | chain0
expr = chain1

print(expr.parse_text("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))

with open("input.txt") as f:
    data = f.readlines()

s = 0
for line in data:
    s += expr.parse_text(line)
print(s)
