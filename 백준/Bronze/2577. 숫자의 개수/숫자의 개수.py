A = int(input())
B = int(input())
C = int(input())

data = str(A * B * C)

for i in range(0, 10):
    print(data.count(str(i)))