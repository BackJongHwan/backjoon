n_str = input()
n = int(n_str)
for i in range(n):
    sum_a = 0
    sum_a += i
    str_i = str(i)
    for j in range(0, len(str_i)):
        sum_a += int(str_i[j])
    if(sum_a == n):
        print(i)
        break
    if(i == n -1):
        print(0)