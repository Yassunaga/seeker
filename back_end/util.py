from math import inf
from graph import Graph

class Util:
    def graph_from_file(self, file_name):
        with open(file_name , "r") as file:
            lines = file.readlines()
        file.close()
        graph = Util.lines_to_graph_matrix(Util, lines)
        return graph
    
    def nodes_from_file(self, file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
        nodes = []
        size = 0
        for line in lines:
            nodes.append(size)
            size += 1
        return nodes

    def paths_from_file(self, file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
        path = Util.lines_to_path_matrix(Util, lines)
        return path

    def lines_to_graph_matrix(self, readed_lines):
        lines = []
        for i in readed_lines:
            lines.append(i.split())
        size = len(lines[0])
        grafo = []
        for i in range(size):
            grafo.append([])
            for j,element in enumerate(lines[i]):
                if element == 'inf':
                    grafo[i].append(inf)
                elif element == '\n':
                    continue
                else:
                    grafo[i].append(int(element))
        return grafo
    
    def lines_to_path_matrix(self, readed_lines):
        lines = []
        for i in readed_lines:
            lines.append(i.split())
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
        graph = Util.graph_from_file(Util, "inputGraph.txt")
        for i in range(size):
            for j, element in enumerate(lines[i]):
                if element != 'inf' and i != j:
                    path[i][j] = [j]
        warshall_graph, warshall_path = Graph.floyd_warshall(Graph,graph, path)
        return warshall_path

    def printGraph(self, graph, size):
        for i in range(size):
            for j in range(size):
                print(graph[i][j], end=" ")
            print()

    def none_to_null(self, matrix):
        size = len(matrix[0])
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == None:
                    matrix[i][j] = "null"

    def removeInifinite(self, matrix):
        size = len(matrix[0])
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == inf:
                    matrix[i][j] = "null"
        return matrix