import sys

input = sys.stdin.readline

n, m = map(int, input().split())

heard = set()
seen = set()

for _ in range(n):
    heard.add(input().strip())

for _ in range(m):
    seen.add(input().strip())

result = sorted(list(heard & seen))

print(len(result))

for i in result:
    print(i)
