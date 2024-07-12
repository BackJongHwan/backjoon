# n = 300
# O(n^3)
n = int(input())
stair = []
for _ in range(n):
    stair_score = int(input())
    stair.append(stair_score)
# max score of far pervious stair
far_score = []
# max score of adjecent previous stair
adj_score = []
far_score.append(stair[0])
adj_score.append(stair[0])
if(n > 1):
    far_score.append(stair[1])
    adj_score.append(stair[0] + stair[1])
for i in range(2, n):
    score_far = max(far_score[i - 2], adj_score[i - 2]) + stair[i]
    score_adj = far_score[i - 1] + stair[i]
    far_score.append(score_far)
    adj_score.append(score_adj)
print(max(far_score[n-1], adj_score[n-1]))
