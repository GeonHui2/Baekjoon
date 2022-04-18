import sys

num = int(sys.stdin.readline())
ball = sys.stdin.readline().rstrip()

cnt = []

R_r = ball.rstrip('R')
cnt.append(R_r.count('R'))

B_r = ball.rstrip('B')
cnt.append(B_r.count('B'))

R_l = ball.lstrip('R')
cnt.append(R_l.count('R'))

B_l = ball.lstrip('B')
cnt.append(B_l.count('B'))

print(min(cnt))
