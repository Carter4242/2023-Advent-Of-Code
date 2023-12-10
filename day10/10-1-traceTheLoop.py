
lines = []
with open("day10/day10", 'r') as f:
    lines = f.readlines()

tiles = []
Spos = []
for i in range(len(lines)):
    l = lines[i].strip()
    tiles.append([])
    for j in range(len(l)):
        c = l[j]
        if c == '|':
            tiles[i].append([[i-1, j],[i+1, j]])
        elif c == '-':
            tiles[i].append([[i, j-1],[i, j+1]])
        elif c == 'L':
            tiles[i].append([[i-1, j],[i, j+1]])
        elif c == 'J':
            tiles[i].append([[i-1, j],[i, j-1]])
        elif c == '7':
            tiles[i].append([[i, j-1],[i+1, j]])
        elif c == 'F':
            tiles[i].append([[i, j+1],[i+1, j]])
        elif c == 'S':
            tiles[i].append([[i, j-1],[i, j+1]])
            Spos = [i,j]
        else:
            tiles[i].append([[-1, -1],[-1, -1]])

maxes = 1
checked = []
checking = [Spos]
while True:
    breakout = False

    checking2 = checking.copy()
    checking = []
    #print()
    #print(checking2)
    for c in checking2:
        checked.append(c)
        #print(tiles[c[0]][c[1]][0], tiles[c[0]][c[1]][1])
        if (tiles[c[0]][c[1]][1] in checked or tiles[c[0]][c[1]][1] in checking) and (tiles[c[0]][c[1]][0] in checked or tiles[c[0]][c[1]][0] in checking):
            breakout = True
            break
        if tiles[c[0]][c[1]][0] not in checked and tiles[c[0]][c[1]][0] not in checking:
            checking.append(tiles[c[0]][c[1]][0])
        if tiles[c[0]][c[1]][1] not in checked and tiles[c[0]][c[1]][1] not in checking:
            checking.append(tiles[c[0]][c[1]][1])

    if breakout:
        break
    maxes += 1
    #print(maxes)
print(maxes)
