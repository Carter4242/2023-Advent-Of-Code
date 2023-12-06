lines = []
with open("day6/day6", 'r') as f:
    lines = f.readlines()

times = lines[0].strip().split(' ')[1:]
times = list(filter(("").__ne__, times)) 
distance = lines[1].strip().split(' ')[1:]
distance = list(filter(("").__ne__, distance)) 
sum = 0
for i in range(len(times)):
    count = 0
    for j in range(1, int(times[i])):
        if (j*(int(times[i])-j) > int(distance[i])):
            count += 1
    if sum != 0:
        sum *= count
    else:
        sum = count
print(sum)