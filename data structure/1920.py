import sys

input = sys.stdin.readline

n = int(input())
n_data = list(map(int, input().split()))
m = int(input())
m_data = list(map(int, input().split()))

n_data.sort()

def binary(target):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if n_data[mid] == target:
            return True

        if target < n_data[mid]:
            right = mid-1
        elif target > n_data[mid]:
            left = mid + 1


for i in range(m):
    if binary(m_data[i]):
        print(1)
    else:
        print(0)
