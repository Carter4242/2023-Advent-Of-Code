
lines = []
with open("day10/day10", 'r') as f:
    lines = f.readlines()

tilesNum = []
Spos = []
for i in range(len(lines)):
    l = lines[i].strip()
    tilesNum.append([])
    for j in range(len(l)):
        c = l[j]
        if c == '|':
            tilesNum[i].append([[i-1, j],[i+1, j]])
        elif c == '-':
            tilesNum[i].append([[i, j-1],[i, j+1]])
        elif c == 'L':
            tilesNum[i].append([[i-1, j],[i, j+1]])
        elif c == 'J':
            tilesNum[i].append([[i-1, j],[i, j-1]])
        elif c == '7':
            tilesNum[i].append([[i, j-1],[i+1, j]])
        elif c == 'F':
            tilesNum[i].append([[i, j+1],[i+1, j]])
        elif c == 'S':
            tilesNum[i].append([[i, j-1],[i, j+1]])
            Spos = [i,j]
        else:
            tilesNum[i].append([[-1, -1],[-1, -1]])

loop = []
checking = [Spos]
while len(checking) != 0:
    checking2 = checking.copy()
    checking = []
    for c in checking2:
        loop.append(c)
        if tilesNum[c[0]][c[1]][0] not in loop and tilesNum[c[0]][c[1]][0] not in checking:
            checking.append(tilesNum[c[0]][c[1]][0])
        if tilesNum[c[0]][c[1]][1] not in loop and tilesNum[c[0]][c[1]][1] not in checking:
            checking.append(tilesNum[c[0]][c[1]][1])

tiles = []
for i in range(len(lines)):
    l = lines[i].strip()
    tiles.append([])
    for j in l:
        tiles[i].append(j)

sum = 0
for l in range(len(tiles)):
    insideLoop = False
    for t in range(len(tiles[l])):
        tilePos = [l, t]
        if tiles[l][t] in "|LJ" and tilePos in loop:
            insideLoop = not insideLoop
        else:
            if insideLoop and [l, t] not in loop:
                sum += 1
print(sum)