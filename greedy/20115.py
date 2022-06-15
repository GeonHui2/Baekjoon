import sys

n = int(sys.stdin.readline())
drink = list(map(int, sys.stdin.readline().split()))

result = max(drink)
drink.remove(result)
result += sum(drink) / 2

print(result)
