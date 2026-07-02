from collections import deque

# 그래프(인접 리스트)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

# DFS (재귀)
def dfs(v, visited):
    visited.add(v)
    print(v, end=' ')

    for node in graph[v]:
        if node not in visited:
            dfs(node, visited)

# BFS (큐)
def bfs(start):
    visited = set([start])
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for node in graph[v]:
            if node not in visited:
                visited.add(node)
                queue.append(node)

print("DFS 결과")
dfs(1, set())

print("\n")

print("BFS 결과")
bfs(1)