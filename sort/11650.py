import sys

input = sys.stdin.readline

n = int(input())

coordinate = []

for i in range(n):
    x, y = map(int, input().split())
    coordinate.append((x, y))

coordinate = sorted(coordinate, key = lambda x: x[1])
coordinate = sorted(coordinate, key = lambda x: x[0])

for i in coordinate:
    print(i[0], i[1])
