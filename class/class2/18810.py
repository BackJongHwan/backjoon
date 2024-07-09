#n = 3 * 10^5 -> O(nlogn)
import sys
input = sys.stdin.readline
def rnd(num):
    diff = num - int(num)
    if diff >= 0.5:
        return int(num) + 1
    else:
        return int(num)
n = int(input())
rank_list = []
for _ in range(n):
    rank = int(input())
    rank_list.append(rank)
rank_list.sort()
delete = (n * 0.15)
delete = rnd(delete)
sum = 0
for i in range(delete, n-delete):
    sum += rank_list[i]
if (n - 2 * delete) > 0:
    print(rnd(sum / (n - 2 * delete)))
else:
    print(0)