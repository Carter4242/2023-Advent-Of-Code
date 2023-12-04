global lines

#takes 90s to run

lines = []
with open("day4/day4.txt", 'r') as f:
    lines = f.readlines()
import time
startTime = time.time()
def countScore(l, i):
    sum = 0
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
    sum += 1
    for j in range(1, 1+total):
        sum += countScore(lines[i+j], i+j)
    return sum

sum = 0
for i in range(len(lines)):
    sum += 1
    l = lines[i]
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
    print(wins, nums)
    for n in nums:
        if n in wins:
            total += 1
    if total > 0:
        for j in range(1, 1+total):
            sum += countScore(lines[i+j], i+j)
print(time.time()-startTime)
print(sum)