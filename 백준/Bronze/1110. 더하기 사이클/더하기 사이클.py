N = int(input())
if N < 10:
    test = [0, int(str(N)[0]), int(str(N)[0])]
else:
    test = [int(str(N)[0]), int(str(N)[1]), (int(str(N)[0]) + int(str(N)[1]))]
new_N = N
cycle = 0

while True:
    test = [test[1], test[2], int(str(test[1] + test[2])[-1])]

    cycle += 1
    if int(str(test[0]) + str(test[1])) == N:
        print(cycle)
        break
