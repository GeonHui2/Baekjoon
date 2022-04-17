import sys

n = int(sys.stdin.readline())

cnt = 0
order = []
for _ in range(n):
    order.append(int(sys.stdin.readline()))

find_book = n
for i in range(n - 1, -1, -1):
    if order[i] != find_book:
        cnt += 1
    else:
        find_book -= 1

print(cnt)
