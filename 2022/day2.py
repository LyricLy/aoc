with open("input.txt") as f:
    text = f.read()

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

results = {
    ("X", "A"): 3,
    ("X", "B"): 0,
    ("X", "C"): 6,
    ("Y", "A"): 6,
    ("Y", "B"): 3,
    ("Y", "C"): 0,
    ("Z", "A"): 0,
    ("Z", "B"): 6,
    ("Z", "C"): 3,
}

results_inverse = {(them, n): me for ((me, them), n) in results.items()}

symbols = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

score = 0
for l in text.splitlines():
    them, idea = l.split()
    me = results_inverse[them, symbols[idea]]
    score += results[me, them] + scores[me]
print(score)
