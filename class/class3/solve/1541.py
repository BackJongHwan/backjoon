import sys
input = sys.stdin.readline

equation = input().rstrip()
component = []
str =""
for i in equation:
    if(i == '+' or i == '-'):
        component.append(int(str))
        component.append(i)
        str =""
    else: 
        str += i
component.append(int(str))
previous = 0
num_list = []
for i in range(len(component)):
    if (component[i] == '-'):
        num_list.append(component[previous: i])
        previous = i + 1
num_list.append(component[previous:])
result = 0
for i in range(len(num_list)):
    temp = 0
    for j in range(len(num_list[i])):
        if(num_list[i][j] != '+'):
            temp += num_list[i][j]
    if(i == 0):
        result = temp
    else:
        result -= temp
print(result)