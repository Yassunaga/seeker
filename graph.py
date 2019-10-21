from math import inf

class Graph:

    def __init__(self, size = None):
        self.graph = []
        if size is None:
            size = 10
        for i in range(size):
            self.graph.append([])
            for j in range(size):
                self.graph[i].append(0)

    def teste():
        return "Teste"

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

    # Create mocked distances for the graph
    def mock_distances(graph_matrix, path_matrix):
        # graph_matrix[0][1] = 13
        # graph_matrix[0][9] = 5
        # graph_matrix[1][0] = 13
        # graph_matrix[1][3] = 4
        # graph_matrix[1][4] = 14
        # graph_matrix[2][8] = 3
        # graph_matrix[2][5] = 5
        # graph_matrix[2][6] = 15
        # graph_matrix[3][4] = 6
        # graph_matrix[3][1] = 4
        # graph_matrix[3][5] = 8
        # graph_matrix[3][6] = 7
        # graph_matrix[4][7] = 11
        # graph_matrix[4][1] = 14
        # graph_matrix[4][3] = 6
        # graph_matrix[5][2] = 5
        # graph_matrix[5][9] = 10
        # graph_matrix[5][3] = 8
        # graph_matrix[6][3] = 7
        # graph_matrix[6][8] = 20
        # graph_matrix[6][2] = 15
        # graph_matrix[7][4] = 11
        # graph_matrix[8][6] = 20
        # graph_matrix[8][6] = 20
        # graph_matrix[8][2] = 3
        # graph_matrix[9][5] = 10 
        # graph_matrix[9][0] = 5
        path_matrix[1][2] = [2]
        graph_matrix[1][2] = 3
        
        path_matrix[1][4] = [4]
        graph_matrix[1][4] = 7
        
        path_matrix[2][1] = [1]
        graph_matrix[2][1] = 8

        path_matrix[2][3] = [3]
        graph_matrix[2][3] = 2

        path_matrix[3][1] = [1]
        graph_matrix[3][1] = 5

        path_matrix[3][4] = [4]
        graph_matrix[3][4] = 1

        path_matrix[4][1] = [1]
        graph_matrix[4][1] = 2
        return graph_matrix, path_matrix

    def floyd_warshall(graph_matrix, path_matrix):
        dist = []
        size = len(graph_matrix)
        # Inicializa a matriz de distâncias com 0
        for i in range(size):
            dist.append([])
            for j in range(size):
                dist[i].append(0)
                
                # print(dist[i][j], end=" ")
            # print()
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