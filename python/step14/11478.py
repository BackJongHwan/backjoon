# len <= 1000 -> O(n^2)
s = input()
set_str = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        set_str.add(s[i:j + 1])
print(len(set_str))