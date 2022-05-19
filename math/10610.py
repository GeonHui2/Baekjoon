import sys

input = sys.stdin.readline

n = list(input().strip())
n.sort(reverse=True) # list로 입력 받은 n을 내림차순으로 정렬한다.
result = 0

for i in n:
    result += int(i) # n의 각 인덱스의 합을 구한다.

if result % 3 == 0 and '0' in n: # 3으로 나눌 때 나머지가 0이고 일의 자리 수가 0이어야 하는 30의 배수가 되는 조건을 확인한다.
    print(''.join(n)) # 30의 배수이면 n을 join을 사용하여 출력한다.
else:
    print(-1) # 30의 배수가 아니라면  -1을 출력한다.
