import math
import sys

input = sys.stdin.readline

n, brand = map(int, input().split())

strings = []
price = []

for i in range(brand):
    a, b = map(int, input().split())
    strings.append(a)
    price.append(b)

result = []
result.append((n // 6) *  min(strings) + (n % 6) * min(price))
result.append(math.ceil(n / 6) *  min(strings))
result.append(n * min(price))
print(min(result))
