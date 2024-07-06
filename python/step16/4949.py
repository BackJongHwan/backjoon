import sys
input = sys.stdin.readline


while True:
    stack = []
    input_str = input().rstrip()
    blance = True
    if(input_str == '.'):
        break
    for char in input_str:
        if(char == '(' or char == '['):
            stack.append(char)
        elif(char == ')'):
            if not stack:
                blance = False
                break
            if(stack.pop() != '('):
                blance = False
                break
        elif(char == ']'):
            if not stack:
                blance = False
                break
            if(stack.pop() != '['):
                blance = False
                break
        else:
            continue
    if stack:
        blance = False
    if(blance):
        print("yes")
    else:
        print("no")