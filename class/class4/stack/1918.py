# import sys
# input = sys.stdin.readline

# string = input().strip()
# # 1. 괄호 치기
# def add_brackets(expression):
#     operand = []
#     operator = []
#     priority = {'+': 1, '-': 1, '*': 2, '/': 2}

#     for ch in expression:
#         if ch.isalpha():  # 피연산자 (A, B, C)
#             operand.append(ch)
#         elif ch == '(':
#             operator.append(ch)
#         elif ch == ')':
#             while operator and operator[-1] != '(':
#                 op2 = operand.pop()
#                 op1 = operand.pop()
#                 op = operator.pop()
#                 expression = f"({op1}{op}{op2})"
#                 operand.append(expression)
#             operator.pop()  # '(' 제거
#         else:  # 연산자 (+, -, *, /)
#             while operator and operator[-1] != '(' and priority[operator[-1]] >= priority[ch]:
#                 op2 = operand.pop()
#                 op1 = operand.pop()
#                 op = operator.pop()
#                 expression = f"({op1}{op}{op2})"
#                 operand.append(expression)
#             operator.append(ch)

#     while operator:
#         op2 = operand.pop()
#         op1 = operand.pop()
#         op = operator.pop()
#         expression = f"({op1}{op}{op2})"
#         operand.append(expression)

#     return operand[0]  # 완전한 괄호 추가된 식 반환
# bracketed_expression = add_brackets(string)
# # print(bracketed_expression)  # 1. 괄호 치기 결과
# # 2. 괄호 없애기
# operand = []
# operator = []
# for ch in bracketed_expression:
#     # print(operand)
#     # print(operator)
#     if ch == ')':
#         op2 = operand.pop()
#         op1 = operand.pop()
#         op = operator.pop()
#         operand.append(op1+op2+op)
#     # operand에 해당하면
#     elif ch.isalpha():
#         operand.append(ch)
#     elif ch == '(':
#         continue
#     else:
#         operator.append(ch)
# result = operand[0]
# print(result)
import sys
input = sys.stdin.readline

string = input().strip()

# ✅ **중위 표기법 → 후위 표기법 변환**
def infix_to_postfix(expression):
    operand = []
    operator = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    for ch in expression:
        if ch.isalpha():  # 피연산자 (A, B, C)
            operand.append(ch)
        elif ch == '(':
            operator.append(ch)
        elif ch == ')':
            while operator and operator[-1] != '(':
                operand.append(operator.pop())  # '(' 만나기 전까지 연산자 이동
            operator.pop()  # '(' 제거
        else:  # 연산자 (+, -, *, /)
            while operator and operator[-1] != '(' and priority[operator[-1]] >= priority[ch]:
                operand.append(operator.pop())  # 우선순위가 높은 연산자 처리
            operator.append(ch)

    while operator:
        operand.append(operator.pop())

    return "".join(operand)  # 후위 표기법 반환

postfix = infix_to_postfix(string)
print(postfix)  # 후위 표기법 출력
