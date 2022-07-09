n = int(input())

# My coding
# for i in range(1, n + 1):
#     space = n - i
#     print(' ' * space, end='')
#     print('*' * i)

# Other coding
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '*' * i)

# My reference coding
[print(' ' * (n - i) + '*' * i) for i in range(1, n + 1)]