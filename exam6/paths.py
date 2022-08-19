def dfs(node, path):
    if node in visited:
        return

    path = path + [node]

    if node == nodes - 1:
        print(*path, sep=' ')
        return

    for child in graph[node]:
        dfs(child, path)


nodes = int(input())
graph = [[] for node in range(nodes)]

for n in range(nodes - 1):
    children = [int(x) for x in input().split()]
    graph[n] = children

for n in range(nodes - 1):
    visited = set()
    dfs(n, [])
