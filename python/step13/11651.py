n = int(input())
cordinate = []
for _ in range(n):
    x, y = map(int, input().split())
    cordinate.append((x, y))
cordinate.sort(key = lambda cordinate: (cordinate[1], cordinate[0]))
for i in range(n):
    print(cordinate[i][0], cordinate[i][1])