n = int(input())
str_list = []
for _ in range(n):
    word = input()
    if(word not in str_list):
        str_list.append(word)
str_list.sort(key = lambda word :(len(word), word) )
for i in str_list:
    print(i)