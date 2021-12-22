from aoccy import *


rang = regex("(\d+)-(\d+)").map(lambda x: (int(x.group(1)), int(x.group(2))+1))
f = (regex("[a-z ]+") << lit(": ")) & rang & (lit(" or ") >> rang) << lit("\n")
@f
def note(t):
    return t[0][0].group(0), t[0][1], t[1]
notes = note[:] << lit("\n")

mine = lit("your ticket:\n") >> sep_by(lit(","), regex("\d+").map(lambda m: int(m.group(0)))) << lit("\n\n")
nearby = lit("nearby tickets:\n") >> (sep_by(lit(","), regex("\d+").map(lambda m: int(m.group(0)))) << lit("\n"))[:]

stuff = notes & mine & nearby

with open("input.txt") as f:
    data = stuff.parse_text(f.read())

(notes, mine), nearby = data

def is_valid(n, note):
    return n in range(note[1][0], note[1][1]) or n in range(note[2][0], note[2][1])

def check_notes(idx, note):
    for n in nearby:
        if not is_valid(n[idx], note):
            return False
    return True

valid = []
for n in nearby:
    if all(any(is_valid(v, note) for note in notes) for v in n):
        valid.append(n)
nearby = valid

possibilities = [{}]
new_possibilities = []
undone = notes.copy()
from tqdm import tqdm

for idx in tqdm(range(len(notes))):
    n = undone.pop()
    while possibilities:
        possibility = possibilities.pop()
        for i in range(0, len(notes)):
            if i in possibility:
                continue
            if check_notes(i, n):
                a = possibility.copy()
                a[i] = n
                new_possibilities.append(a)
    possibilities = new_possibilities
    new_possibilities = []

v = 1
for idx, va in enumerate(mine):
    if possibilities[0][idx][0].startswith("departure"):
        v *= va
print(v)
