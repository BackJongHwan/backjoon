degree = []
for _ in range(3):
    x = int(input())
    degree.append(x)
if(sum(degree) != 180):
    print("Error")
else:
    if(degree[0] == degree[1]):
        if(degree[0] == degree[2]):
            print("Equilateral")
        else:
            print("Isosceles")
    else:
        if((degree[0] == degree[2]) or(degree[1] == degree[2])):
            print("Isosceles")
        else:
            print("Scalene")