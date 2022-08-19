score = []

for i in range(1, 6):
    data = int(input())
    if data < 40:
        data = 40
    score.append(data)

print(int(sum(score) / len(score)))