import sys

r, g, b = map(int, sys.stdin.readline().split())

min_value = min(r, g, b)

cnt = 0
cnt += min_value

r -= min_value
g -= min_value
b -= min_value

cnt += r // 3 + g // 3 + b // 3

r %= 3
g %= 3
b %= 3

if r == 2:
    cnt += 1
    r = 0
if g == 2:
    cnt += 1
    g = 0
if b == 2:
    cnt += 1
    b = 0
if r + g + b > 0:
    cnt += 1
print(cnt)
