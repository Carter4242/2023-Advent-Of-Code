lines = []
with open("day4/day4.txt", 'r') as f:
    lines = f.readlines()

sum = 0
for l in lines:
    total = 0
    l = l.split(': ')[1]
    winsS, numsS = l.split(' | ')
    wins, nums = [], []
    for w in winsS.split(" "):
        if w.strip() != "":
            wins.append(w.strip(''))
    for w in numsS.split(" "):
        if w.strip('') != "":
            nums.append(w.strip())
    for n in nums:
        if n in wins:
            total += 1
    if total > 0:
        sum += 2**(total-1)

print(sum)