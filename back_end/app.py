from flask import Flask
from flask import request
from datetime import datetime
from graph import Graph
from flask_cors import CORS
from math import inf
import json
import re

app = Flask(__name__)
CORS(app)

@app.route("/graph/")
def grafos():
    return getGraph(False)

@app.route("/graph/clean/")
def grafoLimpo():
    return getGraph(True)

def getGraph(remove_infinite):
    graph = Graph.graph_from_file(Graph, "inputGraph.txt")
    graph = Graph.matrix_to_object(graph,remove_infinite)
    response = {
        "responseGraph": graph
    }
    return response

# @app.route("/grafos/<size>")
# def grafo(size):
#     size = int(size)
#     path = Graph.create_path_matrix(size)
#     graph = Graph.create_graph(size)
#     graph,y = Graph.mock_distances(graph, path)
#     dist,x = Graph.floyd_warshall(graph, path)
#     for i in range(5):
#         for j in range(5):
#             if dist[i][j] == inf: 
#                 dist[i][j] = 0
#     retorno = {
#         0: dist,
#         1: graph
#     }
#     return retorno 