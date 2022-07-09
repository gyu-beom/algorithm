n = int(input())
[print(' ' * (n - i) + '*' * (2 * i - 1)) for i in range(1, n + 1)]