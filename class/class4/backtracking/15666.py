# def backtracking(k, idx, len):
#     if k == m:
#         for i in range(m):
#             print(answer[i], end=' ')
#         print()
#         return
#     while(idx < len):
#         answer[k] = num_list[idx]
#         backtracking(k+1, idx, len)
#         idx += 1


# n, m = map(int, input().split())
# num_list = sorted(set(map(int, input().split())))
# answer = [-1] * m
# backtracking(0, 0, len(num_list))
def backtracking(k, idx):
    if k == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return
    for i in range(idx, len(num_list)):
        answer.append(num_list[i])
        backtracking(k + 1, i)
        answer.pop() #backtracking
n, m = map(int, input().split())
num_list = sorted(set(map(int, input().split())))
answer = []
backtracking(0, 0)