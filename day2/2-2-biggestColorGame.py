lines = []
with open("day2/day2.txt", 'r') as f:
    lines = f.readlines()

sum = 0
for l in lines:
    l = l.strip('\n').split(" ")
    gameNum = l[1][:-1]
    l = l[2:]
    l = " ".join(l)
    l = l.split(";")
    maxRed, maxBlue, maxGreen = 0, 0, 0
    for round in l:
        dice = round.split(',')
        for d in dice:
            values = d.strip().split(' ')
            if values[1] == "blue":
                if int(values[0]) > maxBlue:
                    maxBlue = int(values[0])
            if values[1] == "green":
                if int(values[0]) > maxGreen:
                    maxGreen = int(values[0])
            if values[1] == "red":
                if int(values[0]) > maxRed:
                    maxRed = int(values[0])
    sum += maxRed*maxGreen*maxBlue

print(sum)