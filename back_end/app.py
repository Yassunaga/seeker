from flask import Flask
from flask import request
from flask import g
from util import Util
from datetime import datetime
from graph import Graph
from flask_cors import CORS
from math import inf
import copy
import json
import re

# Graph in text file
dbTextFile = "inputGraph.txt"

#Pre-processing
graph = Util.graph_from_file(Graph, dbTextFile)
nodes = Util.nodes_from_file(Graph, dbTextFile)
path_matrix = Util.paths_from_file(Graph, dbTextFile)
dist, floyd = Graph.floyd_warshall(Graph,graph,path_matrix)
graph_list = Graph.matrix_to_list(graph, True)

Util.none_to_null(Graph, path_matrix)
app = Flask(__name__)
CORS(app)

@app.route("/graph/")
def grafos():
    return getGraph(False)

@app.route("/graph/clean/")
def grafoLimpo():
    return getGraph(True)

@app.route("/paths/")
def paths():
    return getPaths()

@app.route("/graphMatrix/")
def getGraphMatrix():
    graph2 = Util.graph_from_file(Graph,dbTextFile)
    graph2 = Util.removeInifinite(Graph, graph2)
    response = {
        "graph_matrix" : graph2
    }
    return response

def getGraph(remove_infinite):
    graphResp = Graph.matrix_to_object(graph,remove_infinite)
    # graph2 = Util.graph_from_file(Graph,dbTextFile)
    graph_matrix = copy.deepcopy(graph)
    graph_matrix = Util.removeInifinite(Util, graph_matrix)

    response = {
        "graph": graphResp,
        "graph_list" : graph_list,
        "nodes" : nodes,
        "floyd" : floyd,
        "dist" : dist,     
        "graph_matrix" : graph_matrix
    }
    return response

def getPaths():
    response = {
        "path" : path_matrix
    }
    return response