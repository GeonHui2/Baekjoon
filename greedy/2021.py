import sys

input = sys.stdin.readline

n = int(input())
rank = []
dissatisfaction = 0 # 불만도

for _ in range(n):
    rank.append(int(input()))

rank.sort() # 예상 등수를 정렬시켜준다.

for i in range(n):
    dissatisfaction += abs(rank[i] - i - 1) # 예상 등수와 실제 등수를 빼고 1을 뺀 후 불만도에 더해준다.
     

print(dissatisfaction) # 불만도를 출력한다.
