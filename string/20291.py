import sys

input = sys.stdin.readline

n = int(input())
file = {} # 파일들을 저장할 딕셔너리를 생성한다.

for _ in range(n):
    filename = input().strip().split('.')[1] # 파일의 이름에서 확장자만 저장한다.
    if file.get(filename):
        file[filename] += 1 # 파일에 파일의 이름이 있다면 갯수를 1 증가시킨다.
    else:
        file[filename] = 1 # 파일에 파일의 이름이 없다면 갯수를 1개로 설정한다.

tmp = [] # 출력을 위한 결과값을 저장할 리스트를 생성한다.

for k in sorted(file):
    tmp.append(str(f'{k} {file[k]}')) # 문자열 포매팅을 사용하여 파일의 이름과 갯수를 리스트에 저장한다.

print('\n'.join(tmp)) # join을 사용하여 결과 리스트를 출력시킨다.
