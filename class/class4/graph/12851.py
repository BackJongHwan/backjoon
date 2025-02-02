# N, K = 10^6 => O(N)
import heapq
n, k = map(int, input().split())

# cost와 도착하는 방법의 수
dp = [[float("inf"), 0] for _ in range(10 ** 6 + 1)]
dp[n] = [0, 1] 

result = 0
pq = []
heapq.heappush(pq, (0, n))
min_value = 0
check = False
while pq:
    cost, pos = heapq.heappop(pq)
    # 이제 더 큰 것만 나와서 break함
    if check and cost > min_value:
        break
    if(pos == k):
        # 처음으로 도달했을 때
        if not check:
            check = True
            min_value = cost
            result += dp[pos][1]
            continue
        else:
            if(cost == min_value):
                result += dp[pos][1]
                continue
    next_positions = [pos-1, pos + 1, pos * 2]
    for next_pos in next_positions:
        if(0<= next_pos <= 10 ** 6):
            if(dp[next_pos][0] > cost + 1):
                dp[next_pos] = [cost + 1, dp[pos][1]]
                heapq.heappush(pq, (cost+1, next_pos))
            elif dp[next_pos][0] == cost + 1:
                dp[next_pos][1] += dp[pos][1]
            else:
                continue

print(min_value)
print(result)