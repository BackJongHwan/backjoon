while True:
    side = list(map(int, input().split()))
    if(side[0] == 0):
        break
    max_val = 0
    max_idx = 0
    for i in range(3):
        if(max_val < side[i]):
            max_val = side[i]
            max_idx = i
    sum = 0
    for i in range(3):
        if(i != max_idx):
            sum += side[i]
    if(sum <= max_val):
        print("Invalid")
    else:
        if(side[0] == side[1] and side[0] == side[2]):
            print("Equilateral")
        elif(side[0] == side[1] or side[1] == side[2] or side[0] == side[2]):
            print("Isosceles")
        else:
            print("Scalene")
