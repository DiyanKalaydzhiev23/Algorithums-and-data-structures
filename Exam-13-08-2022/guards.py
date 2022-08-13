from collections import deque


def dfs(node):
    if node in visited:
        return

    visited.add(node)

    if node not in graph:
        result.appendleft(node)
        return

    for child in graph[node]:
        dfs(child)

    result.appendleft(node)


nodes = int(input())
edges = int(input())

graph = {}
visited = set()
result = deque()
not_visited = set()

for _ in range(edges):
    node, destination = input().split()

    if node not in graph:
        graph[node] = []

    graph[node].append(destination)

dfs(input())

for node in graph:
    if node not in result:
        not_visited.add(node)

    for child in graph[node]:
        if child not in result:
            not_visited.add(child)

print(*sorted(int(x) for x in not_visited), sep=' ')
