import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]
    n = int(input())

    if n > 1: # 입력받은 수가 1보다 크면 
        for i in range(n - 1):
            cnt_0.append(cnt_1[-1]) # 현재의 0의 갯수는 이전의 1의 갯수
            cnt_1.append(cnt_0[-2] + cnt_1[-1]) # 현재의 1의 갯수는 이전의 0의 갯수 + 이전의 1의 갯수

    print(cnt_0[n], cnt_1[n])
