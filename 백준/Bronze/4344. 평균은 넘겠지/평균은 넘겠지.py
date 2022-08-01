C = int(input())
data = []
result = []
flag = 0

while flag <= C - 1:
    data = list(map(int, input().split()))
    count = 0
    average = sum(data[1:]) / len(data[1:])
    for j in range(data[0]):
        if data[j + 1] > average:
            count += 1
    result.append(f'{(count / data[0] * 100):.3f}%')
    flag += 1

for i in range(len(result)):
    print(result[i])