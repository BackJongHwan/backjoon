#recusive time error
'''
def get_people(k, n):
    result = 0
    if(k == 0):
        return n
    else:
        for i in range(1, n + 1):
            result += get_people(k - 1, i)
        return result
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    people = get_people(k, n)
    print(people)
'''

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    num_list = []
    for i in range(1, n + 1):
        num_list.append(i)
    for i in range(0, k):
        new_list = []
        for j in range(0, n):
            new_list.append(sum(num_list[0:j + 1]))
        for j in range(0, n):
            num_list[j] = new_list[j]
    print(num_list[n-1])