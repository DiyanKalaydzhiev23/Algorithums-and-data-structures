from collections import deque


def dfs(node):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child)

    result.appendleft(node)


graph = {}
visited = set()
result = deque()

while True:
    data = input().split()

    if data[0] == "End":
        break

    if len(data) <= 2:
        graph[data[0]] = []
    else:
        graph[data[0]] = data[2:]

for node in graph:
    dfs(node)

print(' '.join(result))
