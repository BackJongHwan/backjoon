# n, m 10^5 -> O(nlongn)
import sys
input = sys.stdin.readline
# slicing에 시간이 오래 걸림
'''
def binary_serach(num, list):
    if not list:
        return False
    middle = len(list) // 2
    if(num == list[middle]):
        return True
    else:
        if(num < list[middle]):
            return binary_serach(num, list[0:middle])
        else:
            return binary_serach(num, list[middle + 1:])
'''
def binary_search(num, list, left, right):
    if(left > right):
        return False
    middle = (left + right) // 2
    if(num == list[middle]):
        return True
    elif(num > list[middle]):
        return binary_search(num, list,  middle+ 1, right)
    else:
        return binary_search(num, list, left,  middle-1)

n = int(input())
n_list = list(map(int ,input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))
#list search O(n), so whole algorithm is O(n^2)
'''
for num in m_list:
    if num in n_list:
        print(1)
    else:
        print(0)
'''
for num in m_list:
    if binary_search(num, n_list, 0, n - 1):
        print(1)
    else:
        print(0)