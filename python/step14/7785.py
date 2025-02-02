#O(nlogn)
n = int(input())
member_dict = {}
for _ in range(n):
    name, state = input().split()
    member_dict[name] = state
member_list = sorted(member_dict.items(), reverse=True)
for (name, state) in member_list:
    if(state == 'enter'):
        print(name)