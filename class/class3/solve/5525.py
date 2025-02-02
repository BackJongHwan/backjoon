import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
string = input().strip()

pattern = "IO" *n + "I"
#50점짜리
''' O(string * pattern)
count = 0
for i in range(len(string) - len(pattern) + 1):
    if(string[i: i + len(pattern)] == pattern):
        count+=1
print(count)
'''
# score = 50
'''O(string * pattern)
count = 0
idx = 0
max_index = len(string) - len(pattern)
while idx <= max_index:
    # print(idx)
    if(idx == max_index):
        if(string[idx : idx + len(pattern)] == pattern):
            count +=1
        break
    if(string[idx: idx + len(pattern)] == pattern):
        count += 1
        if(string[idx + len(pattern)] == 'I'):
            idx += len(pattern)
        else:
            idx += 2
    else:
        idx += 1
print(count)
'''
#only IOI
'''
pi = [0] * len(pattern)
for i in range(1, len(pattern)):
    pi[i] = i - 1
print(pi)
'''
#normally
pi = [0] * len(pattern)
j = 0
for i in range(1, len(pattern)):
    while j > 0 and pattern[i] != pattern[j]:
        j = pi[j - 1]
    if pattern[i] == pattern[j]:
        j += 1
        pi[i] = j
j = 0
cnt = 0
for i in range(len(string)):
    while j > 0 and string[i] != pattern[j]:
        j = pi[j - 1]
    if string[i] == pattern[j]:
        if j == len(pattern) - 1:
            cnt += 1
            j = pi[j]
        else:
            j += 1
print(cnt)