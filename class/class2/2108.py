# n = 5 * 10^5 O(nlogn)
import sys
input = sys.stdin.readline

num_list = []
n = int(input())
for _ in range(n):
    num = int(input())
    num_list.append(num)
#산술평균
print(round(sum(num_list) / n))
#중앙값
num_list.sort()
print(num_list[n // 2])
#최빈값
#n^2같은데...
# In nasted for loop -> O(n^2)
'''
num_set = set(num_list)
result = []
for num in num_set:
    cnt = 0
    for i in num_list:
        if(num == i):
            cnt += 1
    result.append((num, cnt))
max = 0
for num in result:
    if(num[1] > max):
        max = num[1]
max_list = []
for num in result:
    if(num[1] == max):
        max_list.append(num)
max_list.sort()
if(len(max_list) == 1):
    print(max_list[0][0])
else:
    print(max_list[1][0])
'''
num_dict = {}
#O(n)
for num in num_list:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1
max = 0
#O(n)
for values in num_dict.values():
    if(max < values):
        max = values
num_count = list(num_dict.items())
max_count = []
#O(n)
for num in num_count:
    if(num[1] == max):
        max_count.append(num)
#O(nlogn)
max_count.sort()
if(len(max_count) == 1):
    print(max_count[0][0])
else:
    print(max_count[1][0])
#범위
print(num_list[n-1] - num_list[0])