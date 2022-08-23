T = int(input())
for i in range(T):
    count = 0
    grade = 0
    result = input()
    for x in range(len(result)):
        if result[x] == 'O':
            count += 1
        else:
            count = 0
        grade += count

    print(grade)