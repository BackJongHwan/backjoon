x = []
y = []
result_x = 0
result_y = 0
for i in range(3):
    point_x, point_y = map(int, input().split())
    x.append(point_x)
    y.append(point_y)
for i in x:
    if(x.count(i) == 2):
        continue
    result_x = i
for i in y:
    if(y.count(i) == 2):
        continue
    result_y = i 
print(result_x, result_y)