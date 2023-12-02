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
    invalid = False
    for round in l:
        dice = round.split(',')
        for d in dice:
            values = d.strip().split(' ')
            if values[1] == "blue" and int(values[0]) > 14:
                invalid = True
                break
            if values[1] == "green" and int(values[0]) > 13:
                invalid = True
                break
            if values[1] == "red" and int(values[0]) > 12:
                invalid = True
                break
        if invalid:
            break
    if not invalid:
        print(gameNum)
        sum += int(gameNum)
    
print(sum)