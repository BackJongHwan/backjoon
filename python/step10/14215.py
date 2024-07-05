side = list(map(int, input().split()))
max_val = 0
max_idx = 0
sum_2 = 0
for i in range(3):
    if(max_val < side[i]):
        max_val = side[i]
        max_idx = i
for i in range(3):
    if(i != max_idx):
        sum_2 += side[i]
if(max_val < sum_2):
    print(sum(side))
else:
    print(sum(side) - (max_val - sum_2) - 1)

