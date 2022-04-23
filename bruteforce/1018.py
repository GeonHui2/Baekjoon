import sys

input = sys.stdin.readline
n, m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(input().strip()))

result = []
for i in range(n - 7):    
    for j in range(m - 7):
        w = 0
        b = 0                         
        for k in range(i, i + 8):
            for l in range(j, j + 8):              
                if (l + k) % 2 == 0:
                    if board[k][l] != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if board[k][l] != 'B':
                        w += 1
                    else:
                        b += 1
        result.append(w)
        result.append(b)
        
        

print(min(result))
