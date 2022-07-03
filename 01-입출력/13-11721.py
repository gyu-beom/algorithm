# value = input()
# for i in range(0, len(value), 10):
#     print(value[i:i+10])

value = input()
[print(value[i:i+10]) for i in range(0, len(value), 10)]