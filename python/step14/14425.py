n, m = map(int, input().split())
string_set = set() 
for _ in range(n):
    str_input = input()
    string_set.add(str_input)
result = 0
for _ in range(m):
    str_input = input()
    if(str_input in string_set):
        result += 1
print(result)