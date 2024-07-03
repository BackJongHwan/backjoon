a, b, v = map(int, input().split())
gap = a - b
if((v - a) >= gap):
    day = (v-a)//gap + 1
    if((v-a) % gap != 0):
        day += 1
else:
    day = 2
if(v == a):
    day = 1

print(day)