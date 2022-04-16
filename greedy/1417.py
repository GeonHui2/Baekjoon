import sys

n = int(sys.stdin.readline())
vote = []
for i in range(n):
    a = int(sys.stdin.readline())
    vote.append(a)

cnt = 0
dasom = vote.pop(0)

if len(vote) != 0:
    while dasom <= max(vote):
        vote.sort(reverse=True)
        vote[0] -= 1
        dasom += 1
        cnt += 1
    print(cnt)
else:
    print(0)

