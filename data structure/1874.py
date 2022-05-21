import sys

input = sys.stdin.readline

n = int(input())

stack = []
result = []
cnt = 1
temp = True

for i in range(n):
    num = int(input())
    
    while cnt <= num: # cnt == num이 될 때 까지 push한다.
        stack.append(cnt)
        result.append('+')
        cnt += 1
        
    if stack[-1] == num: #stack에서 top이 num과 같으면 pop시켜준다.
        stack.pop()
        result.append('-')
    else: #stack의 top이 num과 같지 않으면 temp를 False로 해주고 break시킨다.
        temp = False
        break

if temp == False: #temp가 False이면 스택을 만들 수 없기때문에 NO를 출력시킨다.
    print('NO')
else: #temp가 True이면 주어진 스택을 만들었기 때문에 result를 순서대로 출력시킨다.
    for i in result:
        print(i)
