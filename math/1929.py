import sys

input = sys.stdin.readline

m, n = map(int, input().split())

prime_nums = [True] * (n + 1)
prime_nums[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if prime_nums[i]:
        for j in range(i * i, n + 1, i):
            prime_nums[j] = False

for i in range(m, n + 1):
    if prime_nums[i]:
        print(i)
