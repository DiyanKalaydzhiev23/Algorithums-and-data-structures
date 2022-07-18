def find_node_without_dependencies():
    for node, count in dependencies_by_node.items():
        if count == 0:
            return "Yes"

    return "No"


def find_dependencies():
    result = {}

    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    return result


graph = {}

while True:
    data = input().split('-')

    if len(data) == 1:
        break

    graph[data[0]] = data[1]

dependencies_by_node = find_dependencies()
print(f"Acyclic: {find_node_without_dependencies()}")
