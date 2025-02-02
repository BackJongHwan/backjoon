import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    result = 1 
    n = int(input())
    dict = {}
    num_list = []
    for _ in range(n):
        name, category = input().split()
        if category not in dict:
            dict[category] = 1 
        else:
            dict[category] += 1
    for num in dict.values():
        result *= (num + 1)
    print(result - 1)