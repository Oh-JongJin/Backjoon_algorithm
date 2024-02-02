docy = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
pay = price[0]
current_pay = 0

for i in range(docy - 1):
    if pay > price[i]:
        pay = price[i]
    current_pay += pay * distance[i]

print(current_pay)
