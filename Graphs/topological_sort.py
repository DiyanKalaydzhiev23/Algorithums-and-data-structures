def top_sort():
    result = []
    while dependencies_by_node:
        node = find_node_without_dependencies()

        if not node:
            break

        for child in graph[node]:
            dependencies_by_node[child] -= 1

        result.append(node)
        dependencies_by_node.pop(node)

    return result


def find_node_without_dependencies():
    for node, count in dependencies_by_node.items():
        if count == 0:
            return node

    return None


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

for _ in range(int(input())):
    key, value = input().split(' ->')
    values = value.strip().split(', ') if value else []
    graph[key] = values

dependencies_by_node = find_dependencies()
sorted_notes = top_sort()

if dependencies_by_node:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_notes)}")
