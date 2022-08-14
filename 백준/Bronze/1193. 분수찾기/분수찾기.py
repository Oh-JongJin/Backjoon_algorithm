x = int(input())

line_number = 0
count = 0
data_list = []

while line_number < x:
    count += 1
    line_number += count

data = x - line_number

if count % 2 == 0:
    for i in range(count):
        data_list.append(f'{i + 1}/{count - i}')

else:
    for i in range(count):
        data_list.append(f'{count - i}/{i + 1}')

print(data_list[data - 1])