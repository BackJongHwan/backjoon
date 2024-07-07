#n = 1000 -> O(n^2)
import sys
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
stack = []
i = 0
line = 1
while i < n:
    if(i == n - 1):
        if(num_list[i] != line):
            print("Sad")
            exit(0)
        else:
            line += 1
    else:
        if(num_list[i] > num_list[i + 1]):
            stack.append(num_list[i])
        else:
            if(num_list[i] == line):
                line += 1
                if stack:
                    while stack[-1] < num_list[i+1]:
                        if(line == stack.pop()):
                            line += 1
                        else:
                            print("Sad")
                            exit(0)
                        if not stack:
                            break
            else:
                print("Sad")
                exit(0)
    i += 1
print("Nice")

# import sys
# input = sys.stdin.readline

# n = int(input())
# num_list = list(map(int, input().split()))

# stack = []
# current = 1

# for num in num_list:
#     while stack and stack[-1] == current:
#         stack.pop()
#         current += 1
    
#     if num == current:
#         current += 1
#     else:
#         stack.append(num)

# while stack and stack[-1] == current:
#     stack.pop()
#     current += 1

# if current == n + 1:
#     print("Nice")
# else:
#     print("Sad")