a1, a0 = map(int, input().split())
c = int(input())
n = int(input())
if(a1 > c):
    print(0)
else:
    if(a1 * n + a0 <= c * n):
        print(1)
    else:
        print(0)

