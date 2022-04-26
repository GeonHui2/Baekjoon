import sys

input = sys.stdin.readline

n = int(input())

queue = []

for i in range(n):
    word = input().split()
    order = word[0]

    if order == 'push':
        queue.append(word[1])
    
    elif order == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif order == 'size':
        print(len(queue))
    
    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif order == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
