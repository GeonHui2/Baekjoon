import sys

input = sys.stdin.readline

length = []
l = int(input())
word = input()

for i in range(l):
    length.append(ord(word[i])- 96)

hashing = 0

for i in range(l):
    hashing += length[i] * 31 ** i

print(hashing % 1234567891)
