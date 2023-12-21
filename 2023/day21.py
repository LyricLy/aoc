from common import *
import sys
a = get_input().grid
half = a.width//2

top_left = 0
top_right = 0
bottom_left = 0
bottom_right = 0
centre = 0

top_left_alt = 0
top_right_alt = 0
bottom_left_alt = 0
bottom_right_alt = 0
centre_alt = 0

def by_quadrant(p, qx, qy):
    sx = qx*half+qx
    ex = (qx+1)*half+qx
    sy = qy*half+qy
    ey = (qy+1)*half+qy
    if sx <= p[0] < ex and sy <= p[1] < ey:
        return p[0]-sx, p[1]-sy 

def behind_slash(p):
    return p[0] <= half-1-p[1]

def ahead_slash(p):
    return p[0] >= half-1-p[1]

def behind_backslash(p):
    return p[0] <= p[1]

def ahead_backslash(p):
    return p[0] >= p[1]

n = int(sys.argv[2])
count = (n - half) // a.width

# m = {}
frontier = [*a.orthagonals((half, half))]
seen = set()
while frontier:
    p = frontier.pop()
    if p in seen:
        continue
    seen.add(p)
    frontier.extend({ppp for pp in a.orthagonals(p) for ppp in a.orthagonals(pp) if a[pp] not in (None, "#") and a[ppp] not in (None, "#")})
    if (q := by_quadrant(p, 0, 0)) and behind_slash(q):
        top_left += 1
        # m[p] = "⌜"
    elif (q := by_quadrant(p, 1, 0)) and ahead_backslash(q):
        top_right += 1
        # m[p] = "⌝"
    elif (q := by_quadrant(p, 0, 1)) and behind_backslash(q):
        bottom_left += 1
        # m[p] = "⌞"
    elif (q := by_quadrant(p, 1, 1)) and ahead_slash(q):
        bottom_right += 1
        # m[p] = "⌟"
    else:
        # m[p] = "*"
        centre += 1

# for k, v in m.items():
#     a[k] = v
# print(a)
# exit(0)

# m = {}
frontier = [(half, half)]
seen = set()
while frontier:
    p = frontier.pop()
    if p in seen:
        continue
    seen.add(p)
    frontier.extend({ppp for pp in a.orthagonals(p) for ppp in a.orthagonals(pp) if a[pp] not in (None, "#") and a[ppp] not in (None, "#")})
    if (q := by_quadrant(p, 0, 0)) and behind_slash(q):
        top_left_alt += 1
        # m[p] = "⌜"
    elif (q := by_quadrant(p, 1, 0)) and ahead_backslash(q):
        top_right_alt += 1
        # m[p] = "⌝"
    elif (q := by_quadrant(p, 0, 1)) and behind_backslash(q):
        bottom_left_alt += 1
        # m[p] = "⌞"
    elif (q := by_quadrant(p, 1, 1)) and ahead_slash(q):
        # m[p] = "⌟"
        bottom_right_alt += 1
    else:
        # m[p] = "*"
        centre_alt += 1

# for k, v in m.items():
#     a[k] = v
# print(a)
# exit(0)

# The finale.
print(
    # Top corner
    centre + bottom_left + bottom_right
    # Left corner
  + centre + top_right + bottom_right
    # Right corner
  + centre + top_left + bottom_left
    # Bottom corner
  + centre + top_left + top_right
    # Main edges
    # Top right edge
  + (count-1) * (centre + top_left + bottom_left + bottom_right)
    # Top left edge
  + (count-1) * (centre + top_right + bottom_left + bottom_right)
    # Bottom left edge
  + (count-1) * (centre + top_right + top_left + bottom_right)
    # Bottom right edge
  + (count-1) * (centre + top_right + bottom_left + top_left)
    # Auxiliary edge rows
  + count * (bottom_right_alt + bottom_left_alt + top_right_alt + top_left_alt)
    # Finally, the center cells!
  + ((count-1)*(count-1)) * (centre + top_left + top_right + bottom_left + bottom_right)
  + (count*count) * (centre_alt + top_left_alt + top_right_alt + bottom_left_alt + bottom_right_alt)
)
