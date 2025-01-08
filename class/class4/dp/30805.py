# 위 방법이 아니라 각각의 해당하는 부분수열을 찾고 거기서 가장 사전순으로 느린 부분만 기억하기

# 입력받기
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))


# 이 경우 96 이고 7이 새로운 문자로 들어올 때 97이 아니라 967로 처리하게 되는 경우가 있음

# list를 element로 가지는 2D dp
dp = [[[] for _ in range(n + 1)] for _ in range(m + 1)]


# a -> b 이면 True 반대면 false
def compare_list(a, b):
    if not a:  # a가 빈 리스트인 경우
        return True
    if not b:  # b가 빈 리스트인 경우
        return False
    len_a = len(a)
    len_b = len(b)
    min_len = min(len_a, len_b)
    for i in range(min_len):
        if(a[i] < b[i]):
            return True
        elif a[i] > b[i]:
            return False
    return len_a < len_b

def compare_word(num_list, new_num):
    temp = -1
    for i in range(len(num_list)):
        if num_list[i] < new_num:
            temp = i
            break
    if temp == -1:  # new_num이 num_list의 모든 원소보다 크거나 같을 경우
        return num_list + [new_num]
    else:
        return num_list[:temp] + [new_num]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        # 같다면 더 사전순이 높은 것을 기억함
        if(A[j-1] == B[i-1]):
            dp[i][j] = compare_word(dp[i-1][j-1], A[j-1])
        else:
            if compare_list(dp[i-1][j], dp[i][j-1]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
# print(dp)
print(len(dp[m][n]))
for i in range(len(dp[m][n])):
    print(dp[m][n][i], end = " ")
print()