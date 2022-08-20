day_count = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
calender_month = []
calender_day = []
calender = {}

x, y = map(int, input().split())

for month in range(1, 13):
    for day in range(1, 32):
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30:
                continue
            calender_month.append(f'{month}/{day}')
        else:
            if month == 2:
                if day > 28:
                    continue
                calender_month.append(f'{month}/{day}')
                continue
            calender_month.append(f'{month}/{day}')

for i in range(len(calender_month)):
    calender_day.append(day_count[i % 7])

for key in calender_month:
    for value in calender_day:
        calender[key] = value
        calender_day.remove(value)
        break

print(calender[f'{x}/{y}'])