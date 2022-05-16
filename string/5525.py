import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

answer, i, cnt = 0, 0, 0

while i < (m - 1):
    if s[i: i + 3] == 'IOI':
        i += 2 # s[i]에서 s[i + 2]까지 'IOI'면 i의 값을 2 증가시켜 다음 'IOI'를 확인한다.
        cnt += 1 # s[i]에서 s[i + 2]까지 'IOI'면 횟수를 1회 증가시킨다.
        if cnt == n: # 증가된 횟수가 n과 같으면 Pn과 같기 때문에 answer을 1회 증가시킨다.
            answer += 1
            cnt -= 1 # 횟수를 1회 감소시켜서 다음 Pn을 찾는다.
    else:
        i += 1
        cnt = 0

print(answer)
