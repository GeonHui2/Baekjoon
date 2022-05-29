import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    profit = 0
    mx = stock[-1] # 리스트의 가장 마지막 인덱스를 최대 가격으로 설정한다.

    for i in range(n - 2, -1, -1): # for문을 뒤에서부터 시작해준다.
        if stock[i] > mx: # 오늘 가격이 최대 가격보다 비싸면
            mx = stock[i] # 최대 가격을 오늘 가격으로 변경해준다.
        else:
            profit += mx - stock[i] # 그렇지 않으면 최대 가격에서 지금 가격을 빼서 이익에 더해준다.

    print(profit)
