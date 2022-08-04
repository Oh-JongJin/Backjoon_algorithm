N = int(input())

data = 1
count = 1

while N > data:
    data += 6 * count
    count += 1
print(count)