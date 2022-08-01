H, M = map(int, input().split())
result_H = 0
result_M = 0

if M - 45 < 0:
    result_M = 60 + (M - 45)
    if H - 1 < 0:
        result_H = 23
    else:
        result_H = H - 1
else:
    result_H = H
    result_M = M - 45

print(result_H, result_M)