while True:
    num = input()
    palin = True
    if(num =='0'):
        break
    for i in range(len(num) // 2):
        if(num[i] != num[len(num) - 1 - i]):
            palin = False
            break
    if palin:
        print("yes")
    else:
        print("no")