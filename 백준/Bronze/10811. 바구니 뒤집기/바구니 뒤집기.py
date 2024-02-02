N, M = map(int, input().split())
baguni = list(range(1, N + 1))

for i in range(M):
    replace1, replace2 = map(int, input().split())
    rep_list = baguni[replace1-1: replace2]
    rep_list.reverse()
    baguni[replace1-1: replace2] = rep_list

print(*baguni, sep=' ')
