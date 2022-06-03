import sys

text = list(sys.stdin.readline().rstrip())


flag = False # 정상 출력은 True
result = ''
stack = ''

for i in text:
    if flag == False: # <을 만나기 전
        if i == '<':
            flag = True
            stack += i
        elif i == ' ':
            stack += i
            result += stack
            stack = ''
        else:
            stack = i + stack # 역순으로 만들어준다.

    elif flag == True:
        stack += i
        if i == '>':
            flag = False
            result += stack
            stack = ''

print(result + stack)
