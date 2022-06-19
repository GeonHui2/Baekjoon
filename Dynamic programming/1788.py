import sys

n = int(sys.stdin.readline())

dp = [0, 1]

for i in range(2, abs(n) + 1):
    dp.append((dp[i - 1] + dp[i - 2]) % 1000000000)

if n == 0:
    print(0)
    print(dp[n])
elif n > 0:
    print(1)
    print(dp[n])
else:
    if n % 2 == 0:
        print(-1)
        print(dp[abs(n)])
    else:
        print(1)
        print(dp[abs(n)])
