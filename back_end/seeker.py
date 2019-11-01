import random
from graph import Graph 

size = 5
with open("inputGraph.txt" , "r") as file:
    lines = file.readlines()
file.close()

gr = Graph.lines_to_graph_matrix(lines)
path = Graph.create_path_matrix(size)
graph = Graph.create_graph(size)
graph,y = Graph.mock_distances(graph, path)
dist,x = Graph.floyd_warshall(Graph, graph, path)
objetct_graph = Graph.matrix_to_object(graph, True)