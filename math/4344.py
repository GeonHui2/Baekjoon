import sys

c = int(sys.stdin.readline())

for _ in range(c):
    num = list(map(int, sys.stdin.readline().split()))
    n = num.pop(0)

    ave = sum(num) / n
    cnt = 0

    for i in num:
        if i > ave:
            cnt += 1

    print("{:.3f}%".format(cnt * 100 / n))
