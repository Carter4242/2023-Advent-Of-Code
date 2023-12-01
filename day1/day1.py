
lines = ""
with open("day1/day1.txt", 'r') as f:
    lines = f.readlines()

sum = 0
for l in lines:
    first = -1
    last = -1
    for c in l:
        if c.isdigit():
            if first == -1:
                first = str(c)
                last = str(c)
            else:
                last = str(c)
    sum += int(str(first)+str(last))
print(sum)