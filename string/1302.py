import sys

input = sys.stdin.readline

n = int(input())
books = {}

for _ in range(n):
    book = input().strip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

books = dict(sorted(books.items()))

print(max(books,key=books.get))
