import sys

input = sys.stdin.readline

a = input().split('-')

num = []

for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)

result = num[0]

for i in range(1, len(num)):
    result -= num[i]

print(result)
