#using O(n) algorithm
x = int(input())
#p is 분자,q is 분모
p, q = 1, 1
temp = 1
while x > temp:
    x -= temp
    temp += 1
    q += 1
while x > 1:
    x -= 1
    q -= 1
    p += 1
if(temp % 2 == 1):
    p, q = q, p
print(str(p) +"/" + str(q))
