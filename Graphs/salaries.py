def dfs(node, visited):
    visited.add(node)

    if node in salaries:
        return salaries[node]

    salary = 0 if graph[node] else 1

    for child in graph[node]:
        salary += dfs(child, visited)

    return salary


n = int(input())
graph = [[] for _ in range(n)]
salaries = {}

for i in range(n):
    for idx, val in enumerate(list(input())):
        if val == "Y":
            graph[i].append(int(idx))


for i in range(n):
    salaries[i] = dfs(i, set())

print(sum(salaries.values()))
