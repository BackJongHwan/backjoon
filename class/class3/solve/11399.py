# n = 1000 -> O(n^2)
n = int(input())
p_list = list(map(int, input().split()))
p_list.sort()
total = 0
for i in range(n):
    total += sum(p_list[0:i + 1])
print(total)