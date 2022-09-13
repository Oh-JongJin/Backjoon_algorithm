import sys

N = int(sys.stdin.readline())
data = []

for i in range(0, N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        data.append(int(command[1]))
    elif command[0] == 'top':
        if len(data) != 0:
            print(data[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(data))
    elif command[0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'pop':
        if len(data) == 0:
            print(-1)
        else:
            print(data[-1])
            del data[-1]
