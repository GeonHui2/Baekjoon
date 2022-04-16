import sys

num, lenght = map(int,sys.stdin.readline().split())
h = list(map(int,sys.stdin.readline().split()))

h.sort()

for i in range(num):
    if lenght >= h[i]:
        lenght += 1


print(lenght)
