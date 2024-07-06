n = int(input())
list1 = list(map(int, input().split()))
dic ={}
for num in list1:
    dic[num] = 1
m = int(input())
list2 = list(map(int,input().split()))
for num in list2:
    if(num in dic):
        print(1, end=" ")
    else:
        print(0, end=" ")
print()