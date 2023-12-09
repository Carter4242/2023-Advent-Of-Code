lines = []
with open("day9/day9", 'r') as f:
    lines = f.readlines()

sum = 0
traceBack = []
for l in lines:
    value = 0
    l = l.strip().split()
    traceBack = []
    traceBack.append(l)
    endValue = l[-1]
    while endValue != 0: # just checking the end value doesn't work for 0 1 2 2 (but not case like this exists)
        newL = []
        for i in range(1, len(l)):
            newL.append(int(l[i]) - int(l[i-1]))
        traceBack.append(newL)
        l = newL
        endValue = l[-1]
    for i in range(len(traceBack)-1, -1, -1):
        value = int(traceBack[i][-1]) + value
    sum += value
print(sum)