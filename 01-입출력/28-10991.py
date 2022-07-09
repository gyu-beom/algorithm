n = int(input())

# Other code
# for i in range(1, n + 1):
#     print(' ' * (n - i), end='')
#     for j in range(i):
#         print('*', end=' ')
#     print()

# Other code
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '* ' * (i - 1) + '*')

# My reference code
[print(' ' * (n - i) + '* ' * (i - 1) + '*') for i in range(1, n + 1)]