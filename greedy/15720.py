import sys

b, c, d = map(int, sys.stdin.readline().split())

burger = list(map(int, sys.stdin.readline().split()))
side = list(map(int, sys.stdin.readline().split()))
drink = list(map(int, sys.stdin.readline().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

result = 0
min_price = min(b, c, d)
for i in range(min_price):
    result += (burger[i] + side[i] + drink[i]) * 0.9

result += sum(burger[min_price::]) + sum(side[min_price::]) + sum(drink[min_price::])
print(sum(burger) + sum(side) + sum(drink))
print(int(result))
