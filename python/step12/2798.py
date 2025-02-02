n, m = map(int, input().split())
card = list(map(int, input().split()))
max_val = 0
for i in range(n - 2):
    for j in range(i+1, n - 1):
        for k in range(j + 1, n):
            val = card[i] + card[j] + card[k]
            if(max_val <= val <= m):
                max_val = val
print(max_val)
