test = int(input())
for _ in range(test):
    h, w, n = map(int, input().split())
    room = 0 
    floor = 0
    if(n % h == 0):
        room += n // h
    else:
        room += n // h + 1
    floor = n % h
    if(n % h == 0):
        floor = h
    result = str(floor)
    if(room < 10):
        result += str('0') +  str(room)
    else:
        result += str(room)
    print(result)