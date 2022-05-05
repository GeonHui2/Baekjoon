import sys

input = sys.stdin.readline

num = int(input()) # 컴퓨터의 수
line = int(input()) # 연결된 컴퓨터 쌍의 수

graph = [[] for _ in range(num + 1)]
for _ in range(line):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (num + 1) #방문처리

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
    return True

dfs(graph, 1, visited)
print(sum(visited) - 1) #방문한 컴퓨터 개수 - 1번 컴퓨터
