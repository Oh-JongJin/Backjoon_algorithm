count = int(input())
for i in range(count):
    index = int(input())
    zero, one = 1, 0
    for _ in range(index):
        zero, one = one, zero + one
    print(zero, one)