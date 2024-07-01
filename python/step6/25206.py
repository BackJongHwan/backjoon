sum = 0.0
num = 0.0 
for _ in range(20):
    subject, point, grade = input().split()
    if(len(grade) == 1):
        if(grade == 'P'):
            continue
        else:
            num += float(point)
    else:
        num += float(point)
        if(grade[0] == 'A'):
            num_grade = 4.0
        elif(grade[0] == 'B'):
            num_grade = 3.0
        elif(grade[0] == 'C'):
            num_grade = 2.0
        else:
            num_grade = 1.0
        if(grade[1] == '+'):
            num_grade += 0.5
        sum += float(point) * num_grade
print(sum / num)