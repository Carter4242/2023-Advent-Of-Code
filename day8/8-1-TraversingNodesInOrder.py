lines = []
with open("day8/day8", 'r') as f:
    lines = f.readlines()

queue = []
places = {}
directions = lines[0].strip()
for l in lines[2:]:
    l = l.split()
    print(l[0])
    places[l[0]] = [l[2][1:-1], l[3][0:3]]
sum = 0
current = "AAA"
while True:
    for c in directions:
        if c == 'L':
            current = places[current][0]
        else:
            current = places[current][1]
        sum += 1
        if current == "ZZZ":
            print(sum)
            exit()