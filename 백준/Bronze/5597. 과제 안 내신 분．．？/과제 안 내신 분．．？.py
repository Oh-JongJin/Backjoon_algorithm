st_list = []

for i in range(28):
    st_list.append(int(input()))

for i in range(1, 31):
    if i not in st_list:
        print(i)
