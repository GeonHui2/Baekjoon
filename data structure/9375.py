import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    data = []

    for _ in range(n):
        a, b = input().split()
        data.append(b)
        
    cnt = 1
    result = Counter(data)
    
    for i in result:
        cnt *= result[i] + 1

    print(cnt - 1)
