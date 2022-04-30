import sys

input = sys.stdin.readline

t = int(input())
data = []
for i in range(t):
    data.append(list(input().strip()))

for i in data:
    cnt = 0
    for j in i:
        if cnt >= 0:
            if j == '(':
                cnt += 1
            else:
                cnt -= 1
        else:
            break
    if cnt == 0:
        print('YES')
    else:
        print('NO')
