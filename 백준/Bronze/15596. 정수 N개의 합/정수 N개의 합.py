def solve(a: list) -> int:
    result = 0

    for i in range(0, len(a)):
        result += a[i]

    return result