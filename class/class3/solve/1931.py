#n = 10^5
n = int(input())
num_list = []
for _ in range(n):
    start, end = map(int, input().split())
    num_list.append((start, end))
sorted_list = sorted(num_list, key=lambda x : (x[1], x[0]))
''' not effienct beacuse of remove operation
k = 1
for _ in range(n - 1):
    if(sorted_list[k][0] >= sorted_list[k-1][1]):
        k+=1
    else:
        sorted_list.remove(sorted_list[k])
print(len(sorted_list))
'''
# Initialize the count of non-overlapping intervals and the end time of the last added interval
count = 1
last_end = sorted_list[0][1]

# Iterate through the sorted list and count non-overlapping intervals
for i in range(1, n):
    if sorted_list[i][0] >= last_end:
        count += 1
        last_end = sorted_list[i][1]

print(count)