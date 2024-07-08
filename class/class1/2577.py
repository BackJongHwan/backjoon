num_list = [0] * 10 
a = int(input())
b = int(input())
c = int(input())
result = str(a * b * c)
for i in result:
    num_list[int(i)] += 1
for i in num_list:
    print(i)