import sys

word = str(sys.stdin.readline().rstrip("\n"))

word = word.replace("pi", " ")
word = word.replace("ka", " ")
word = word.replace("chu", " ")

if len(word.strip()) == 0:
    print("YES")
else:
    print("NO")
