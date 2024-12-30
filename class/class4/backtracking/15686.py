import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    new_list = list(map(int, input().split()))
    matrix.append(new_list)

# def backtracking(k, start, selected):
#     if(k == m):
#         total_cost = 0
#         for hx, hy in house:
#             min_cost = float('inf')
#             for sx, sy in selected:
#                 min_cost = min(min_cost, abs(hx-sx) + abs(hy-sy))
#             total_cost+= min_cost
#         result.append(total_cost)
#         return
#     for i in range(start, len(store)):
#         backtracking(k+1, i+1, selected + [store[i]])
def backtracking(k, start, cost, path):
    if k == m:
        result.append(cost)
        return
    for i in range(start, len(store)):  # 'start'를 사용해 중복 방지
        s_x, s_y = store[i]
        temp_cost = 0
        temp_values = []
        for j in range(len(house)):
            x, y, value = house[j]
            temp_values.append(value)
            # 현재까지의 최소 거리와 새로운 가게와의 거리 비교
            new_val = abs(s_x - x) + abs(s_y - y)
            house[j] = [x, y, min(house[j][2], new_val)]
            temp_cost += house[j][2]
        # 현재 가게를 선택
        path.append(store[i])  # path에 현재 가게 추가
        # 백트래킹 호출
        backtracking(k + 1, i + 1, temp_cost, path)
        # 백트래킹이 끝난 후 원래 상태로 복구
        path.pop()
          # house 리스트를 원래 상태로 복구
        for j in range(len(house)):
            house[j][2] = temp_values[j]
house = []
store = []
result = []
for i in range(n):
    for j in range(n):
        if(matrix[i][j] == 1):
            house.append([i, j, float('inf')])
        elif matrix[i][j] == 2:
            store.append((i,j))
backtracking(0, 0, 0, [])
print(min(result))