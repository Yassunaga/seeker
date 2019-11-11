from flask import Flask
from flask import request
from flask import g
from util import Util
from datetime import datetime
from graph import Graph
from flask_cors import CORS
from math import inf
from copy import copy
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

def getGraph(remove_infinite):
    graph_matrix = copy(graph)
    graphResp = Graph.matrix_to_object(graph,remove_infinite)
    
    # "graph_matrix" : graph_matrix

    response = {
        "graph": graphResp,
        "graph_list" : graph_list,
        "nodes" : nodes,
        "floyd" : floyd,
        "dist" : dist,     
    }
    return response

def getPaths():
    response = {
        "path" : path_matrix
    }
    return response