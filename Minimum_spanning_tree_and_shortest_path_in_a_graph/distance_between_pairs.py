from collections import deque


nodes = int(input())
directions = int(input())

graph = {}

for _ in range(nodes):
    node_str, children_str = input().split(":")
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[int(node_str)] = children

for _ in range(directions):
    source, destination = [int(x) for x in input().split("-")]

    visited = {source}
    parent = {source: None}

    queue = deque([source])

    while queue:
        node = queue.popleft()

        if node == destination:
            break

        for child in graph[node]:
            if child in visited:
                continue

            visited.add(child)
            queue.append(child)
            parent[child] = node

    if destination not in parent:
        print(f"{{{source}, {destination}}} -> -1")
        continue

    path = deque()
    node = destination

    while node:
        path.appendleft(node)
        node = parent[node]

    print(f"{{{source}, {destination}}} -> {len(path) - 1}")
