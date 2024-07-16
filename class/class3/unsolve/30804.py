# n = 10^6 * 2
import sys
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
max = 0
for a in range(n):
    for b in range(n):
        if(a + b < n):
            new_list = num_list[a:n - b]
            new_set = set(new_list)
            if(len(new_set) <= 2):
                if(len(new_list) > max):
                    max = len(new_list)
print(max)