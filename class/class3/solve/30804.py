# n = 10^6 * 2
import sys
from collections import deque 
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
#O(n^3)
#a, b의 값을 하나하나 변화시키면서 슬라이싱
'''
max = 0
for a in range(n):
    for b in range(n):
        if(a + b < n):
            new_list = num_list[a:n - b] #O(n) time complexity
            new_set = set(new_list)
            if(len(new_set) <= 2):
                if(len(new_list) > max):
                    max = len(new_list)
print(max)
'''
# a + b의 값을 고정시켜놓고 window slicing과 비슷한 방식으로 함.
'''
k = 0
check = False 
result = 0
while n > k:
    for a in range(k + 1):
        b = k - a
        new_list = num_list[a:n - b]
        new_set = set(new_list)
        # print(new_list)
        if(len(new_set) <= 2):
            check = True
            result = len(new_list)
        if check:
            break
    k += 1
    if check:
        break
print(result)
'''
#O(nlong)
#two pointer를 이용함
left = 0
right = 0
max_len = 0
num = [0] * 10 
kind = 0
lenth = 0
while right < n:
    if(num[num_list[right]] == 0):
        kind += 1
    num[num_list[right]] += 1
    if kind > 2:
        while kind > 2:
            if(num[num_list[left]] == 1):
                kind -= 1
            num[num_list[left]] -= 1
            left += 1
    lenth = right - left + 1
    if(max_len < lenth):
        max_len = lenth
    right += 1
print(max_len)