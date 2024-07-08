test = int(input())
for _ in range(test):
    score = 0
    quiz = input()
    succ = 0
    for ans in quiz:
        if(ans == 'O'):
            succ += 1
            score += succ
        else:
            succ = 0
    print(score)