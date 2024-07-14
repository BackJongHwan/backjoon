#100 -> O(n^3)
#10^4 -> O(nlogn)
n, a, b = map(int,input().split())
assign_list = list(map(int, input().split())) 
assign_list.sort()
effort = a
complete_task = 0

#no sleep
task = 0
time = 0
for i in range(n):
    time += a
    if(assign_list[i] < time):
        break
    task += 1
complete_task = task
# #with sleep
for x in range(a):
    task = 0
    time = 0
    # before sleep
    for i in range(n):
        time += a
        if(assign_list[i] < time):
            if(complete_task < task):
                complete_task = task
            break
        task += 1
        effort = x - a
        time += b * x
        #after sleep
    for j in range(i , n):
        time += effort 
        if(assign_list[j] < time):
            if(complete_task < task):
                complete_task = task
            break
        task += 1
print(complete_task)