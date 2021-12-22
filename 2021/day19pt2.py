with open("input.txt") as f:
    t = f.read()

scanners = []
for ix, c in enumerate(t.split("\n\n")):
    scanners.append((ix, [tuple(int(h) for h in x.split(",")) for x in c.splitlines()[1:]]))

def rot_z(l):
    return [(-y, x, z) for x, y, z in l]

def rot_y(l):
    return [(-z, y, x) for x, y, z in l]

def rot_x(l):
    return [(x, -z, y) for x, y, z in l]


total = {*scanners[0][1]}
scan_pos = []

def unify(ty):
    for _ in range(4):
        for _ in range(4):
            for _ in range(4):
                for ffx, ffy, ffz in total:
                    diffs = {(x-ffx, y-ffy, z-ffz) for x, y, z in total}
                    for fx, fy, fz in ty:
                        ins = {(x-fx, y-fy, z-fz) for x, y, z in ty}
                        ins &= diffs
                        if len(ins) >= 12:
                            os = (ffx-fx, ffy-fy, ffz-fz)
                            scan_pos.append(os)
                            total.update((x+os[0], y+os[1], z+os[2]) for x, y, z in ty)
                            return True
                ty = rot_z(ty)
            ty = rot_y(ty)
        ty = rot_x(ty)
    return False

scanners.pop(0)
while scanners:
    for i, scan in enumerate(scanners):
        if not scan[1] or unify(scan[1]):
            scanners[i] = None
    scanners[:] = filter(None, scanners)
print(len(total))

import itertools
m = []
for x, y in itertools.combinations(scan_pos, 2):
    m.append(abs(x[0]-y[0])+abs(x[1]-y[1])+abs(x[2]-y[2]))
print(max(m))
