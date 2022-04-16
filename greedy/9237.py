import sys
num = int(input())
time = list(map(int,sys.stdin.readline().split()))

sum = []

time.sort(reverse=True)

for i in range(num):
    sum.append((i + 1) + time[i])

print(max(sum) + 1)
