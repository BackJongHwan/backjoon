# n -> 5 * 10^5 ==> O(nlogn)
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
card_list = deque()
for i in range(n):
    card_list.append(i + 1)
while card_list:
    if(len(card_list) == 1):
        print(card_list.pop())
        break
    card1 = card_list.popleft()
    card2 = card_list.popleft()
    card_list.append(card2)
