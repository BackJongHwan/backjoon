str = input()
num_letter = len(str)
for i in range(len(str)):
    if str[i] == '-':
        num_letter -= 1
    if str[i] == 'j':
        if(i != 0):
            if(str[i-1] == 'l' or str[i-1] == 'n'):
                num_letter -= 1
    if str[i] == '=':
        if(i > 1):
            if(str[i - 2] == 'd' and str[i - 1] == 'z'):
                num_letter -= 2
                continue
        if(i > 0):
            if(str[i -1] == 'c' or 'z' or 's'):
                num_letter -= 1
print(num_letter)