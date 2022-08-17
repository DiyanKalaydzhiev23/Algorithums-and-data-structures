def find_path(route):
    node = route.pop(0)

    if not route:
        return "yes"

    if route[0] in graph[node]:
        return find_path(route)

    return "no"


nodes = int(input())
graph = []

for _ in range(nodes):
    children = input()

    if children:
        graph.append([int(c) for c in children.split()])
    else:
        graph.append([])

paths = int(input())

for _ in range(paths):
    print(find_path([int(x) for x in input().split()]))
