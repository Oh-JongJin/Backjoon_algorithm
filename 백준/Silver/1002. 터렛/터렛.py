from math import sqrt
T = int(input())

def get_intersections(x0, y0, r0, x1, y1, r1):

    d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    if d > r0 + r1:
        return 0
    if d < abs(r0 - r1):
        return 0
    if d == 0 and r0 == r1:
        return -1
    else:
        a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
        h = sqrt(r0 ** 2 - a ** 2)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d

        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d

        if x3 == x4 and y3 == y4:
            return 1
        return 2

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(get_intersections(x1, y1, r1, x2, y2, r2))
