n = int(input())
cordinate = []
for _ in range(n):
    x, y = map(int, input().split())
    cordinate.append((x, y))
cordinate.sort()
for i in range(n):
    print(cordinate[i][0], cordinate[i][1])