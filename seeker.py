import random
from graph import Graph 

graph = Graph.create_graph(10)
graph = Graph.mock_distances(graph)
dist = Graph.floyd_warshall(graph)

# graph = random_distances(graph)
size = 10
for i in range(size):
    for j in range(size):
        print(dist[i][j], end=" ")
    print()
print("--------------------------")

for i in range(size):
    for j in range(size):
        print(graph[i][j], end=" ")
    print()