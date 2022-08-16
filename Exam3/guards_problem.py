from collections import deque


def dfs(node):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child)

    result.appendleft(node)


nodes, edges = int(input()), int(input())
graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    first, second = [int(x) for x in input().split()]

    graph[first].append(second)

start_node = int(input())
visited = set()
not_visited = deque()
result = deque()

dfs(start_node)

for n in range(1, nodes + 1):
    if n not in result:
        not_visited.append(n)

print(*sorted(not_visited), sep=' ')
