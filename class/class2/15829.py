l = int(input())
input_string = input()
result = 0
k = 0
m = 1234567891
for word in input_string:
    result += (ord(word) - ord('a') + 1) * (31 ** k)
    k += 1
print(result % m)