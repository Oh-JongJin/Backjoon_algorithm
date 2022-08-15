a, b, c = map(int, input().split())
maximum = max(a, b, c)
prize = 0

if a == b == c:
    prize = 10000 + (a * 1000)
elif a == b != c or a == c != b:
    prize = 1000 + (a * 100)
elif a != b == c:
    prize = 1000 + (b * 100)
elif a != b != c:
    prize = maximum * 100

print(prize)