def is_group(str):
    idx = 0
    alpha = [0] * 26
    while idx < len(str):
        idx_alpha = (ord(str[idx]) - ord('a'))
        if(alpha[idx_alpha] == 0):
            alpha[idx_alpha] = 1
            while True:
                if((idx + 1) == len(str)):
                    break
                if str[idx] == str[idx + 1]:
                    idx += 1
                else:
                    break
            idx += 1
        else:
            return 0
    return 1
num_case = int(input())
num_group = 0
for _ in range(num_case):
    str = input()
    num_group += is_group(str)
print(num_group)