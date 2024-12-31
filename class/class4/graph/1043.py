# graph dfs
# using adjcent matrix
'''
import sys
from queue import Queue
# q = Queue()
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * n  for _ in range(n)]
# print(graph)
data = list(map(int, input().split()))
num_truth = data[0]
if(num_truth != 0):
    truth_people = data[1:]
else:
    truth_people = []
party = []
for _ in range(m):
    temp = list(map(int ,input().split()))
    party.append(temp)

# party에 참가한 사람끼리 graph만들기
for element in party:
    # print(eement)
    for i in range(1, element[0] + 1):
        for j in range(i + 1, element[0] + 1):
            # print(i, j)
            if(i != j):
                graph[element[i]-1][element[j]-1] = 1
                graph[element[j]-1][element[i]-1] = 1
# 진실을 아는 사람끼리 bfs를 돌림

visited = [False] * n
result = []

def bfs(start):
    if visited[start]:
        return
    q = Queue()
    q.put(start)
    visited[start] = True
    while not q.empty():
        idx = q.get()
        if idx not in result:
            result.append(idx)
        for i in range(n):
            if(graph[i][idx] == 1) and not visited[i]:
                visited[i] = True
                q.put(i)
for people in truth_people:
    bfs(people-1)
result = [x + 1 for x in result]
result.sort()
num_party = 0
for element in party:
    check = False
    data = element[1:]
    for k in data:
        if k in result:
            check = True
            break
    if check == False:
        num_party+=1
# print(result)
# print(graph)
print(num_party)
'''

# using disjoint set
