# import heapq
'''
n, k = map(int ,input().split())
dp = [float('inf')] * (k + 2)
idx = 0
pq = []
# dp[n] = 0
# for i in range(n, -1, -1):
#     dp[i] = idx
#     idx += 1
heapq.heappush(pq, (0, n))
while(True):
    idx, value = heapq.heappop(pq)
    if(value == k):
        print(idx)
        break
    if(value != 0):
        a = value * 2
        while(a < k + 2):
            dp[a] = idx
            heapq.heappush(pq, (idx, a))
            a *= 2
    if(value > 0 and value < k + 1):
        dp[value + 1] = idx + 1
        dp[value - 1] = idx + 1
        heapq.heappush(pq, (idx + 1, value-1))
        heapq.heappush(pq, (idx + 1, value+1))
    elif (value == 0):
        dp[value + 1] = idx + 1
    elif (value == k + 1): #         dp[value - 1] = idx + 1
        heapq.heappush(pq, (idx + 1, value-1))
'''
# bfs
import heapq

n, k = map(int, input().split())
dp = [float('inf')] * (100001)  # n, k가 100,000 이하라고 가정
pq = []
heapq.heappush(pq, (0, n))
dp[n] = 0

while pq:
    idx, value = heapq.heappop(pq)
    
    # 이미 더 짧은 경로로 방문했다면 무시
    if idx > dp[value]:
        continue

    # 목표 값 도달
    if value == k:
        print(idx)
        break

    # 이동: value * 2
    if value * 2 < 100001 and idx < dp[value * 2]:
        dp[value * 2] = idx
        heapq.heappush(pq, (idx, value * 2))

    # 이동: value + 1
    if value + 1 < 100001 and idx + 1 < dp[value + 1]:
        dp[value + 1] = idx + 1
        heapq.heappush(pq, (idx + 1, value + 1))

    # 이동: value - 1
    if value - 1 >= 0 and idx + 1 < dp[value - 1]:
        dp[value - 1] = idx + 1
        heapq.heappush(pq, (idx + 1, value - 1))
 