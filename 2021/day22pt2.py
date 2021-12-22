import re
from collections import defaultdict

with open("input.txt") as f:
    t = f.read()

cubs = []

def push_cub(cub):
    xl, xh, yl, yh, zl, zh = cub
    if xh < xl or yh < yl or zh < zl:
        return
    cubs.append(cub)

def cub_sum():
    c = 0
    for cub in cubs:
        xl, xh, yl, yh, zl, zh = cub
        c += (xh-xl+1)*(yh-yl+1)*(zh-zl+1)
    print(c)

for line in t.splitlines():
    on, pos = line.split()
    xl, xh, yl, yh, zl, zh = map(int, re.findall(r"-?[0-9]+", pos))
    popped = 0
    for idx, cub in enumerate(cubs.copy()):
        cxl, cxh, cyl, cyh, czl, czh = cub
        if (cxl <= xl <= cxh or cxl <= xh <= cxh or xl <= cxl and xh >= cxh) and (cyl <= yl <= cyh or cyl <= yh <= cyh or yl <= cyl and yh >= cyh) and (
        czl <= zl <= czh or czl <= zh <= czh or zl <= czl and zh >= czh):
            cubs.pop(idx-popped)
            popped += 1
            push_cub((cxl, cxh, cyl, yl-1, czl, czh))
            push_cub((cxl, cxh, yh+1, cyh, czl, czh))
            tyl = max(yl, cyl)
            tyh = min(yh, cyh)
            push_cub((cxl, cxh, tyl, tyh, czl, zl-1))
            push_cub((cxl, cxh, tyl, tyh, zh+1, czh))
            tzl = max(zl, czl)
            tzh = min(zh, czh)
            push_cub((cxl, xl-1, tyl, tyh, tzl, tzh))
            push_cub((xh+1, cxh, tyl, tyh, tzl, tzh))
    if on == "on":
        cubs.append((xl, xh, yl, yh, zl, zh))
cub_sum()
