count = int(input())
data = list(map(int, input().split(' ')))
find = int(input())

cnt = 0
for i in data:
    if i == find:
        cnt += 1

print(cnt)
