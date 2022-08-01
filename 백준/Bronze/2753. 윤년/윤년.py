def leaf_year(year: int):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return 1
        else:
            return 0
    else:
        return 0


n = int(input())
print(leaf_year(n))