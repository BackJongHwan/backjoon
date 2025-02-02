n = int(input())
temp = 1 
step = 0
while n > temp:
    temp += step * 6
    step += 1
if(n == 1):
    print(1)
else:
    print(step)