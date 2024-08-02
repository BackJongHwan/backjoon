def solve(n, m):
    def DFS(start, path):
        if(len(path) == m):
            print(" ".join(map(str, path)))
            return
        for i in range(start, n + 1):
            path.append(i)
            DFS(i, path)
            path.pop()
    DFS(1, [])    
n, m = map(int ,input().split())
solve(n, m)