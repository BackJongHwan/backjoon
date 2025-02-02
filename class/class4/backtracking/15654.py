def solve(n, m, numList):
    path = []
    def backtracking(depth):
        if depth == m:
            print(" ".join(map(str, path)))
            return
        for i in range(n):
            if numList[i] in path:
                continue
            path.append(numList[i])
            backtracking(depth + 1)
            path.pop()
    backtracking(0)

n, m = map(int ,input().split())
numList = list(map(int, input().split()))
numList.sort()
solve(n, m, numList)