# n = 10^16
# O(N)은 불가능 -> O(logN)으로 해야하나?
# n번째 fibo % 1,000,000,007
# 나머지 법칙
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이를 10^6으로 설정
'''
(A + B) mod C = ((A mod C) + (B mod C)) mod C
AB mod C = ((A mod C) * (B mod C)) mod C
'''
# dp를 이용해서 하는 거 같은데 너무 큰가? -> N의 크기가 매우 큼
n = int(input())
mod = 1000000007
dict = {}
# 홀수 -> Fn = F(n//2 +1)^2 + F(n//2)^2
# 짝수 -> Fn = (F(n//2) + F(n//2 -1))F(n//2) + F(n//2)F(n//2 -1)
dict[0] = 0
dict[1] = 1
for i in range(2, 10):
    dict[i] = dict[i-2] + dict[i-1]

def get_fibo(num):
    # 이미 있는 거라면
    if num in dict:
        return dict[num]
    else:
        # 홀수면
        if(num % 2 == 1):
            num1 = get_fibo((num//2 + 1))
            num2 = get_fibo((num//2))
            dict[num] = (((num1 % mod) * (num1 % mod) % mod) + ((num2 % mod) *(num2 % mod) % mod))  % mod
            return dict[num]
        # 짝수면
        else:
            num1 = get_fibo(num//2)
            num2 = get_fibo(num//2 - 1)
            dict[num] = (((num1 + num2) * num1)  + num1 * num2) % mod
            return dict[num]
print(get_fibo(n))