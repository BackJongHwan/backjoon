#O(nlogn)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n = int(input())
trees = []
gaps = []
for _ in range(n):
    tree = int(input())
    trees.append(tree)
for i in range(n-1):
    gaps.append(trees[i+1] - trees[i])
k = gcd(gaps[0], gaps[1]) 
for i in range(2, len(gaps)):
    k = gcd(k, gaps[i])
result = (trees[len(trees) - 1] - trees[0]) // k - len(trees) + 1
print(result)