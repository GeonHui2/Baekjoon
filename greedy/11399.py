import sys

input = sys.stdin.readline

num = int(input()) #사람의 수
time = list(map(int, input().split())) # 각 사람이 인출하는데 필요한 시간

time.sort() # 필요한 시간 리스트 정렬

for i in range(1, num):
    time[i] += time[i - 1] # 앞 사람이 걸리는 시간에 자신이 인출하는데 걸리는 시간 더하기

print(sum(time)) # 각 사람이 걸리는 시간 더하기
