import sys

input = sys.stdin.readline

trees = {} # 딕셔너리 생성한다.
cnt = 0 # 횟수를 저장할 변수를 생성한다.

while True:
    tree = input().rstrip()
    if not tree: # 입력값이 공백이면 break한다.
        break

    if tree in trees: 
        trees[tree] += 1 # 딕셔너리에 입력값이 있다면 횟수를 1회 증가시킨다.

    else:
        trees[tree] = 1 # 딕셔너리에 입력값이 없다면 추가해준다.
    cnt += 1

tree_list = list(trees.keys()) # 딕셔너리의 키 값을 리스트로 만들어준다.
tree_list.sort() # 리스트를 정렬시켜준다.

for tree in tree_list:
    print('%s %.4f' %(tree, trees[tree] / cnt * 100)) # 백분율을 사용하여 출력시킨다.
