a, b = map(int, input().split())

def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

print(gcd(a, b))
print(int(a * b / gcd(a, b)))
