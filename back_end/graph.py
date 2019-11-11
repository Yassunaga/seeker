from math import inf
from flask import g

class Graph:
    def __init__(self, size = None):
        self.graph = []
        if size is None:
            size = 10
        for i in range(size):
            self.graph.append([])
            for j in range(size):
                self.graph[i].append(0)

    def matrix_to_object(matrix_graph, remove_infinite):
        size = len(matrix_graph[0])
        graph = {
            "size": size,
            "arcList" : []
        }
        for i in range(size):
            for j in range(size):
                arco = {
                    "begin" : i,
                    "end" : j,
                    "weight" : matrix_graph[i][j]
                }
                if arco["weight"] == inf and remove_infinite == True:
                    continue
                graph["arcList"].append(arco)
        return graph

    def matrix_to_list(matrix_graph, remove_infinite):
        size = len(matrix_graph[0])
        graph_list = {}
        for i in range(size):
            graph_list[i] = []
        for i in range(size):
            for j in range(size):
                if remove_infinite == True and matrix_graph[i][j] == inf:
                    continue
                elif matrix_graph[i][j] > 0:
                    graph_list[i].append(j)
                    graph_list[j].append(i)
        return graph_list

    # Create a graph NxN according to size
    def create_graph(size):
        graph = []
        for i in range(size):
            graph.append([])
            for j in range(size):
                if i == j:
                    graph[i].append(0)
                else:
                    graph[i].append(inf)
        return graph
        
    def create_path_matrix(size):
        path = []
        for i in range(size):
            path.append([])
            for j in range(size):
                if i == j:
                    path[i].append(0)
                path[i].append(None)
        return path

    def random_distances(graph_matrix):
        size = len(graph_matrix)
        for i in range(size):
            for j in range(size):
                if graph_matrix[i][j] == 1:
                    random_distance = random.randint(1,20)
                    graph_matrix[i][j] = random_distance
                    graph_matrix[j][i] = random_distance
        return graph_matrix

    def floyd_warshall(self,graph_matrix,path_matrix):
        dist = []
        size = len(graph_matrix)
        # Inicializa a matriz de distâncias com 0
        for i in range(size):
            dist.append([])
            for j in range(size):
                dist[i].append(0)
        for i in range(size):
            for j in range(size):
                if graph_matrix[i][j] != 0:
                    dist[i][j] = graph_matrix[i][j]
        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        path_matrix[i][j] = path_matrix[i][k] + path_matrix[k][j]
        return dist, path_matrix