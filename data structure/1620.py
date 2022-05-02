import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokemon_num = {} #포켓몬 번호
pokemon_name = {} #포켓몬 이름

num = 1
for _ in range(n):
    name = input().strip()
    pokemon_num[name] = num
    pokemon_name[num] = name
    num += 1

for _ in range(m):
    quest = input().strip()

    try:
        print(pokemon_name[int(quest)])
    except:
        print(pokemon_num[quest])
