import sys

n, k = map(int, sys.stdin.readline().split())

basket = k * (k + 1) / 2

if n < basket:
    print(-1)
else:
    if (n - basket) % k == 0:
        print(k - 1)
    else:
        print(k)
