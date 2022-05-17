import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    first = input()
    second = input()
    data = [] #다른 단어를 넣어줄 리스트 생성
    for i in range(n):
        if first[i] != second[i]:
            data.append(first[i]) # i번째 단어가 다르면 data에 추가한다.

    b_cnt = data.count('B') #data에서 B의 개수
    w_cnt = data.count('W') #data에서 W의 개수
    print(max(w_cnt, b_cnt)) #data에서 B와 W의 개수를 비교해서 큰 수를 출력
