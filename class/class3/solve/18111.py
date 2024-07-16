import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = []
for _ in range(n):
    ground.append(list(map(int ,input().split())))
min_h = min(min(row) for row in ground)
max_h = max(max(row) for row in ground)
check = 0
min_time = 0
max_heigth = 0
for h in range(min_h, max_h + 1):
    block = b
    time = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] > h:
                diff = ground[i][j] - h
                block += diff
                time += 2 * diff
            else:
                diff = h - ground[i][j]
                block -= diff
                time += diff
    if block >= 0:
        if check == 0:
            check = 1
            min_time = time
            max_heigth = h
        else:
            if(min_time >= time):
                min_time = time
                max_heigth = h
print(min_time, max_heigth)