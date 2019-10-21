import random
from graph import Graph 

size = 5

file = open("inputGraph.txt", "r")
# contents = file.read()
# print(contents)
file_size = 0
lines = file.readlines()
for line in lines:
    print(line, end="")
    file_size += 1
file.close

path = Graph.create_path_matrix(size)
graph = Graph.create_graph(size)
graph,y = Graph.mock_distances(graph, path)
dist,x = Graph.floyd_warshall(graph, path)
# graph = random_distances(graph)

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