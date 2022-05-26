import sys

input = sys.stdin.readline

n, l = map(int, input().split())

hole = list(map(int, input().split()))

hole.sort() # 가장 왼쪽에서 물이 떨어지기 때문에 정렬을 시켜준다.
cnt = 0 # 테이프의 개수
tape = 0 # 마지막 테이프의 위치

for i in hole:
    if tape < i: # 마지막 테이프의 위치가 구멍의 위치보다 왼쪽에 있다면
        tape = i + l - 0.5 # 마지막 테이프의 위치는 구멍의 위치에 테이프의 길이를 더하고 간격인 0.5를 빼준다.
        cnt += 1 # 테이프의 개수를 증가시킨다.

print(cnt)
