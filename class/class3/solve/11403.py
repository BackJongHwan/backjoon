#floyd-washell algorithm
n = int(input())
adj_list = []
for _ in range(n):
    adj_list.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if(adj_list[i][k] == 1 and adj_list[k][j] == 1):
                adj_list[i][j] = 1
for i in range(n):
    print((" ").join(map(str, adj_list[i])))