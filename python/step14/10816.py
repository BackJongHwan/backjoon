#5 * 10^6 -> O(nlogn)
import sys
input = sys.stdin.readline
n = input().rstrip()
n_list = list(map(int, input().split()))
m = input().rstrip()
m_list = list(map(int, input().split()))
number_dict = {}
for i in n_list:
    if(i not in number_dict):
        number_dict[i] = 1
    else:
        number_dict[i] += 1
for num in m_list:
    if(num in number_dict):
        print(number_dict[num], end= " ")
    else:
        print(0, end=" ")
print()