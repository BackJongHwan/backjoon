n = int(input())
x_list = list(map(int, input().split()))
x_set = sorted(list(set(x_list)))
dic= {x_set[i] : i for i in range(len(x_set))}
for i in x_list:
    print(dic[i], end = " ")
print()