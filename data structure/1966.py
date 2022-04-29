import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    n, m = map(int, input().split())
    print_queue = list(map(int, input().split()))
    index = [i for i in range(n)]
    target = index[m]
    cnt = 0

    while print_queue:
        if print_queue[0] == max(print_queue):
            cnt += 1
            if index[0] == target:
                print(cnt)
                break
            print_queue.pop(0)
            index.pop(0)
        else:
            print_queue.append(print_queue.pop(0))
            index.append(index.pop(0))
