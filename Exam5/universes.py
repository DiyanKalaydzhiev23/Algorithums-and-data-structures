def dfs(node):
    if node in visited:
        return 0

    visited.add(node)

    if graph[node] in graph:
        return dfs(graph[node])

    return 1


n = int(input())
graph = {}
visited = set()
universes = 0

for _ in range(n):
    first, second = input().split(' - ')
    graph[first] = second

for node in graph:
    universes += dfs(node)

print(universes)
