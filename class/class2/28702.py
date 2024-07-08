str1 = input()
str2 = input()
str3 = input()
#string 중 digit가 있으면
result = 0
if(str1.isdigit()):
    str1 = int(str1)
    result = str1 + 3
if(str2.isdigit()):
    str2 = int(str2)
    result = str2 + 2
if(str3.isdigit()):
    str3 = int(str3)
    result = str3 + 1
if(result == 0):
    print("Fizz")
else:
    if(result % 3 == 0):
        if(result % 5 == 0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif(result % 5 == 0):
        print("Buzz")
    else:
        print(result)

