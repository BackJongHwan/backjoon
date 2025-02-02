# n = 100, m = n -> O(n^2)
import sys
from collections import deque

input = sys.stdin.readline
test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    jobs = deque(list(enumerate(map(int ,input().split()))))
    # print(jobs)
    k = 0
    while True:
        job = jobs.popleft()
        check = 0
        for i in range(len(jobs)):
            if(job[1] < jobs[i][1]):
                jobs.append(job)
                check = 1
                break
        if check == 0:
            k += 1
            if(job[0] == m):
                break
    print(k)