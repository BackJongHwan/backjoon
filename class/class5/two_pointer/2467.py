# 10^9
# two pointer를 이용해서 index
n = int(input())
nums = list(map(int,input().split()))

result_left = 0
result_right = n - 1
near_0 = nums[result_left] + nums[result_right]
left = 0
right = n-1
while(left < right):
    k = nums[left] + nums[right]
    if(abs(near_0) > abs(k)):
        near_0 = k
        result_left = left
        result_right = right
    if(k > 0):
        right -= 1
    elif k < 0:
        left += 1
    else:
        break

print(nums[result_left], nums[result_right])