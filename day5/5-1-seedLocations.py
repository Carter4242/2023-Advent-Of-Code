lines = []
with open("day5/day5", 'r') as f:
    lines = f.readlines()

seedsL = lines[0].strip().split(' ')[1:]
seeds = []
for s in seedsL:
    seeds.append([s, False])

for l in lines[1:]:
    print()
    l = l.strip()
    if l != "" and l[0].isdigit():
        l = l.split(' ')
        for i in range(len(seeds)):
            s = int(seeds[i][0])
            if s >= int(l[1]) and s < int(l[1]) + int(l[2]):
                if not seeds[i][1]:
                    seeds[i][0] = int(l[0]) + s - int(l[1])
                    seeds[i][1] = True
    else:
        for i in range(len(seeds)):
            seeds[i][1] = False
seedNums = []
for s in seeds:
    seedNums.append(s[0])
print(min(seedNums))