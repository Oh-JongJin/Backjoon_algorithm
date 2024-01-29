length, cnt = map(int, input().split(' '))
baguni = []
result = ""
for i in range(length):
    baguni.append(0)

for x in range(cnt):
    i, j, k = map(int, input().split(' '))
    for y in range(i-1, j):
        baguni[y] = k

print(*baguni, sep=' ')

