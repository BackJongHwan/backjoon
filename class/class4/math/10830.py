# N <=5 -> 25개의 수
# A^B % 1000
import sys
input = sys.stdin.readline

'''
나머지 법칙과 지수법칙을 이용하여 해결
지수법칙: A^m +n = A^m * A^n
나머지 법칙 = (AB) % c = (A % C)(B % C)
'''
def matrix_multiply(A, B):
    result = [[0] *n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000  # 결과를 1000으로 나눈 나머지로 유지
    return result

def divide(matrix, b):
    # print(b)
    if b == 1:
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] += matrix[i][j] % 1000
        return result
    half = divide(matrix, b // 2)
    result = matrix_multiply(half, half)
    if b % 2 == 1:  # b가 홀수라면 matrix를 한 번 더 곱함
        result = matrix_multiply(result, matrix)
    return result
def divide2(matrix, b):
    # print(b)
    if b == 1:
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] += matrix[i][j] % 1000
        return result
    half = divide(matrix, b // 2)
    if b % 2 == 0:
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += half[i][k] * half[k][j]
        for i in range(n):
            for j in range(n):
                result[i][j] %= 1000
        # print(result)
        return result
    else:
        result = [[0] * n for _ in range(n)]
        temp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    temp[i][j] += half[i][k] * half[k][j]
                temp[i][j] %= 1000
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += temp[i][k] * matrix[k][j]
        for i in range(n):
            for j in range(n):
                result[i][j] %= 1000
        return result
n, b= map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

value = divide2(matrix, b)
for row in value:
    print(' '.join(map(str, row)))
# print(value)