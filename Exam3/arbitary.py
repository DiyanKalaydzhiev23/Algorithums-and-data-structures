from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = input().split(' ')
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, float(weight)))

target = input()
distance = {}
parent = {}
child = {}
visited = {}

for node in graph.keys():
    distance[node] = float('inf')
    parent[node] = None
    child[node] = None
    visited[node] = False

distance[target] = 1
pq = PriorityQueue()

pq.put((-1, target))

while not pq.empty():
    min_distance, node = pq.get()
    visited[node] = True
    for edge in graph[node]:
        new_distance = - (abs(min_distance) * abs(edge.weight))
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            child[node] = edge.destination
            pq.put((new_distance, edge.destination))
        if visited[edge.destination]:
            break

if distance[target] >= - 1:
    print(False)
    path = deque()
    node = target
    while True:
        path.append(node)
        node = child[node]
        if node == target:
            break
    for currency in path:
        if currency == target:
            print(f"{currency}: 1.000")
        else:
            print(f"{currency}: {abs(distance[currency]):.3f}")
else:
    print(True)
    path = deque()
    node = target
    while True:
        path.appendleft(node)

        if target == parent[node]:
            break
        node = parent[node]

    path.appendleft(target)
    print(*path, sep=' ')
