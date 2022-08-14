from collections import deque


def dfs(node, target):
    if node in visited:
        return

    if node == target:
        result.appendleft(node)
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, target)

    result.appendleft(node)


nodes, edges = int(input()), int(input())

graph = [[] for _ in range(nodes + 1)]
visited = set()
result = deque()

for _ in range(edges):
    first, second = [int(x) for x in input().split()]
    graph[first].append(second)

dfs(int(input()), int(input()))

print(*result, sep=' ')
