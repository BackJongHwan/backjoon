import sys
n = int(sys.stdin.readline().rstrip())
num_list = [0] * 10000
max = 0
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if(max < num):
        max = num
    num_list[num-1] += 1
for i in range(max):
    if(num_list[i] > 0):
        for _ in range(num_list[i]):
            print(i + 1)