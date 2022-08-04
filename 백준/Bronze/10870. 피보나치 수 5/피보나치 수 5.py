n = int(input())

n2_pre = 0
n2 = 0
n1 = 1

value = []

for i in range(n + 1):
    value.append(n2)

    n2 = n1
    n1 = n2_pre + n1
    n2_pre = n2

print(value[-1])