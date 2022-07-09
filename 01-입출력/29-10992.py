n = int(input())

# Other code
# for i in range(1, n + 1):
#     if i == 1:
#         print(' ' * (n - 1) + '*')
#     elif 1 < i < n:
#         print(' ' * (n - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*')
#     else:
#         print('*' * (2 * n - 1))

# Other code
# for i in range(1, n + 1):
#     if (i == 1 or i == n):
#         print(' ' * (n - i) + '*' * (2 * i - 1))
#     else:
#         print(' ' * (n - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*')

# My reference code
[print(' ' * (n - i) + '*' * (2 * i -1)) if (i == 1 or i == n) else print(' ' * (n - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*') for i in range(1, n + 1)]