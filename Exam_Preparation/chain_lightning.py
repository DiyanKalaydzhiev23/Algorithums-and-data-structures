from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def prim(node, graph, forest):
    forest.add(node)
    pq = PriorityQueue()

    [pq.put(edge) for edge in graph[node]]

    while not pq.empty():
        min_edge = pq.get()
        tree_node, non_tree_node = -1, -1

        if min_edge.first in forest and min_edge.second not in forest:
            tree_node, non_tree_node = min_edge.first, min_edge.second
        elif min_edge.second in forest and min_edge.first not in forest:
            tree_node, non_tree_node = min_edge.second, min_edge.first

        if non_tree_node == -1:
            continue

        if non_tree_node not in houses_damage:
            houses_damage[-1][non_tree_node] = 0

        forest.add(non_tree_node)
        houses_damage[-1][non_tree_node] += houses_damage[-1][tree_node]
        [pq.put(edge) for edge in graph[non_tree_node]]


nodes = int(input())
edges = int(input())
lightnings = int(input())

graph = {n: [] for n in range(nodes)}
max_damage_for_house = {}

houses_damage = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

for _ in range(lightnings):
    node, damage = [int(x) for x in input().split()]
    forest = set()

    houses_damage.append({})

    if node not in houses_damage:
        houses_damage[-1][node] = 0

    houses_damage[-1][node] += damage

    prim(node, graph, forest)

for node in range(nodes):
    current_damage = 0

    for house in houses_damage:
        if node in house:
            current_damage += house[node]

    max_damage_for_house[node] = current_damage

print(max(max_damage_for_house.values()))
