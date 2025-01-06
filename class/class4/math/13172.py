m = int(input())
mod = 1000000007

def modular_exponentiation(base, exp, mod):
    result = 1  # 결과 초기화
    base = base % mod  # base를 mod 범위로 줄임

    while exp > 0:
        # 지수가 홀수인 경우 결과에 base를 곱함
        if exp % 2 == 1:
            result = (result * base) % mod

        # base를 제곱하고 지수를 반으로 나눔
        base = (base * base) % mod
        exp //= 2

    return result

def modular_inverse(b, mod):
    return modular_exponentiation(b, mod - 2, mod)

def solve(a, b):
    # a / b ≡ a × b^(-1) (mod mod)
    return (a * modular_inverse(b, mod)) % mod

result = 0
for _ in range(m):
    n, s = map(int, input().split())
    result = (result + solve(s, n)) % mod  # 모듈러 연산 적용

print(result)

