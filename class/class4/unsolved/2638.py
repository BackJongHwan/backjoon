# N, M <= 100 O(N^3) 가능
# 많아야 50초 걸림
# BFS 50번 돌리기
# (0, 0)에서 시작해서 BFS 돌리고 각 block마다 check하고 없애기

import sys
input = sys.stdin.readline

n, m = map(int , input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
