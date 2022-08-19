from collections import deque


class Edge:
    def __init__(self, source, destination, price):
        self.source = source
        self.destination = destination
        self.price = price


def get_graph(edges):
    graph = []
    nodes = set()

    for _ in range(edges):
        source, destination, price = input().split()
        price = float(price)
        graph.append(Edge(source, destination, price))
        nodes.add(source)
        nodes.add(destination)

    return graph, nodes


def bellman_ford(nodes, start, graph):
    parents = {n: None for n in nodes}
    currencies = {n: -float('inf') for n in nodes}
    currencies[start] = 1
    cyclical = False
    last_node = start

    for _ in range(len(nodes)):
        updated = False

        for edge in graph:
            if currencies[edge.source] == float('inf'):
                continue

            new_price = currencies[edge.source] * edge.price
            if new_price > currencies[edge.destination]:
                currencies[edge.destination] = new_price
                parents[edge.destination] = edge.source
                last_node = edge.destination
                updated = True

        if not updated:
            break

    for edge in graph:
        new_price = currencies[edge.source] * edge.price
        if new_price > currencies[edge.destination]:
            cyclical = True
            break

    return parents, last_node, currencies, cyclical


def get_path(target, node, parents):
    path = deque()

    while node is not None:
        path.appendleft(node)
        node = parents[node]

        if node == target:
            path.appendleft(node)
            break

    return path


edges = int(input())
graph, nodes = get_graph(edges)
target = input()
parents, last_node, currencies, cyclical = bellman_ford(nodes, target, graph)
path = get_path(target, last_node, parents)
result = [str(cyclical)]

if cyclical:
    result.append(' '.join(path))
else:
    for node in nodes:
        if currencies[node] == -float('inf'):
            currencies[node] = 1

        result.append(f'{node}: {currencies[node]:.3f}')

print('\n'.join(result))
