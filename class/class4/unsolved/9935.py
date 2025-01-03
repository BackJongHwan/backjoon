# str1 -> 1,000,000
# str2 -> 36
# O(N)으로

str1 = input()
str2 = input()

# while(True):
#     idx = str1.find(str2)
#     if(idx == -1):
#         break
#     str1 = str1[:idx] + str1[idx+len(str2):]
# if str1 == "":
#     print("FRULA")
# else:
#     print(str1)
stack = []
idx = [] 
for char in str1:
    # print(char, end="")
    stack.append(char)
    # stack.pop()



if stack == []:
    print("FRULA")
else:
    print("".join(stack))

# print()
