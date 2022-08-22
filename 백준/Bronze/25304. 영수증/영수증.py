X = int(input())
N = int(input())
data = []

for i in range(N):
    a, b = map(int, input().split())
    data.append(a * b)

if sum(data) == X:
    print('Yes')
else:
    print('No')
