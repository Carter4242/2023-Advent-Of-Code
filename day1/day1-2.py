
lines = []
with open("day1/day1.txt", 'r') as f:
    lines = f.readlines()

sum = 0
for l in lines:
    i = 0
    newL = ""
    while(i < len(l)):
        length = len(l)
        left = (length-1)-i
        if l[i].isdigit():
            newL += l[i]
        if left >= 3:
            segment = l[i:i+3]
            if segment == "six":
                newL += '6'
            if segment == "two":
                newL += '2'
            if segment == "one":
                newL += '1'
        if left >= 4:
            segment = l[i:i+4]
            if segment == "nine":
                newL += '9'
            if segment == "five":
                newL += '5'
            if segment == "four":
                newL += '4'
        if left >= 5:
            segment = l[i:i+5]
            if segment == "eight":
                newL += '8'
            if segment == "seven":
                newL += '7'
            if segment == "three":
                newL += '3'
        i += 1

    first = -1
    last = -1
    for c in newL:
        if c.isdigit():
            if first == -1:
                first = c
                last = c
            else:
                last = c
    sum += int(str(first)+str(last))

print(sum)