import sys

d = {}

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    a = sys.stdin.readline().rstrip()

    d[a] = [i,0]

for i in range(n):
    b = sys.stdin.readline().rstrip()
    d[b][1] = i

g = list(d.values())
g.sort()

answer = 0
i = 0

for k in g:
    if k[1] > i:
        answer += k[1] - i
        i = k[1] + 1
    elif k[1] == i:
        i += 1

print(answer)
