import sys

input = sys.stdin.readline

m = int(input())
s = set()

for i in range(m):
    word = input().strip().split()

    if len(word) == 1:
        if word[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue

    order, value = word[0], word[1]
    value = int(value)

    if order == 'add':
        s.add(value)
    elif order == 'check':
        print(1 if value in s else 0)
    elif order == 'remove':
        s.discard(value)
    elif order == 'toggle':
        if value in s:
            s.discard(value)
        else:
            s.add(value)
