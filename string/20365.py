import sys

n = int(sys.stdin.readline())
word = list(sys.stdin.readline())
cnt_b = 0 # 파란색 그룹 갯수
cnt_r = 0 # 빨간색 그룹 갯수

color = word[0]
if color == 'B':
    cnt_b += 1 # 첫 번째 색이 파란색이면 파란색 그룹 갯수 + 1
else:
    cnt_r += 1 # 첫 번째 색이 빨간색이면 빨간색 그룹 갯수 + 1

for i in range(1, n):
    if color != word[i]: # color와 현재 색상이 다르면
        if word[i] == 'B': # 현재 색상이 파란색이면 파란색 그룹 갯수 + 1
            cnt_b += 1
        else:
            cnt_r += 1 # 현재 색상이 빨간색이면 빨간색 그룹 갯수 + 1
        color = word[i] # color를 현재 색상으로 변경

print(min(cnt_b, cnt_r) + 1) # 파란색 그룹과 빨간색 그룹의 갯수 중 가장 작은 것에 + 1을 하고 출력한다.
