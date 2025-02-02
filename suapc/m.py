import heapq

n = int(input())
trees = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    x, k = map(int, input().split())
    arr = heapq(trees)
    for _ in range(x):
        min_value = arr.heappop()
        
