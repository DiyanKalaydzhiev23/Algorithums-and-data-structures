from collections import deque


def dfs(node):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child)

    result.appendleft(node)


nodes, edges = int(input()), int(input())

graph = {}

for _ in range(edges):
    first, second = [int(x) for x in input().split()]

    if first not in graph:
        graph[first] = []

    if second not in graph:
        graph[second] = []

    graph[first].append(second)
    graph[second].append(first)

start_node = int(input())
visited = set()
not_visited = set()
result = deque()

dfs(start_node)

for n in graph:
    if n not in result:
        not_visited.add(n)

print(*sorted(not_visited), sep=' ')
