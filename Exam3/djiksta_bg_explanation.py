from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


edges = int(input())  # брой редове които четем
graph = {}  # създаваме граф като речник

for _ in range(edges):  # четем всеки ред на инпута
    source, destination, weight = [int(x) for x in
                                   input().split(', ')]  # всеки ред е от три променливи разделени от запетая
    if source not in graph:  # започваме да изграждаме графа първо за върхове
        graph[source] = []
    if destination not in graph:
        graph[destination] = []  # започваме да изграждаме графа, независимо че е дистинация пак е връх
    graph[source].append(Edge(source, destination, weight))
    # все пак като родител му добавяме детето като го създаваме като клас, защото трябва да държи информация

start = int(input())  # четем началия връх
target = int(input())  # четем крайнат адестинация

max_node = max(graph.keys())
# тук може да си позволим на видим кой е най-големия връх като число, независимо че не са последователни

distance = [float('inf')] * (max_node + 1)
# правим си 2 списъка - единия с дистанциите между като всеки инкес ще е връх, а всяка стойност ще е дистанция
parent = [None] * (max_node + 1)
# тук по същиян ачин само че стойността ще е родителя от който идва
distance[start] = 0
# винаги първата дистанция е 0, от върха от който започваме

pq = PriorityQueue()
# създаваме си приорити кю
pq.put((0, start))
# започваме да наливаме по метода на BFS като създаваме тюпъли за всеки връх, реда не се спазва затова са тюпълите
# на първо място е винаги дистанцията, а на второ място е върха
# първо разбрира се слагаме началния връх, старта

while not pq.empty():
    # по метода на БФС докато не извадим всички върхове обхождаме графа
    min_distance, node = pq.get()
    # по правило от приорити кю взимаме най-малката дистанция, но тъй като е тюпъл го разделяме на 2 променливи
    if node == target:
        # дъно на цикъла, ако върхът се окаже крайната ни цел приключваме цикъла
        break
    for edge in graph[node]:
        # ако върха не е равен на крайната цел продължаваме като намираме информация за всяко дете на горния връх
        # edge е всъщност всяка една инстанция на класа Edge от списъка
        new_distance = min_distance + edge.weight
        # правим дистанцията на принципа на Джийкстра като към текущата дистанция добавяме предходната
        # след това сравняваме дали новата дистанция е по-малка от сложената в списъка distance
        if new_distance < distance[edge.destination]:
            # edge.destination e child дестинацията - число, там където отива реброто, там запазваме данните
            # в началото е винаги inf
            distance[edge.destination] = new_distance
            # ако е по-малко то променяме данните и запазваме новата дестинация на това място
            parent[edge.destination] = node
            # също така променяме родителя с новия от който разстоянието е по-оптимално
            pq.put((new_distance, edge.destination))
            # и накрая поставяме новия връх в приорити кю-то, на първо място с дестинацията, на второ място с върха
            # реално тук може да изглежда така (1, 5),(2,5),(3,5) но ще обходим всички възможни пътища и чак когато
            # приключим с него ще го махнем, защото може в началото да е по-голям пътя, но после да се окаче по-оптимален

if distance[target] == float('inf'):
    print('There is no such path.')
else:
    print(distance[target])

    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')
