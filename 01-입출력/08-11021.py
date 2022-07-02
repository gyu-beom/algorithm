test_case = int(input())
for idx in range(test_case):
    x, y = map(int, input().split())
    print(f'Case #{idx + 1}: {x + y}')