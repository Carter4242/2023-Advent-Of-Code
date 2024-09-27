import numpy 

lines = []
with open('day11/day11') as f:
    lines = f.read().splitlines()
linesTransposed = []
for l in lines:
    linesTransposed.append(list(l))
linesTransposed = numpy.transpose(linesTransposed)

galaxies = []

doublesY = 0
for intL in range(len(lines)):
    l = lines[intL]
    if '#' not in l:
        doublesY += 1000000-1
    else:
        for intC in range(len(l)):
            if l[intC] == '#':
                galaxies.append([intC, intL+doublesY])

doublesX = 0
for intL in range(len(linesTransposed)):
    if '#' not in linesTransposed[intL]:
        for intG in range(len(galaxies)):
            if galaxies[intG][0] > intL + doublesX:
                galaxies[intG][0] += 1000000-1
        doublesX += 1000000-1
print(galaxies)

shortestDistance = 0
for intG in range(len(galaxies)):
    g = galaxies[intG]
    for intG2 in range(intG+1, len(galaxies[intG+1:])+intG+1):
        g2 = galaxies[intG2]
        x = abs(g[0]-g2[0])
        y = abs(g[1]-g2[1])
        shortestDistance += x+y
print(shortestDistance)