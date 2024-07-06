#O(nlogn)
n, m = map(int, input().split())
people1 = []
people2 = []
for _ in range(n):
    name = input()
    people1.append(name)
for _ in range(m):
    name = input()
    people2.append(name)
set_people = sorted((set(people1) & set(people2)))
print(len(set_people))
for name in set_people:
    print(name)