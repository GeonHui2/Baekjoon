import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
square = [i * i for i in range(1, 317)] # 제곱수를 미리 계산해서 리스트로 만들어준다.

for i in range(1, n + 1):
    s = [] # 결과를 저장할 리스트를 만들어준다.
    for j in square:
        if j > i: # 제곱수가 i보다 크면 for문을 멈춰준다.
            break
        s.append(dp[i - j]) # i와 제곱수를 뺀 값을 구하고 dp에 저장되어 있는 값을 결과 리스트에 저장해준다.

    dp[i] = min(s) + 1 # 결과 리스트에서 최소값을 구하고 1을 더해준다.

print(dp[n])
