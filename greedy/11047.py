import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
cnt = 0
for _ in range(n):
    coin.append(int(input()))

coin.reverse() #coin을 역순으로 만들어준다.

for i in coin:
    cnt += k // i  #총 금액에서 동전의 가치를 나눈 몫을 동전 개수에 더해준다.
    k %= i  #총 금액에서 동전의 가치를 나눈 나머지를 총 금액으로 바꿔준다.

print(cnt)
