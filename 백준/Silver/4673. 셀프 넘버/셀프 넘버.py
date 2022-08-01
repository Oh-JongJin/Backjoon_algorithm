A = []
result = []


for i in range(1, 10001):
    A.append(i)

for i in range(len(A)):
    length = len(str(A[i]))
    data = 0
    for j in range(length):
        data += int(str(A[i])[j])
        if j == length - 1:
            result.append(data + A[i])

real_result = [i for i in A if i not in result]
for i in real_result:
    print(i)