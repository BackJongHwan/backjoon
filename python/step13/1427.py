n = input()
num_list = list(map(int, n))
num_list.sort(reverse=True)
print("".join(map(str,num_list)))