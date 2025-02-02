n = int(input())
members = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    members.append((age, name, i))
members.sort(key = lambda members : (members[0], members[2]))
for mem in members:
    print(mem[0], mem[1])