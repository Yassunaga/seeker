import random
from graph import Graph 

size = 5

file = open("inputGraph.txt", "r")
lines = file.readlines()
gr = Graph.lines_to_graph_matrix(lines)
print(gr)
file.close()
path = Graph.create_path_matrix(size)
graph = Graph.create_graph(size)
graph,y = Graph.mock_distances(graph, path)
dist,x = Graph.floyd_warshall(graph, path)
# graph = random_distances(graph)
objetct_graph = Graph.matrix_to_object(graph)

print(objetct_graph)

for i in range(size):
    for j in range(size):
        print(path[i][j], end=" ")
    print()
print("--------------------------")
for i in range(size):
    for j in range(size):
        print(graph[i][j], end=" ")
    print()

print("--------------------------")

for i in range(size):
    for j in range(size):
        print(dist[i][j], end=" ")
    print()