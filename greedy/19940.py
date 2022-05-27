import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(input().rstrip())

cnt = 0

for i in range(len(data)):
    if data[i] == "P": # 만약 사람이 나온다면
        for j in range(i - k, i + k + 1): # 사람에서 k만큼 왼쪽과 오른쪽을 확인해본다.
            if 0 <= j < n and data[j] == "H": # 만약 사람이 맨 처음에 나온다면 j가 -1이 될 수 있으므로 and 좌측조건을 추가해준다.
                cnt += 1
                data[j] = "0"
                break # 만약 맞다면 0으로 바꿔주고 for문을 빠져나간다.
print(cnt)
