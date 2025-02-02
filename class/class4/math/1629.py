# #
# # a = 5
# # b = 7
# # for i in range(10):
# #     print(a % b, i + 1, a)
# #     a *= a
# # 반복되는 특성을 가지는데 
# a, b, c= map(int, input().split())
# # check = False
# dict = {}
# dict2 = {}
# # if c is 1 나머지는 0
# if(c == 1):
#     print(0)
# else:
#     # a가 1이면 c가 0이 아닌 이상 나머지는 1
#     if(a == 1):
#         print(1)
#     else:
#         #general case
#         idx = 1
#         num = a
#         while(True):
#             temp = num % c
#             num = (a * temp) % c
#             if temp in dict:
#                 break
#             else:
#                 dict[temp] = idx
#                 dict2[idx] = temp
#                 idx +=1
#         idx -= 1
#         # print(dict)
#         # print(idx, b)
#         result = b % idx 
#         # print(result)
#         # print(dict)
#         # print(dict2)
#         print(dict2[result])

'''
나머지 법칙과 지수법칙을 이용하여 해결
지수법칙: A^m +n = A^m * A^n
나머지 법칙 = (AB) % c = (A % C)(B % C)
'''
def divide(a, b):
    if b == 0:
        return 1  # a^0 = 1
    if b == 1:
        return a % c
    half = divide(a, b // 2) % c
    if b % 2 == 0:  # 짝수
        return (half * half) % c
    else:  # 홀수
        return (half * half * (a % c)) % c
a, b, c= map(int, input().split())
result = divide(a, b)
print(result)