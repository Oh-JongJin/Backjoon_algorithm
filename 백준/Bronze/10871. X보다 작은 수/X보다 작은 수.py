N, X = map(int, input().split())

A = list(map(int, input().split()))
data = []

for i in A:
    if i < X:
        data.append(i)
print(*data)
