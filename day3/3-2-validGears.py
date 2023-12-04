def validChar(c):
    return(c.isdigit())

lines = []
with open("day3/day3.txt", 'r') as f:
    lines = f.readlines()

schem = []

for l in lines:
    newLine = []
    for c in l.strip():
        newLine.append(c)
    schem.append(newLine)

#print(schem)

sum = 0
height = len(schem)-1
width = len(schem[0])-1
for l in range(len(schem)):
    for i in range(len(schem[l])):
        c = schem[l][i]
        if c == '*':
            nums = []
            backwards, forwards = 0, 0
            if i > 4:
                backwards = 3
            else:
                backwards = i
            if i + 3 < width:
                forwards = 3
            else:
                forwards = width-i
            goBack = i-2
            if goBack < 0:
                goBack = 0
            goForward = i+2
            if goForward > width:
                goForward = width
            goForward+=1
            if (i != 0):
                if validChar(schem[l][i-1]):
                    nums.append(schem[l][i-backwards:i])
                if (i != width and validChar(schem[l][i+1])):
                    nums.append(schem[l][i+1:i+forwards+1])
            
            if (l != 0):
                middle = False
                left = False
                right = False
                if (validChar(schem[l-1][i])):
                    middle = True
                if (i != 0 and validChar(schem[l-1][i-1])):
                    left = True
                if (i != width and validChar(schem[l-1][i+1])):
                    right = True
                if middle:
                    if not left and not right:
                        nums.append(schem[l-1][i])
                    else:
                        nums.append(schem[l-1][goBack:goForward])
                else:
                    if left:
                        nums.append(schem[l-1][i-backwards:i])
                    if right:
                        nums.append(schem[l-1][i+1:i+forwards+1])
                

            if (l != height):
                middle = False
                left = False
                right = False
                if (validChar(schem[l+1][i])):
                    middle = True
                if (i != 0 and validChar(schem[l+1][i-1])):
                    left = True
                if (i != width and validChar(schem[l+1][i+1])):
                    right = True
                if middle:
                    if not left and not right:
                        nums.append(schem[l+1][i])
                    else:
                        nums.append(schem[l+1][goBack:goForward])
                else:
                    if left:
                        nums.append(schem[l+1][i-backwards:i])
                    if right:
                        nums.append(schem[l+1][i+1:i+forwards+1])
            
            if len(nums) == 2:
                num1 = "".join(nums[0]).strip('.')
                num2 = "".join(nums[1]).strip('.')
                num1 = max(num1.split('.'), key = len)
                num2 = max(num2.split('.'), key = len)
                print(num1, num2)#nums[0], num1, nums[1], num2)
                sum += (int(num1)*int(num2))


print(sum)