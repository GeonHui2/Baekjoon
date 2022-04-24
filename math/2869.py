import math

a, b, v = map(int, input().split())

cnt = math.ceil((v-a)/(a-b)) + 1
print(cnt)
