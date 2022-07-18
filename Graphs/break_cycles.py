def dfs(node, visited, destination):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, visited, destination)

    if destination in visited:
        return True


n = int(input())
graph = {}
edges = []
removed = []

for _ in range(n):
    key, values = input().split(' -> ')
    graph[key] = sorted(values.split())
    for child in values:
        edges.append([key, child])


for key, value in sorted(edges, key=lambda x: [x[0], x[1]]):
    if value not in graph[key] or key not in graph[value]:
        continue

    graph[key].remove(value)
    graph[value].remove(key)

    if dfs(key, set(), value):
        removed.append(f"{key} - {value}")
    else:
        graph[key].append(value)
        graph[value].append(key)

print(f"Edges to remove: {len(removed)}")
[print(edge) for edge in removed]
