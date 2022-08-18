chess = [1, 1, 2, 2, 2, 8]
dong_hyeok = list(map(int, input().split()))
data = []

for i in range(len(chess)):
    data.append(chess[i] - dong_hyeok[i])

a = ' '.join(str(s) for s in data)
print(a)
