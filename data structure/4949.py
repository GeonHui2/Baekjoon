import sys

input = sys.stdin.readline

def check(words):
    stack = []

    for char in words:
        if char not in '()[]':
            continue

        if char in '([':
            stack.append(char)
        elif stack and ((char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[')):
            stack.pop()
        else:
            print('no')
            return

    if not stack:
        print('yes')
    else:
        print('no')
    return


import sys

words = sys.stdin.readline().rstrip()

while words != '.':
    check(words)
    words = sys.stdin.readline().rstrip()
