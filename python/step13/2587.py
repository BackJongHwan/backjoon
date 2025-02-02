num_list = []
for _ in range(5):
    num = int(input())
    num_list.append(num)
avg = int(sum(num_list) / 5)
num_list.sort()
mid = num_list[2]
print(avg)
print(mid)
