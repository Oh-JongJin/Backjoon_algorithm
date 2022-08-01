N = int(input())
score = list(map(int, input().split()))
data = []

M = max(score)

for i in range(N):
    data.append((score[i] / M) * 100)
print(sum(data) / N)