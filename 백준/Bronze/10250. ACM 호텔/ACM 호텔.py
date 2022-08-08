T = int(input())

for x in range(T):
    hotel = []
    test = []
    H, W, N = map(int, input().split())

    for i in range(H):
        hotel.append([])
        for j in range(W):
            room_number = int(f'{i + 1}{str(j + 1).zfill(2)}')
            hotel[i].append(room_number)

    for i in range(W):
        for j in hotel:
            test.append(j[i])

    print(test[N - 1])