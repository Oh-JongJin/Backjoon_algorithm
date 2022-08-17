T = int(input())


for x in range(T):
    k = int(input())
    n = int(input())
    human_under = []
    human_now = []

    for i in range(k + 1):
        test = 0
        if i > 1:
            human_under = human_now
            human_now = []

        for j in range(1, n + 1):
            if i == 0:
                human_under.append(j)
                continue
            test += human_under[j - 1]
            human_now.append(test)

    print(human_now[-1])