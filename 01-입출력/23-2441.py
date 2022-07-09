n = int(input())
[print(' ' * (n - i) + '*' * i) for i in range(n, 0, -1)]