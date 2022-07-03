# test_case = int(input())
# value = list(map(int, input().split()))
# print(min(value), max(value), sep=' ')

test_case = int(input())
*value, = map(int, input().split())
print(min(value), max(value))