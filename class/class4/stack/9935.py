# str1 -> 1,000,000
# str2 -> 36
# O(N)으로 -> stack을 이용함

s1 = input()
s2 = input()

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
temp_idx = []
k = 0
end_k = len(s2) - 1
def pop_stack():
    for _ in range(len(s2)):
        stack.pop()

# for char in s1:
    # stack.append(char)
    # # print(k)
    # if(char == s2[k]):
    #     if(k == end_k):
    #         if(temp_idx != []):
    #             k = temp_idx.pop()
    #         else:
    #             k = 0
    #         # print("pop!!")
    #         pop_stack()
    #     else:
    #         k += 1
    # else:
    #     if(char == s2[0]):
    #         temp_idx.append(k)
    #         k = 1
    #     else:
    #         temp_idx = []
    #         k = 0
for char in s1:
    stack.append(char)
    if char == s2[k]:
        k += 1
        if k > end_k:  # s2가 완전히 매칭된 경우
            pop_stack()
            k = 0
            # 스택에서 남아있는 문자가 s2의 부분과 일치하면 k를 재설정
            for i in range(1, len(s2)):
                if stack[-i:] == list(s2[:i]):
                    k = i
                    break
    else:
        if char == s2[0]:
            k = 1
        else:
            k = 0 

if stack == []:
    print("FRULA")
else:
    print("".join(stack))

# print()
