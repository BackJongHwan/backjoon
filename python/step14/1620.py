#n, m -> 10^6 => O(nlogn)
import sys
n, m = map(int, sys.stdin.readline().split())
name_dic = {}
num_dic = {}
for i in range(n):
    name = sys.stdin.readline().strip() 
    name_dic[name] = i + 1
    num_dic[i + 1] = name
for _ in range(m):
    question = sys.stdin.readline().strip() 
    if(question.isdigit()):
        print(num_dic[int(question)])
    else:
        print(name_dic[question])