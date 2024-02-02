N, M = map(int, input().split())
baguni = list(range(1, N + 1))

for i in range(M):
    replace1, replace2 = map(int, input().split())
    baguni[replace1-1], baguni[replace2-1] = baguni[replace2-1], baguni[replace1-1]

print(*baguni, sep=' ')
