result = '?'
str = input()
max = [[], 0]
for i in range(len(str)):
    char = str[i].upper()
    if(str[i] in max[0]):
        continue
    else:
        frq = str.count(str[i])
        if(max[1] < frq):
            max[0].append(str[i])
            max[1] = frq
            result = str[i]
        elif(max[1] == frq):
            result = '?'
print(result)