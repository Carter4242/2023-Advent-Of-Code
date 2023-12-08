import math

lines = []
with open("day8/day8", 'r') as f:
    lines = f.readlines()

queue = []
places2 = []
places = {}
directions = lines[0].strip()
for l in lines[2:]:
    l = l.split()
    places2.append(l[0])
    places[l[0]] = [l[2][1:-1], l[3][0:3]]

sum = 0
listCurrent = []
for p in places2:
    if p[2] == 'A':
        listCurrent.append(p)
                    
for c in range(len(listCurrent)):
    breakout = False
    current = listCurrent[c]
    steps = 0
    prevSteps = 0
    while True:
        if breakout:
            break
        for d in directions:
            if current[2] == 'Z':
                if steps == prevSteps:
                    breakout = True
                    current = steps
                    break
                else:
                    prevSteps = steps
                    steps = 0
            if d == 'L':
                current = places[current][0]
            else:
                current = places[current][1]
            steps += 1
    listCurrent[c] = current

print(math.lcm(*listCurrent))