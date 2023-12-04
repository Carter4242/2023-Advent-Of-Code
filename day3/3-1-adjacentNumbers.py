def validChar(c):
    return(not c.isdigit() and c != '.')

lines = []
with open("day3/day3.txt", 'r') as f:
    lines = f.readlines()

schem = []

for l in lines:
    newLine = []
    for c in l.strip():
        newLine.append(c)
    schem.append(newLine)

print(schem)

sum = 0
height = len(schem)-1
width = len(schem[0])-1
for l in range(len(schem)):
    addPartNum = False
    partNum = ""
    for i in range(len(schem[l])):
        c = schem[l][i]
        if c.isdigit():
            partNum += c
            if (i != 0 and validChar(schem[l][i-1])) or (i != width and validChar(schem[l][i+1])):
                addPartNum = True
            if (l != 0 and ((i != 0 and validChar(schem[l-1][i-1])) or (validChar(schem[l-1][i])) or (i != width and validChar(schem[l-1][i+1])))):
                addPartNum = True
            if (l != height and ((i != 0 and validChar(schem[l+1][i-1])) or (validChar(schem[l+1][i])) or (i != width and validChar(schem[l+1][i+1])))):
                addPartNum = True
        else:
            if addPartNum:
                sum += int(partNum)
                addPartNum = False
            partNum = ""
    if addPartNum:
        sum += int(partNum)



print(sum)