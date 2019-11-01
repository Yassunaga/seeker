from flask import Flask
from flask import request
from flask import g
from util import Util
from datetime import datetime
from graph import Graph
from flask_cors import CORS
from math import inf
import json
import re

# Graph in text file
dbTextFile = "inputGraph.txt"

#Pre-processing
graph = Util.graph_from_file(Graph, dbTextFile)
nodes = Util.nodes_from_file(Graph, dbTextFile)
path_matrix = Util.paths_from_file(Graph, dbTextFile)

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
    return path_matrix

def getGraph(remove_infinite):
    graphResp = Graph.matrix_to_object(graph,remove_infinite)
    response = {
        "graph": graphResp,
        "nodes" : nodes
    }
    return response
