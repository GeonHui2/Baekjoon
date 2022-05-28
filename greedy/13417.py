import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    t = int(input())
    data = list(input().split())
    result = [data[0]]
    
    for i in range(1, t):
        if result[0] >= data[i]:
            result.insert(0, data[i])
        else:
            result.append(data[i])

    print(''.join(result))
