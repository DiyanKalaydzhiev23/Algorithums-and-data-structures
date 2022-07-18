def dfs(node):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        if child:
            dfs(int(child))
    nodes.append(node)


lines = int(input())
graph = [input().split(' ') for _ in range(lines)]
visited = set()

for n in range(len(graph)):
    if n in visited:
        continue

    nodes = []
    dfs(n)

    print(f"Connected component: {' '.join(str(n) for n in nodes)}")
