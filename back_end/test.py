from math import inf
from graph import Graph

with open("inputGraph.txt", "r") as file:
    fileLines = file.readlines()
    lines = []
    for i in fileLines:
        lines.append(i.split())
    file.close()

    size = len(lines[0])
    path = []
    for i in range(size):
        path.append([])
        for j in range(size):
            if i == j:
                path[i].append(0)
            else:
                path[i].append(None)
    # print(path)
    graph = Graph.graph_from_file(Graph, "inputGraph.txt")
    for i in range(size):
        for j, element in enumerate(lines[i]):
            if element != 'inf' and i != j:
                path[i][j] = [j]
    warshall_graph, warshall_path = Graph.floyd_warshall(Graph,graph, path)