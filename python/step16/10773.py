n = int(input())
num_list = []
for _ in range(n):
    num = int(input())
    if(num == 0):
        num_list.pop()
    else:
        num_list.append(num)
print(sum(num_list))