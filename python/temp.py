result = '?'
str = input()
str = str.upper()
frq_list = []
for _ in range(ord('A'), ord('Z') + 1):
    frq_list.append(0)
for i in range(len(str)):
    frq_list[ord(str[i]) - ord('A')] += 1
max_frq = max(frq_list)
max_count = 0
for i in range(len(frq_list)):
    if(frq_list[i] == max_frq):
        max_count += 1
        result = chr(i + ord('A'))
        if(max_count != 1):
            result ='?'
            break
print(result)