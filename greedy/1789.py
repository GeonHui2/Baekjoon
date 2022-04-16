s = int(input())

cnt = 0
i = 1

while s >= 0:
    s -= i
    i +=1
    cnt += 1
    
    if s <0:
        print(cnt - 1)
