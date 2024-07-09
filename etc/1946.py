# n = 10^5 O(nlogn)
import sys
input = sys.stdin.readline
test = int(input())
for _ in range(test):
    n = int(input())
    apply_list = []
    for _ in range(n):
        rank1, rank2 = map(int, input().split())
        apply_list.append((rank1, rank2))
    apply_list.sort()
    #print(apply_list)
    rank = apply_list[0][1]
    #print(rank)
    cnt = 0
    for i in range(n):
        if(rank > apply_list[i][1]):
            rank = apply_list[i][1]
            cnt += 1
    print(cnt + 1)