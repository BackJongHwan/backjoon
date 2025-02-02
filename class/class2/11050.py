n , k = map(int ,input().split())
p = 1
q1 = 1
q2 = 1
for i in range(1, n + 1):
    p *= i
for i in range(1, k + 1):
    q1 *= i
for i in range(1, n - k + 1):
    q2 *= i
print((p // q1) // q2)