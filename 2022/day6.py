with open("input.txt") as f:
    s = f.read()

for i in range(14, len(s)):
    if len(set(s[i-14:i])) == 14:
        print(i)
        break
