import sys

input = sys.stdin.readline

num = int(input())
stair = [0]

for _ in range(num):
    stair.append(int(input()))

if num == 1:
    print(stair[1])
else:
    dp = [0] * (num + 1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, num + 1):
        dp[i] = max(dp[i - 3] +stair[i - 1] + stair[i], dp[i - 2] + stair[i])
        # 자신의 위치 점수 + 1 칸 밑의 점수 + 3 칸 밑 까지 올라오는 최대 점수(DP)와 자신의 위치 점수 + 2 칸 밑의 점수 중 더 큰 값을 비교하여 dp 리스트에 저장한다.

    print(dp[num])
