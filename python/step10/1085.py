x, y, w, h = map(int, input().split())
a = min(x, y, h - y, w - x)
print(a)