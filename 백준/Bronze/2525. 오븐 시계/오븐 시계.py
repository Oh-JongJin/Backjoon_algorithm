H, M = map(int, input().split())
time = int(input())

spend_time = time + M

if time + M >= 60:
    H = H + spend_time // 60
    M = spend_time % 60
    if H >= 24:
        H -= 24
else:
    M = time + M
print(H, M)