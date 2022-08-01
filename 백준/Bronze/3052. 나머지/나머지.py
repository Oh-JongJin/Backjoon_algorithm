A = []
result = []

for i in range(1, 11):
    A.append(int(input()))
    result.append(A[i - 1] % 42)
print(len(list(dict.fromkeys(result))))