# n, m = 10^5
# O(nlogn)?? IDK
n, m = map(int ,input().split())
memo_dict = {}
for _ in range(n):
    site, password = input().split()
    memo_dict[site] = password
for _ in range(m):
    site = input()
    print(memo_dict[site])