import sys

input = sys.stdin.readline

s = list(input().strip())
result = set() # set을 통해서 중복된 값들을 제거해준다.

for i in range(len(s)):
    for j in range(i, len(s)):
        result.add(''.join(s[i : j + 1])) # i번째 문자부터 부분문자열을 구해서 result에 추가해준다.
        
print(len(result))
