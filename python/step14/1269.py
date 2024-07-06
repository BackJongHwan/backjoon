#200,000 -> 2 * 10^6 => O(nlogn)

num_a, num_b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
reseult_set = (set_a | set_b) - (set_a & set_b)
print(len(reseult_set))