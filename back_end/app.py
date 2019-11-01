from flask import Flask
from flask import request
from flask import g
from datetime import datetime
from graph import Graph
from flask_cors import CORS
from math import inf
import json
import re

# Graph in text file
dbTextFile = "inputGraph.txt"

#Pre-processing
graph = Graph.graph_from_file(Graph, dbTextFile)
nodes = Graph.nodes_from_file(Graph, dbTextFile)

app = Flask(__name__)
CORS(app)

@app.route("/graph/")
def grafos():
    return getGraph(False)

@app.route("/graph/clean/")
def grafoLimpo():
    return getGraph(True)

def getGraph(remove_infinite):
    # path = Graph.paths_from_file(Graph, dbTextFile)
    graphResp = Graph.matrix_to_object(graph,remove_infinite)
    # path = Graph.create_path_matrix(raph.size)
    response = {
        "graph": graphResp,
        "nodes" : nodes
    }
    return response
