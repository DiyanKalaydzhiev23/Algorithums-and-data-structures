from collections import deque


def dfs(node, target_node):
    if node in visited:
        return

    if node == target_node:
        result.appendleft(node)
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, target_node)

    result.appendleft(node)


nodes, edges = int(input()), int(input())
visited = set()
not_visited = deque()
result = deque()
graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    first, second = [int(x) for x in input().split()]

    if first not in graph:
        graph[first] = []

    graph[first].append(second)

dfs(int(input()), int(input()))

for n in range(1, nodes + 1):
    if n not in result:
        not_visited.append(n)

print(*result, sep=" ")

if not_visited:
    print(*not_visited, sep=" ")
else:
    print()
