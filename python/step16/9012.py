n = int(input())
for _ in range(n):
    stack = []
    paren = input()
    check = 0
    for i in paren:
        if(i == '('):
            stack.append('(')
        else:
            if(len(stack) == 0):
                check = 1
                continue
            else:
                stack.pop()
    if(len(stack) != 0):
        check = 1
    if(check == 1):
        print("NO")
        continue
    print("YES")