import sys

n, fret = map(int, sys.stdin.readline().split())

cnt = 0

cal =[[] for _ in range(7)]

for _ in range(n):
    i, j = map(int, sys.stdin.readline().split())
    if not cal[i]:
        cal[i].append(j)
        cnt += 1
    else:
        while cal[i] and j < cal[i][-1]:
            cal[i].pop()
            cnt += 1
        if not cal[i] or j > cal[i][-1]:
            cal[i].append(j)
            cnt += 1     
        else:
            pass     

print(cnt)  
