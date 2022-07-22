def dfs(node):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child)


graph = []
edges = []
important_streets = []

[graph.append([]) for _ in range(int(input()))]

for _ in range(int(input())):
    first, second = [int(x) for x in input().split(" - ")]
    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(first, second)))

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * len(graph)

    dfs(0)

    if not all(visited):
        important_streets.append((first, second))

    graph[first].append(second)
    graph[second].append(first)

print("Important streets:")
[print(f"{f} {s}") for f, s in important_streets]
