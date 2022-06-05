import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10): # n = 1 일 때 0을 제외하고 경우의 수가 1개로 초기화 해준다.
    dp[1][i] = 1

for i in range(2, n +1):
    for j in range(10):
        if j == 0: # 0 일 때는 앞에 1만 올 수 있다.
            dp[i][j] = dp[i - 1][1]
        elif j == 9: # 9일 때는 앞에 8만 올 수 있다.
            dp[i][j] = dp[i - 1][8]
        else: # 2 ~ 8은 앞에 숫자가 2개 올 수 있다.
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)
