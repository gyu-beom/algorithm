month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month, day = map(int, input().split())

# value = 0
# for i in range(month - 1):
#     if month == 1:
#         break
#     value += month_days[i]
# value = (value + day) % 7
# print(days[value])

# value = (sum(month_days[:month - 1]) + day) % 7
# print(days[value])

print(days[(sum(month_days[:month - 1]) + day) % 7])