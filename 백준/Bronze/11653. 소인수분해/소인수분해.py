from math import sqrt
N = int(input())
divide = 2

while divide <= sqrt(N):
    if N % divide == 0:
        print(divide)
        N = N // divide
    else:
        divide += 1

if N > 1:
    print(N)