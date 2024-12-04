from common import *
a = get_input().grid

c = 0
for g in [a, a.rot(), a.rot().rot(), a.rot().rot().rot()]:
    for p in g:
        if g[p] == "M" and g[offset(p, (0, 2))] == "M" and g[offset(p, (1, 1))] == "A" and g[offset(p, (2, 0))] == "S" and g[offset(p, (2, 2))] == "S":
            c += 1
# a.flip()
# for g in [a, a.rot(), a.rot().rot(), a.rot().rot().rot()]:
#     for p in g:
#         if g[p] == "M" and g[offset(p, (0, 2))] == "M" and g[offset(p, (1, 1))] == "A" and g[offset(p, (2, 0))] == "S" and g[offset(p, (2, 2))] == "S":
#             c += 1
print(c)
