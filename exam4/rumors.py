from collections import deque

nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]

    graph[source].append(destination)
    graph[destination].append(source)

start_node = int(input())

for destination_node in range(1, nodes + 1):
    if start_node == destination_node:
        continue

    visited = [False] * (nodes + 1)
    parent = [None] * (nodes + 1)

    visited[start_node] = True
    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        if node == destination_node:
            break

        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue.append(child)
            parent[child] = node

    path = deque([])
    node = destination_node
    while node:
        path.appendleft(node)
        node = parent[node]

    if len(path) - 1 > 0:
        print(f"{start_node} -> {destination_node} ({len(path) - 1})")
