def disaster(num):
    str_num = str(num)
    con = 0
    for i in range(len(str_num)):
        if(str_num[i] == '6'):
            con += 1
        else:
            con = 0
        if(con == 3):
            return True
    return False

n = int(input())
k = 0 
result = 665
while n > k:
    result +=1
    if(disaster(result)):
        k +=1

print(result)