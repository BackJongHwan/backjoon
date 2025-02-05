import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 증가
input = sys.stdin.readline

n, root, q = map(int, input().split())
tree = dict()
parent = [-1] *(n+1)
size = [-1] * (n + 1)

# tree 만들기
for i in range(1, n+1):
    tree[i] = []
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def make_tree(node, par):
    parent[node] = par
    size[node] = 1
    for child in tree[node]:
        if child == par:
            continue
        make_tree(child, node)
        size[node] += size[child]
make_tree(root, -1)

for _ in range(q):
    k = int(input())
    print(size[k])