# N = 10^5
# sum >= S
import sys
input = sys.stdin.readline
n, s = map(int ,input().split())
nums = list(map(int , input().split()))
# print(nums)
# 이 방식은 left, right의 크기가 sort되어 있지 않다면 맞지 않는 방식!!
def two_pointer_wrong():
    # 초기 상태: 전체 배열 길이로 시작
    left, right = 0, n
    current_sum = sum(nums)  # 처음에는 전체 합으로 시작
    if current_sum < s:
        return 0
    min_length = n  # 최소 길이 설정
    while left <= right:
        if current_sum >= s:
            min_length = min(min_length, right - left)
            if nums[left] < nums[right -1]:
                current_sum -= nums[left]
                left += 1
            else:
                current_sum -= nums[right - 1]
                right -= 1
        else:
            break
    return min_length
def two_pointer():
    left, right = 0, 0
    current_sum = 0
    
result = two_pointer()
print(result)