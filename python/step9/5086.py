while True:
    n1, n2 = map(int, input().split())
    if(n1 == 0 and n2 == 0):
        break
    #facor
    if(n2 % n1 == 0 and n1 % n2 == n1):
        print("factor")
    #mutiple
    elif(n1 % n2 == 0 and n2 % n1 == n2):
        print("multiple")
    else:
        print("neither")