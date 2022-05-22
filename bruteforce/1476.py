import sys

input = sys.stdin.readline

def day():
    e, s, m = map(int, input().split())
    earth, sun, moon, cnt = 0, 0, 0, 0
    
    while True:
        earth += 1
        sun += 1
        moon += 1
        
        if earth > 15:
            earth = 1
        if sun > 28:
            sun = 1
        if moon > 19:
            moon = 1

        cnt += 1
        if e == earth and s == sun and m == moon:
            print(cnt)
            break

day()
