import sys

n = int(sys.stdin.readline())

dp = [0] * 100001 # n의 최대 크기인 100,000에 0번째까지 포함한 크기의 리스트를 생성해준다.
dp[1] = 3
dp[2] = 7

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901 # i - 1 번째 값의 2배에 i - 2 번째 값을 더하면 i의 값이 나오는 규칙이다.

print(dp[n])
