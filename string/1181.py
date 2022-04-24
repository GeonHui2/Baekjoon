import sys

input = sys.stdin.readline

n = int(input())
word = []
for i in range(n):
    word.append(input().strip())

word = list(set(word))
word = sorted(word)
word.sort(key = len)


for i in range(len(word)):
    print(word[i])
